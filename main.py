import os
from dotenv import load_dotenv

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.apps import App

from agents.search_agent import root_search_agent

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

session_service = InMemorySessionService()

# Create an App with the agent
app = App(
    name="search_app",
    root_agent=root_search_agent
)

runner = Runner(
    app=app,
    session_service=session_service
)

if __name__ == "__main__":
    import asyncio
    from google.genai import types
    
    user_input = "What is happening in AI today?"
    
    # Create session first
    asyncio.run(session_service.create_session(
        app_name="search_app",
        user_id="user1",
        session_id="session1"
    ))
    
    content = types.Content(
        role="user",
        parts=[types.Part(text=user_input)]
    )

    events = runner.run(
        user_id="user1",
        session_id="session1",
        new_message=content
    )

    print("\nAI Response:\n")

    for event in events:
        if hasattr(event, "content") and event.content:
            if hasattr(event.content, "parts") and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, "text"):
                        print(part.text)