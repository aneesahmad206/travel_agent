# 🛫 AI Travel Agent (Watsonx Edition)

An AI-powered travel assistant built using **IBM Watsonx** and **Streamlit**. This application automates researching destinations, planning activities, and organizing your trip into a downloadable calendar format.

---

## 🌟 Features

✅ Discover exciting travel destinations, activities, and accommodations
✅ Personalized itineraries based on destination and trip duration
✅ Powered by **IBM Watsonx** for intelligent itinerary generation
✅ Download your plan as a **Calendar (.ics)** file
✅ Import into Google, Apple, or Outlook calendar

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aneesahmad206/travel_agent.git
cd travel_agent
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set Up API Keys

This project requires:

* IBM Watsonx API key
* IBM Watsonx Project ID
* SerpAPI key (for web research)

Set them as environment variables:

```bash
export WATSONX_API_KEY="your_watsonx_api_key"
export WATSONX_PROJECT_ID="your_project_id"
export WATSONX_URL="https://us-south.ml.cloud.ibm.com"

export SERPAPI_KEY="your_serpapi_key"
```

⚠️ **Do NOT hardcode API keys** in the code or commit them to GitHub.

---

### 4. Run the Streamlit App

```bash
streamlit run local_travel_agent.py
```

This file supports both:

* ✅ Watsonx Cloud
* ✅ Local LLM setups

---

## 🧠 How It Works

The AI Travel Agent includes two intelligent components:

### 🔍 Researcher Agent

* Generates search queries based on destination and duration
* Searches the web using SerpAPI
* Collects activities, landmarks, and accommodations

### 🗓️ Planner Agent

* Uses research results and user preferences
* Produces a structured daily travel itinerary
* Suggests activities, dining, and lodging

---

## 📅 Calendar Download Feature

After generating your itinerary:

1. Click **Download Itinerary as Calendar (.ics)**
2. Save the file
3. Import into:

   * Google Calendar
   * Apple Calendar
   * Outlook
   * Any calendar app

Each day appears as an **all‑day event**, including:

* Activity details
* Locations
* Notes and recommendations

This allows you to:
✅ Access plans offline
✅ View on mobile devices
✅ Stay organized while traveling

---

## 🌐 Local vs Cloud

| Mode                    | Description                            |
| ----------------------- | -------------------------------------- |
| `local_travel_agent.py` | Runs locally or with Watsonx Cloud     |
| Cloud Deployment        | Use environment variables for security |

---

## 🛠️ Deployment

You can deploy this app on:

* Streamlit Cloud
* IBM Cloud

Ensure API keys are configured using environment variables.

---

## 📂 Project Structure

```
travel_agent/
├── local_travel_agent.py
├── requirements.txt
└── README.md
```

---


## 🤝 Contributing

Pull requests are welcome! Feel free to submit improvements or new features.

---

## ⭐ Support

If you like this project, please ⭐ the repository!
