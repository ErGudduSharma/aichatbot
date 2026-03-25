# 🤖 AI ChatBot (Google Gemini + PostgreSQL)

A Streamlit-based AI Chatbot driven by **Google Generative AI** (`gemini-2.0-flash` / `gemini-2.5-flash`) that automatically logs all user queries and AI responses directly into a connected **PostgreSQL** database (e.g., AWS RDS). Built with containerization and cloud deployments in mind.

## ✨ Key Features
- **Generative AI Responses**: Connects seamlessly with Google Gemini API to retrieve context-aware and high-quality responses.
- **Streamlit Interface**: Lightweight, user-friendly Web UI.
- **Query Logging Mechanism**: Stores all interactions (`user_input`, `bot_response`) natively into a structured relational database architecture to maintain chat history and logs.
- **Containerization Support**: Easy-to-build Dockerfile instructions included for cross-compatibility deployment on VM environments (like AWS EC2).
- **Scalable Architecture**: Connects remote applications directly to powerful managed database solutions like AWS RDS PostgreSQL.

## 🛠️ Tech Stack
- **Python Framework**: `Streamlit`
- **AI/LLM Engine**: `google-generativeai` (Gemini)
- **Database**: `PostgreSQL` powered by `psycopg2`
- **Deployment**: `Docker`

## 📁 File Structure

```
aichatbot/
│
├── app.py                # Main Streamlit web application & DB logic
├── main.py               # Auxiliary script
├── requirements.txt      # Python dependencies
├── docker_steps.txt      # Manual instructions on how to Dockerize and deploy
├── postgre_steps.txt     # Instructions for AWS EC2 and RDS postgres connection
└── README.md             # Project documentation (this file)
```

## ⚙️ Prerequisites & Setup

### 1. Variables Configuration (`.env`)
Before you initialize the application, create a root file named `.env` and fill it with your credentials:

```ini
GOOGLE_API_KEY="your-google-api-key"

# Database Configuration (AWS RDS or Local PostgreSQL)
DB_HOST="your-rds-endpoint.amazonaws.com"
DB_NAME="your_db_name"
DB_USER="your_db_username"
DB_PASSWORD="your_db_password"
DB_PORT="5432"
```

### 2. Local Installation
You need a Python 3.9+ runtime to spin this up on your local machine.

```bash
# Install required libraries
pip install -r requirements.txt

# Start the Streamlit server
streamlit run app.py
```
> The local Streamlit web application runs on `http://localhost:8501`.

---

## 🐳 Docker Deployment

The application runs seamlessly in isolated Docker containers, especially when deployed to Ubuntu servers like AWS EC2.

1. **Build the Image**
   ```bash
   docker build -t query_bot_app .
   ```
2. **Run the Container**
   ```bash
   docker run -d -p 8501:8501 --env-file .env query_bot_app
   ```
3. Open `http://<YOUR_EC2_IP>:8501` to use the chatbot live.

---

## ☁️ Setting Up Cloud Persistence (AWS RDS / EC2)

This app supports continuous persistence. A PostgreSQL datatable `query_logs` is created on initialization.

1. Set up an AWS RDS PostgreSQL instance with Public Access permitted (for testing).
2. Install `postgresql-client` on your EC2 instance.
3. Verify your DB interactions utilizing `psql`:

```bash
psql -h <your-rds-endpoint.amazonaws.com> -U <username> -d <dbname> -p 5432
```

**Beneficial SQL Verification Queries:**
- Verify the logs table: `\dt`
- Output the 5 specific latest Chat Logs: 
  ```sql
  SELECT * FROM query_logs ORDER BY id DESC LIMIT 5;
  ```
- Print total history size: `SELECT COUNT(*) FROM query_logs;`
