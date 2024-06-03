from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

class Messages(SQLModel, table=True):
    __table_args__ = {'extend_existing': True} 
    id: int | None = Field(default=None, primary_key=True)
    message_user: str
    message_ai: str
    user_id: int = Field(foreign_key="users.id")
    users: "Users" = Relationship(back_populates="messages")

class Users(SQLModel, table=True):
    __table_args__ = {'extend_existing': True} 
    id: int | None = Field(default=None, primary_key=True)
    usernames: str
    passwords: str
    email: str
    messages: Messages | None = Relationship(back_populates="users")

class Sqlmethods:
    def __init__(self) -> None:
        sqlite_file_name = "database.db"
        sqlite_url = f"sqlite:///{sqlite_file_name}"
        # sqlite_url = "postgresql://root:u45kF342z32zHR5pIY3BSrJw@chatbot:5432/postgres"
        self.engine = create_engine(sqlite_url, echo=True)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def add_user(self, username, password, email):
        with Session(self.engine) as session:
            user = Users(usernames=username, passwords=password, email=email)
            session.add(user)
            session.commit()

    def add_message_to_user(self, message_user, message_ai, user):
        with Session(self.engine) as session:
            message = Messages(message_user=[message_user], message_ai=[message_ai], users=user)
            session.add(message)
            session.commit()

    def update_message_of_a_user(self, message_user, message_ai, user):
        with Session(self.engine) as session:
            user = select(Users).where(Users.id == user.id)
            user = session.exec(user)
            user = user.first()

            statement = select(Messages).where(Messages.users == user)
            res = session.exec(statement)
            message = res.first()
            if message is None:
                message = Messages(message_user=message_user, message_ai=message_ai, users=user)
            else:
                message.message_user += f",{message_user}"
                message.message_ai += f",{message_ai}"
            session.add(message)
            session.commit()
            session.refresh(message)

    def select_message_of_a_user(self, user):
        with Session(self.engine) as session:
            statement = select(Messages).where(Messages.users == user)
            res = session.exec(statement)
            message = res.first()
            if message is None:
                return "", ""
            else:
                message_user = message.message_user
                message_ai = message.message_ai
                return message_user, message_ai

    def select_a_user(self, username, password):
        with Session(self.engine) as session:
            statement = select(Users).where(Users.usernames==username, Users.passwords==password)
            user_res = session.exec(statement)
            user = user_res.first()
            if user is None:
                return False
            else:
                return user

    def delete_messages_of_a_user(self, user):
        with Session(self.engine) as session:
            statement = select(Messages).where(Messages.users == user)
            res = session.exec(statement)
            message = res.one()

            if message is None:
                print(f"There's no messages for {user.username}")
            else:
                session.delete(message)
                session.commit()

                print(f"Deleted messages of {user.username} is completed")

    def delete_a_user(self, user):
        with Session(self.engine) as session:
            statement = select(Messages).where(Messages.users == user)
            res = session.exec(statement)
            message = res.one()

            if message is None:
                print(f"There's no user which name is {user.username}")
            else:
                session.delete(message)
                session.commit()
                session.delete(user)
                session.commit()
                print(f"Deleted messages of {user.username} is completed")
