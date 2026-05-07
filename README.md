# Google ADK Search Assistant

A conversational AI assistant built with Google's Agent Development Kit (ADK) that can search the web and answer questions using real-time information.

## Features

- **Web Search Integration**: Uses Google Search tool to fetch current information
- **Gemini 2.5 Flash Model**: Powered by Google's latest language model
- **Session Management**: In-memory session handling for conversation context
- **Event Streaming**: Real-time response streaming
- **Async Execution**: Built with asyncio for efficient processing

## Project Structure

```
.
├── agents/
│   ├── agent.py           # Alternative agent configuration
│   └── search_agent.py    # Main search agent with Google Search tool
├── .adk/                  # ADK artifacts and cache
├── .env                   # Environment variables (API key)
├── config.py              # Configuration loader
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Components

### Search Agent (`agents/search_agent.py`)
- **Name**: search_assistant
- **Model**: gemini-2.5-flash
- **Tools**: Google Search
- **Purpose**: Answers user questions using web search when needed

### Main Application (`main.py`)
- Sets up ADK Runner with in-memory session service
- Creates an App instance with the search agent
- Handles user input and streams AI responses
- Example query: "What is happening in AI today?"

### Configuration (`config.py`)
- Loads environment variables from .env file
- Manages Google API key

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your API key in .env**:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Dependencies

- `google-adk`: Google Agent Development Kit
- `python-dotenv`: Environment variable management

## How It Works

1. The application loads the Google API key from the .env file
2. Creates an in-memory session service for conversation management
3. Initializes the search agent with Google Search capability
4. Sets up an ADK App and Runner
5. Processes user queries and streams responses
6. The agent automatically uses Google Search when needed to answer questions

## Usage Example

The default example in `main.py` demonstrates asking about current AI news:

```python
user_input = "What is happening in AI today?"
```

The agent will search the web and provide an up-to-date response based on current information.

## Customization

To modify the agent's behavior, edit `agents/search_agent.py`:
- Change the `instruction` to adjust the agent's personality
- Add more tools to extend capabilities
- Switch to a different model if needed

## Notes

- Sessions are stored in-memory and will be lost when the application stops
- The agent uses Google Search automatically when it needs current information
- Responses are streamed in real-time through the event system
