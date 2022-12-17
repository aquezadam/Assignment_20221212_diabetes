#   • • • Consider the diabetes dataset from day 12 assignment section and perform the
#   following operations using Pandas library

#           -Create a dashboard with at least 2 charts using streamlit
import main
import streamlit as st
st.set_page_config(layout="wide")
title = st.title("Diabetes and Pregnancy")
subtitle = st.subheader("Pima Indians Diabetes Database")
intro_text = st.markdown('''<h6 style= 
                            "text-align:left;
                             color: #ff4b4b;">
                             "This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. 
                             The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on 
                             certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of 
                             these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage."
                             </h6>''',unsafe_allow_html=True)
link_source = "https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database"
source_text = st.write(f"[Source:]({link_source})")
columns_plot = st.columns(2)
columns_plot[0].plotly_chart(main.plot_one, use_container_width=True)
columns_plot[1].plotly_chart(main.plot_two, use_container_width=True)
st.plotly_chart(main.plot_three, use_container_width=True)

note_text = st.markdown('''<h8 style= "text-align:left;"> These charts are based on data before processing. No conclusions can be drawn yet. </h8>''',unsafe_allow_html=True)

