
# Livestock Marketplace (Prototype)

## About
A Streamlit prototype for AgriConnect – AI-powered livestock marketplace.
Farmers upload livestock details, and the app fetches fair price suggestions
from an n8n workflow.

## Features
- Farmer inputs: name, breed, weight, health, photo
- Sends data to n8n webhook
- n8n returns AI-powered price suggestion
- Prototype only – demo purpose for OpenAI × NxtWave Buildathon

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
