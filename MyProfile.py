import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Supriya Prakash")
    content="""
    With over 18 years of extensive experience in the Information Technology industry, Supriya is a seasoned professional specializing in the Java/J2EE technology stack. Throughout her career, she has successfully led and delivered complex, enterprise-level software projects across diverse domains, consistently demonstrating a strong blend of technical expertise, leadership, and strategic project oversight.

    """
    st.info(content)

st.text("I have started learning pythin recently.Below are the some apps which I developed in Python.Pleaes take a look")


col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]('url')")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]('url')")