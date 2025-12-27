from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use ONLY this model (works 100%)
model = genai.GenerativeModel("gemini-2.5-flash")

def my_output(query):
    response = model.generate_content(query)
    return response.text

# -------- Streamlit UI --------
st.set_page_config(page_title="Query Bot")

st.title("🤖 Query Bot")

user_input = st.text_input("Ask your question:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        answer = my_output(user_input)
        st.subheader("Response:")
        st.write(answer)


# Add this after configuring the API

# for m in genai.list_models():
#     print(m.name)

# # Or in Streamlit:
# st.write("Available models:")
# for m in genai.list_models():
#     st.write(f"- {m.name}")