from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

st.title("Open ai emailing system")
userinput=st.text_input("enter your details that you want to write")
submitbtn=st.button("generate email")
Summarization=st.button("Summarization")
language_input=st.text_input("Enter your preffered language")
Language=st.button("change Language")

if 'arr' not in st.session_state:
    st.session_state.arr = []

if submitbtn :
    if userinput:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You va a good knowlage off everything "},
                {"role": "user", "content": f"write a 200 words paragraph based on : {userinput} "}
            ]
            )
        
        context=st.text_area("Email",completion.choices[0].message.content,height=600)
        st.session_state.arr.append(context)
        


if Summarization:
    completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You va a good knowlage off everything "},
                {"role": "user", "content": f"write short summarization of  : {st.session_state.arr[0]} "}
            ]
            )
    summerizationtext=st.text_area("summarization Text",completion.choices[0].message.content,height=300)
    
if Language and language_input:
    completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You va a good knowlage off every language "},
                {"role": "user", "content": f"convert text {st.session_state.arr[0]} to {language_input} language "}
            ]
            )
    language_change_text=st.text_area("Text",completion.choices[0].message.content,height=600)
