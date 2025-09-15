# step 1 - setup streamlit
import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="AI Mental Health Therapist", page_icon="🤖", layout="wide")
st.title("Personal AI Mental Health Therapist")

# initailize chat history in session state

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# step 2 - user able to ask questions

user_query = st.chat_input("How are you, Can i help you with something?", key="input")
if user_query:
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    # AI Agent Exist here
    res = requests.post(BACKEND_URL, json={"message": user_query})
    st.session_state.chat_history.append({"role": "assistant", "content": f'{res.json()["res"]}WITH TOOL: {res.json()["tool_called"]}'})

# step 3 - display the answer/ show response from backend

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

