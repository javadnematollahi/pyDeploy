from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# class Database:
#     def __init__(self):
#         file = "todo.db"
#         try: 
#             conn = sqlite3.connect(file) 
#             cursor_obj = conn.cursor()
        
#             # Drop the GEEK table if already exists.
#             cursor_obj.execute("DROP TABLE IF EXISTS todo")
            
#             # Creating table
#             table = """ 
#                     CREATE TABLE "tasks" (
#                         "id" INTEGER NOT NULL,
#                         "title" TEXT NOT NULL,
#                         "description" TEXT,
#                         "time" TEXT,
#                         "status" INTEGER  NOT NULL,
#                         PRIMARY KEY("id" AUTOINCREMENT)
#                     ); 
#                     """
            
#             cursor_obj.execute(table)
#             conn.commit()
#             print("Database todo.db formed.") 
#         except: 
#             print("Database todo.db not formed.")



#     def get_task(self):
#         query="SELECT * FROM tasks"
#         result=self.cursor.execute(query)
#         tasks=result.fetchall()
#         return tasks
    
#     def add_new_tasks(self,new_title,new_description,time,status):
#         try:
#             query= f"INSERT INTO tasks('title','description','time','status') VALUES('{new_title}','{new_description}','{time}',{status})"
#             self.cursor.execute(query)
#             self.conn.commit()
#             return True
#         except :
#             return False

#     # def update_tasks(self,new_title,new_description,time,status):
#     #     try:
#     #         query= f"UPDATE tasks SET is_done='{r}' WHERE id={id_num}"
#     #         self.cursor.execute(query)
#     #         self.conn.commit()
#     #         return True
#     #     except :
#     #         return False

#     def remove_task(self,id_num,obj):
#         query=f"DELETE FROM tasks WHERE id={id_num}" 
#         self.cursor.execute(query)
#         self.conn.commit()
#         obj.read_from_database()



#     def task_done(self,id_num,r):
#         # print(r)
#         # query_read_state=f"SELECT is_done FROM tasks WHERE id={id_num} "
#         # result=self.cursor.execute(query_read_state)
#         # state=result.fetchall()
#         # state1=state[0][0]
#         # if state1=='1':
#         #     state1='0'
#         # elif state1=='0': 
#         #     state1='1'
#         if r==2:
#             r=1
#         query=f"UPDATE tasks SET is_done='{r}' WHERE id={id_num}"
#         self.cursor.execute(query)
#         self.conn.commit()