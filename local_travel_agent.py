# from textwrap import dedent
# from agno.agent import Agent
# from agno.run.agent import RunOutput
# from agno.tools.serpapi import SerpApiTools
# import streamlit as st
# import re
# from agno.models.ollama import Ollama
# from icalendar import Calendar, Event
# from datetime import datetime, timedelta


# def generate_ics_content(plan_text:str, start_date: datetime = None) -> bytes:
#     """
#         Generate an ICS calendar file from a travel itinerary text.

#         Args:
#             plan_text: The travel itinerary text
#             start_date: Optional start date for the itinerary (defaults to today)

#         Returns:
#             bytes: The ICS file content as bytes
#         """
#     cal = Calendar()
#     cal.add('prodid','-//AI Travel Planner//github.com//' )
#     cal.add('version', '2.0')

#     if start_date is None:
#         start_date = datetime.today()

#     # Split the plan into days
#     day_pattern = re.compile(r'Day (\d+)[:\s]+(.*?)(?=Day \d+|$)', re.DOTALL)
#     days = day_pattern.findall(plan_text)

#     if not days: # If no day pattern found, create a single all-day event with the entire content
#         event = Event()
#         event.add('summary', "Travel Itinerary")
#         event.add('description', plan_text)
#         event.add('dtstart', start_date.date())
#         event.add('dtend', start_date.date())
#         event.add("dtstamp", datetime.now())
#         cal.add_component(event)  
#     else:
#         # Process each day
#         for day_num, day_content in days:
#             day_num = int(day_num)
#             current_date = start_date + timedelta(days=day_num - 1)
            
#             # Create a single event for the entire day
#             event = Event()
#             event.add('summary', f"Day {day_num} Itinerary")
#             event.add('description', day_content.strip())
            
#             # Make it an all-day event
#             event.add('dtstart', current_date.date())
#             event.add('dtend', current_date.date())
#             event.add("dtstamp", datetime.now())
#             cal.add_component(event)

#     return cal.to_ical()


# # Set up the Streamlit app
# st.title("AI Travel Planner using Llama-3.2 ")
# st.caption("Plan your next adventure with AI Travel Planner by researching and planning a personalized itinerary on autopilot using local Llama-3")

# # Initialize session state to store the generated itinerary
# if 'itinerary' not in st.session_state:
#     st.session_state.itinerary = None

# # Get SerpAPI key from the user
# serp_api_key = st.text_input("Enter Serp API Key for Search functionality", type="password")

# if serp_api_key:
#     researcher = Agent(
#         name="Researcher",
#         role="Searches for travel destinations, activities, and accommodations based on user preferences",
#         model=Ollama(id="llama3.2"),
#         description=dedent(
#             """\
#         You are a world-class travel researcher. Given a travel destination and the number of days the user wants to travel for,
#         generate a list of search terms for finding relevant travel activities and accommodations.
#         Then search the web for each term, analyze the results, and return the 10 most relevant results.
#         """
#         ),
#         instructions=[
#             "Given a travel destination and the number of days the user wants to travel for, first generate a list of 3 search terms related to that destination and the number of days.",
#             "For each search term, `search_google` and analyze the results."
#             "From the results of all searches, return the 10 most relevant results to the user's preferences.",
#             "Remember: the quality of the results is important.",
#         ],
#         tools=[SerpApiTools(api_key=serp_api_key)],
#         add_datetime_to_context=True,
#     )
#     planner = Agent(
#         name="Planner",
#         role="Generates a draft itinerary based on user preferences and research results",
#         model=Ollama(id="llama3.2"),
#         description=dedent(
#             """\
#         You are a senior travel planner. Given a travel destination, the number of days the user wants to travel for, and a list of research results,
#         your goal is to generate a draft itinerary that meets the user's needs and preferences.
#         """
#         ),
#         instructions=[
#             "Given a travel destination, the number of days the user wants to travel for, and a list of research results, generate a draft itinerary that includes suggested activities and accommodations.",
#             "Ensure the itinerary is well-structured, informative, and engaging.",
#             "Ensure you provide a nuanced and balanced itinerary, quoting facts where possible.",
#             "Remember: the quality of the itinerary is important.",
#             "Focus on clarity, coherence, and overall quality.",
#             "Never make up facts or plagiarize. Always provide proper attribution.",
#         ],
#         add_datetime_to_context=True,
#     )

#     # Input fields for the user's destination and the number of days they want to travel for
#     destination = st.text_input("Where do you want to go?")
#     num_days = st.number_input("How many days do you want to travel for?", min_value=1, max_value=30, value=7)

#     col1, col2 = st.columns(2)
    
#     with col1:
#         if st.button("Generate Itinerary"):
#             with st.spinner("Processing..."):
#                 # Get the response from the assistant
#                 response: RunOutput = planner.run(f"{destination} for {num_days} days", stream=False)
#                 # Store the response in session state
#                 st.session_state.itinerary = response.content
#                 st.write(response.content)
    
#     # Only show download button if there's an itinerary
#     with col2:
#         if st.session_state.itinerary:
#             # Generate the ICS file
#             ics_content = generate_ics_content(st.session_state.itinerary)
            
#             # Provide the file for download
#             st.download_button(
#                 label="Download Itinerary as Calendar (.ics)",
#                 data=ics_content,
#                 file_name="travel_itinerary.ics",
#                 mime="text/calendar"
#             )

#c5c4b72d49acc20c2084500c903b2185a7020438385cc6c7580a9420c8793e5d
#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
from textwrap import dedent
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.tools.serpapi import SerpApiTools
from agno.models.openai import OpenAIChat  # Agno's OpenAI wrapper
import streamlit as st
import re
from icalendar import Calendar, Event
from datetime import datetime, timedelta

# -----------------------
# ✅ INSERT YOUR KEYS HERE
# -----------------------
OPENAI_API_KEY = "your key"  # replace with your OpenAI key
SERPAPI_KEY = "your key"    # replace with your SerpAPI key
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


st.title("AI Travel Planner using OpenAI + SerpAPI")
st.caption("Plan your next adventure with AI")

if 'itinerary' not in st.session_state:
    st.session_state.itinerary = None

if OPENAI_API_KEY and SERPAPI_KEY:

    # Researcher Agent
    researcher = Agent(
        name="Researcher",
        role="Searches for travel destinations and activities",
        model=OpenAIChat("gpt-4.1-mini", api_key=OPENAI_API_KEY),  # ✅ pass model as first argument
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
        model=OpenAIChat("gpt-4.1-mini", api_key=OPENAI_API_KEY),  # ✅ pass model as first argument
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

    destination = st.text_input("Where do you want to go?")
    num_days = st.number_input("How many days?", min_value=1, max_value=30, value=7)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate Itinerary"):
            with st.spinner("Planning your trip..."):
                response: RunOutput = planner.run(
                    f"Create a {num_days}-day itinerary for {destination}",
                    stream=False
                )
                st.session_state.itinerary = response.content
                st.write(response.content)

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
