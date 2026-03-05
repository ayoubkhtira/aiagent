import streamlit as st
from agent import run_agent

st.set_page_config(page_title="AI Agent", layout="wide")

st.title("🤖 AI Agent Local Gratuit")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Pose ta question")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})

    response = run_agent(user_input)

    st.session_state.messages.append({"role":"ai","content":response})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"🧑‍💻 : {msg['content']}")
    else:
        st.write(f"🤖 : {msg['content']}")
