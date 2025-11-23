#c5c4b72d49acc20c2084500c903b2185a7020438385cc6c7580a9420c8793e5d
#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

# from textwrap import dedent
# from agno.agent import Agent
# from agno.run.agent import RunOutput
# from agno.tools.serpapi import SerpApiTools
# from agno.models.base import Model
# import streamlit as st
# import re
# from icalendar import Calendar, Event
# from datetime import datetime, timedelta

# # -----------------------
# # ✅ Watsonx Credentials
# # -----------------------
# from ibm_watsonx_ai import APIClient, Credentials
# from ibm_watsonx_ai.foundation_models import ModelInference

# WATSONX_API_KEY = "MsCr_EafVvZEQWhFl9JAL5orVYLq3qOhx_KyPqHFerRP"
# WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
# PROJECT_ID = "2e0aa627-23e6-4396-a484-7fd8f6e9ea20"
# SERPAPI_KEY = "c5c4b72d49acc20c2084500c903b2185a7020438385cc6c7580a9420c8793e5d"

# # -----------------------
# # Set up Watsonx client
# # -----------------------
# creds = Credentials(url=WATSONX_URL, api_key=WATSONX_API_KEY)
# client = APIClient(credentials=creds)

# # -----------------------
# # Agno-compatible Watsonx Model
# # -----------------------
# class WatsonxAgnoModel(Model):
#     def __init__(self, client, project_id, model_id="ibm/granite-3-2-8b-instruct"):
#         # Pass model_id as required 'id' argument to Agno Model
#         super().__init__(id=model_id)
#         self.client = client
#         self.project_id = project_id
#         self.model_id = model_id

#     # Required method for synchronous call
#     def invoke(self, prompt: str, **kwargs) -> str:
#         max_tokens = kwargs.get("max_tokens", 500)
#         model = ModelInference(
#             model_id=self.model_id,
#             api_client=self.client,
#             project_id=self.project_id,
#             params={"max_new_tokens": max_tokens}
#         )
#         result = model.generate(prompt)
#         return result['results'][0]['generated_text']

#     # Minimal implementations for abstract methods
#     def _parse_provider_response(self, response):
#         return response

#     def _parse_provider_response_delta(self, response):
#         return response

#     def ainvoke(self, prompt, **kwargs):
#         return self.invoke(prompt, **kwargs)

#     def ainvoke_stream(self, prompt, **kwargs):
#         return self.invoke(prompt, **kwargs)

#     def invoke_stream(self, prompt, **kwargs):
#         return self.invoke(prompt, **kwargs)

# # -----------------------
# # ICS file generator
# # -----------------------
# def generate_ics_content(plan_text: str, start_date: datetime = None) -> bytes:
#     cal = Calendar()
#     cal.add('prodid', '-//AI Travel Planner//github.com//')
#     cal.add('version', '2.0')
#     if start_date is None:
#         start_date = datetime.today()
#     day_pattern = re.compile(r'Day (\d+)[:\s]+(.*?)(?=Day \d+|$)', re.DOTALL)
#     days = day_pattern.findall(plan_text)
#     if not days:
#         event = Event()
#         event.add('summary', "Travel Itinerary")
#         event.add('description', plan_text)
#         event.add('dtstart', start_date.date())
#         event.add('dtend', start_date.date())
#         event.add("dtstamp", datetime.now())
#         cal.add_component(event)
#     else:
#         for day_num, day_content in days:
#             day_num = int(day_num)
#             current_date = start_date + timedelta(days=day_num - 1)
#             event = Event()
#             event.add('summary', f"Day {day_num} Itinerary")
#             event.add('description', day_content.strip())
#             event.add('dtstart', current_date.date())
#             event.add('dtend', current_date.date())
#             event.add("dtstamp", datetime.now())
#             cal.add_component(event)
#     return cal.to_ical()

# # -----------------------
# # Streamlit UI
# # -----------------------
# st.title("AI Travel Planner using Watsonx + SerpAPI")
# st.caption("Plan your next adventure with AI")

# if 'itinerary' not in st.session_state:
#     st.session_state.itinerary = None

# if WATSONX_API_KEY and SERPAPI_KEY:

#     # Watsonx Agno-compatible model
#     watson_model = WatsonxAgnoModel(client, PROJECT_ID)

#     # Researcher Agent
#     researcher = Agent(
#         name="Researcher",
#         role="Searches for travel destinations and activities",
#         model=watson_model,
#         description=dedent("""\
#             You are a world-class travel researcher. Generate search terms,
#             search the web using SerpAPI, analyze results and return the most relevant findings.
#         """),
#         instructions=[
#             "Generate 3 search terms",
#             "Search Google using `search_google`",
#             "Analyze all results and return the 10 best"
#         ],
#         tools=[SerpApiTools(api_key=SERPAPI_KEY)],
#         add_datetime_to_context=True,
#     )

#     # Planner Agent
#     planner = Agent(
#         name="Planner",
#         role="Generates a travel itinerary",
#         model=watson_model,
#         description=dedent("""\
#             Create a detailed day-by-day travel itinerary using research results.
#         """),
#         instructions=[
#             "Use research results to build itinerary",
#             "Include activities, food, transport, accommodations",
#             "Write clearly and structured",
#         ],
#         add_datetime_to_context=True,
#     )

#     # User input
#     destination = st.text_input("Where do you want to go?")
#     num_days = st.number_input("How many days?", min_value=1, max_value=30, value=7)

#     col1, col2 = st.columns(2)

#     # Generate itinerary
#     with col1:
#         if st.button("Generate Itinerary"):
#             with st.spinner("Planning your trip..."):
#                 response: RunOutput = planner.run(
#                     f"Create a {num_days}-day itinerary for {destination}",
#                     stream=False
#                 )
#                 st.session_state.itinerary = response.content
#                 st.write(response.content)

#     # Download ICS
#     with col2:
#         if st.session_state.itinerary:
#             ics_content = generate_ics_content(st.session_state.itinerary)
#             st.download_button(
#                 label="Download as Calendar (.ics)",
#                 data=ics_content,
#                 file_name="travel_itinerary.ics",
#                 mime="text/calendar"
#             )

# else:
#     st.warning("API keys missing. Please insert them in the code.")


# WATSONX_API_KEY = "MsCr_EafVvZEQWhFl9JAL5orVYLq3qOhx_KyPqHFerRP"
# WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
# PROJECT_ID = "2e0aa627-23e6-4396-a484-7fd8f6e9ea20"
# SERPAPI_KEY = "c5c4b72d49acc20c2084500c903b2185a7020438385cc6c7580a9420c8793e5d"
from textwrap import dedent
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.tools.serpapi import SerpApiTools
from agno.models.base import Model, ModelResponse
import streamlit as st
import re
from icalendar import Calendar, Event
from datetime import datetime, timedelta

# -----------------------
# ✅ Watsonx Credentials
# -----------------------
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

WATSONX_API_KEY = "MsCr_EafVvZEQWhFl9JAL5orVYLq3qOhx_KyPqHFerRP"
WATSONX_URL = "https://us-south.ml.cloud.ibm.com"
PROJECT_ID = "2e0aa627-23e6-4396-a484-7fd8f6e9ea20"
SERPAPI_KEY = "c5c4b72d49acc20c2084500c903b2185a7020438385cc6c7580a9420c8793e5d"

# -----------------------
# Set up Watsonx client
# -----------------------
creds = Credentials(url=WATSONX_URL, api_key=WATSONX_API_KEY)
client = APIClient(credentials=creds)

# -----------------------
# Agno-compatible Watsonx Model
# -----------------------
class WatsonxAgnoModel(Model):
    def __init__(self, client, project_id, model_id="ibm/granite-3-2-8b-instruct"):
        super().__init__(id=model_id)
        self.client = client
        self.project_id = project_id
        self.model_id = model_id

    def invoke(self, assistant_message=None, messages=None, **kwargs):
        """Agno-compatible invoke, returns ModelResponse object"""
        # Build prompt from messages or assistant_message
        if messages:
            prompt = " ".join([m.content for m in messages])
        elif assistant_message:
            prompt = assistant_message.content
        else:
            prompt = kwargs.get("prompt", "")

        max_tokens = kwargs.get("max_tokens", 500)

        # Watsonx ModelInference
        model = ModelInference(
            model_id=self.model_id,
            api_client=self.client,
            project_id=self.project_id,
            params={"max_new_tokens": max_tokens}
        )
        result_text = model.generate(prompt)['results'][0]['generated_text']

        # Return ModelResponse with content only
        return ModelResponse(content=result_text)

    # Abstract methods required by Agno
    def _parse_provider_response(self, response): return response
    def _parse_provider_response_delta(self, response): return response
    def ainvoke(self, **kwargs): return self.invoke(**kwargs)
    def ainvoke_stream(self, **kwargs): return self.invoke(**kwargs)
    def invoke_stream(self, **kwargs): return self.invoke(**kwargs)

# -----------------------
# ICS file generator
# -----------------------
def generate_ics_content(plan_text: str, start_date: datetime = None) -> bytes:
    cal = Calendar()
    cal.add('prodid', '-//AI Travel Planner//github.com//')
    cal.add('version', '2.0')

    if start_date is None:
        start_date = datetime.today()

    day_pattern = re.compile(r'Day (\d+)[:\s]+(.*?)(?=Day \d+|$)', re.DOTALL)
    days = day_pattern.findall(plan_text)

    if not days:
        event = Event()
        event.add('summary', "Travel Itinerary")
        event.add('description', plan_text)
        event.add('dtstart', start_date.date())
        event.add('dtend', start_date.date())
        event.add("dtstamp", datetime.now())
        cal.add_component(event)
    else:
        for day_num, day_content in days:
            day_num = int(day_num)
            current_date = start_date + timedelta(days=day_num - 1)
            event = Event()
            event.add('summary', f"Day {day_num} Itinerary")
            event.add('description', day_content.strip())
            event.add('dtstart', current_date.date())
            event.add('dtend', current_date.date())
            event.add("dtstamp", datetime.now())
            cal.add_component(event)

    return cal.to_ical()

# -----------------------
# Streamlit UI
# -----------------------
st.title("AI Travel Planner using Watsonx + SerpAPI")
st.caption("Plan your next adventure with AI")

if 'itinerary' not in st.session_state:
    st.session_state.itinerary = None

if WATSONX_API_KEY and SERPAPI_KEY:

    # Watsonx Agno-compatible model
    watson_model = WatsonxAgnoModel(client, PROJECT_ID)

    # Researcher Agent
    researcher = Agent(
        name="Researcher",
        role="Searches for travel destinations and activities",
        model=watson_model,
        description=dedent("""\
            You are a world-class travel researcher. Generate search terms,
            search the web using SerpAPI, analyze results and return the most relevant findings.
        """),
        instructions=[
            "Generate 3 search terms",
            "Search Google using `search_google`",
            "Analyze all results and return the 10 best"
        ],
        tools=[SerpApiTools(api_key=SERPAPI_KEY)],
        add_datetime_to_context=True,
    )

    # Planner Agent
    planner = Agent(
        name="Planner",
        role="Generates a travel itinerary",
        model=watson_model,
        description=dedent("""\
            Create a detailed day-by-day travel itinerary using research results.
        """),
        instructions=[
            "Use research results to build itinerary",
            "Include activities, food, transport, accommodations",
            "Write clearly and structured",
        ],
        add_datetime_to_context=True,
    )

    # User input
    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days?", min_value=1, max_value=30, value=7)

    col1, col2 = st.columns(2)

    # Generate itinerary
    with col1:
        if st.button("Generate Itinerary"):
            if destination.strip() == "":
                st.warning("Please enter a destination.")
            else:
                prompt_text = f"Create a {num_days}-day itinerary for {destination}"
                with st.spinner("Planning your trip..."):
                    response: RunOutput = planner.run(prompt_text, stream=False)
                    st.session_state.itinerary = response.content
                    st.write(response.content)

    # Download ICS
    with col2:
        if st.session_state.itinerary:
            ics_content = generate_ics_content(st.session_state.itinerary)
            st.download_button(
                label="Download as Calendar (.ics)",
                data=ics_content,
                file_name="travel_itinerary.ics",
                mime="text/calendar"
            )

else:
    st.warning("API keys missing. Please insert them in the code.")
