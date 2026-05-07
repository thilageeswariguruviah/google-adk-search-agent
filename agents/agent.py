from google.adk.agents import Agent
from google.adk.tools import google_search

def great_tool(name: str)-> str:
    return f"Hello, {name}! How can i assist you today?"

root_agent = Agent(
    name="search_assistant",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search]
)
