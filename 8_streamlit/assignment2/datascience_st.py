import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px  
import plotly.graph_objects as go


st.title("CSV reader")

with st.sidebar:
    blur_amount = st.write("You can upload a csv file \nand see its data as a table \nand you can also see some chart from your file.")


dataframe = st.file_uploader("Choose a csv ...", type=["csv"])


if dataframe is not None:
    # if "df" not in st.session_state:
    st.session_state.df = pd.read_csv(dataframe)
    print(type(st.session_state.df))
    st.success("فایل با موفقیت بارگزاری شد")

    # preprocessing
    # dataframe = pd.read_csv(dataframe)
    st.dataframe(
        st.session_state.df,
    )


if st.button("Check Data", type="primary"):

    df = px.data.tips()
    colors = ['blue','red','green','orange']
    x_data = np.array(list(range(len(st.session_state.df)))) 
    lines = []
    x_tick_index = []
    x_tick_pos = []
    for i,col in enumerate(st.session_state.df.columns):
        max_len = 0
        x_tick_index.append(x_data[len(list(x_data))//2])
        x_tick_pos.append(col)
        y_data = st.session_state.df[col]

        trace1 = go.Scatter(x=x_data , y=y_data, mode='lines', name=col , line=dict(color=colors[i%4]), showlegend=True)

        lines.append(trace1)
        max_len = x_data.max() + 3
 
        layout = go.Layout(
            title=f'Chart of your file',
            xaxis=dict(
                title='first column',
                # tickvals=x_tick_index,  # Positions of the ticks
                # ticktext=x_tick_pos,   # Labels for the ticks
            ),
            yaxis=dict(title="dataframe values")
            )

        fig = go.Figure(data = trace1 , layout=layout)
        # fig.show()

        st.plotly_chart(fig, use_container_width=True)


else:
    st.info("فایل با موفقیت بارگزاری نشده است.")




