from google.adk.agents import Agent
from google.adk.tools import google_search

root_search_agent = Agent(
    name="search_assistant",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search]
)

# Alias for adk web compatibility
root_agent = root_search_agent