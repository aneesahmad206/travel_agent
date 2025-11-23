# 🛫 AI Travel Agent (Watsonx Edition)

This Streamlit app is an AI-powered travel agent that generates personalized travel itineraries using **IBM Watsonx**. It automates the process of researching, planning, and organizing your dream vacation, allowing you to explore exciting destinations with ease.

---

## Features

- Research and discover exciting travel destinations, activities, and accommodations  
- Customize your itinerary based on the number of days you want to travel  
- Utilize the power of **Watsonx** to generate intelligent and personalized travel plans  
- Download your itinerary as a calendar (.ics) file to import into Google Calendar, Apple Calendar, or other calendar apps  

---

## Getting Started

### 1. Clone the GitHub repository

```bash
git clone https://github.com/aneesahmad206/travel_agent.git
cd awesome-llm-apps/ai_agent_tutorials/ai_travel_agent
2. Install the required dependencies
```bash
pip install -r requirements.txt
3. Set up API keys
Watsonx API
Sign up for an IBM Watsonx account

Obtain your API key and project ID

Use environment variables to store them securely:

export WATSONX_API_KEY="your_watsonx_api_key"
export WATSONX_PROJECT_ID="your_project_id"
export WATSONX_URL="https://us-south.ml.cloud.ibm.com"
SerpAPI Key
Sign up for a SerpAPI account and obtain your API key


export SERPAPI_KEY="your_serpapi_key"
⚠️ Do not hardcode your API keys in the code. Use environment variables for security.

4. Run the Streamlit App

streamlit run local_travel_agent.py
The local_travel_agent.py file supports both Watsonx cloud and local LLM setups.

How It Works
The AI Travel Agent has two main components:

Researcher Agent
Generates search terms based on the user's destination and travel duration

Searches the web for relevant activities and accommodations using SerpAPI

Planner Agent
Takes research results and user preferences

Generates a personalized draft itinerary including suggested activities, dining options, and accommodations

Using the Calendar Download Feature
After generating your travel itinerary:

Click the Download Itinerary as Calendar (.ics) button next to Generate Itinerary

Save the .ics file to your computer

Import it into your preferred calendar application (Google Calendar, Apple Calendar, Outlook, etc.)

Each day of your itinerary appears as an all-day event in your calendar

Complete details for each day's activities are included in the event description

This feature makes it easy to keep track of your travel plans and access your itinerary across all devices, even offline.

Local vs Cloud Version
local_travel_agent.py: Runs Watsonx locally or with cloud access (requires IBM Watsonx API key and project ID)

Cloud deployment: Use environment variables to keep your API keys secure while deploying on Streamlit Cloud or other hosting platforms
