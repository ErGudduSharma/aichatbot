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










from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
import psycopg2

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# Database connection
def connect_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS query_logs (
        id SERIAL PRIMARY KEY,,
        user_input TEXT,
        bot_response TEXT
    );
    """)
    conn.commit()
    cur.close()
    conn.close()

def log_query(user_input, bot_response):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO query_logs (user_input, bot_response) VALUES (%s, %s);", (user_input, bot_response))
    conn.commit()
    cur.close()
    conn.close()

def my_output(query):
    response = model.generate_content(query)
    return response.text

#### UI Development using streamlit 

st.set_page_config(page_title="QUERY_BOT")
st.header("QUERY_BOT")
input = st.text_input("Input " , key = "input")
submit = st.button("Ask your query")

create_table()



# psql -h database-1.cxs8oe0mk1mm.ap-south-1.rds.amazonaws.com -U postgres -d database-1 -p 5432