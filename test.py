import google.generativeai as genai

genai.configure(api_key="GOOGLE_API_KEY")

for model in genai.list_models():
    print(model.name)



# # Use an official Python runtime as a parent image
# FROM python:3.9-slim
# # Set the working directory
# WORKDIR /app
# # Copy requirements.txt and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# # Copy the application code
# COPY . .
# # Expose the Streamlit port
# EXPOSE 8501
# # Run the Streamlit application
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
