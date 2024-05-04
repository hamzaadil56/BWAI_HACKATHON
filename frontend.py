import streamlit as st
import requests

st.title("EQ Mentor")
st.subheader("I understand your feelings...")

text_input = st.text_input(label="",
                           placeholder="Express yourself without hesitation", key="text_input")
if st.button("Submit"):
    response = requests.post(
        f"http://127.0.0.1:8000/submit-feelings", json={"prompt": text_input})
    st.write(response.text)
