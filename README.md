# bunny.ai — AI-Powered College Guidance Chatbot

bunny.ai is a web-based chatbot designed to help students explore academic options, career paths, and college-related questions through conversational AI. It uses Flask for the backend and Google's Gemini API to generate responses.

**Repository:** [college-buddy-ai](https://github.com/dhritiiixpaw/college-buddy-ai)

## Features

- AI-generated responses using the Google Gemini API
- Suggested prompts for course exploration, fees and budgeting, and career guidance
- Conversation history stored in the Flask session
- Voice input using browser speech recognition, where supported
- Responsive chat interface with a pastel-themed design
- New-chat functionality to clear the current conversation
- Error handling for API and connectivity issues

## Tech Stack

- **Backend:** Python, Flask
- **AI Integration:** Google Gemini API, Google Gen AI SDK
- **Frontend:** HTML, CSS, JavaScript
- **Configuration:** python-dotenv

## Project Structure

```text
college-buddy-ai/
├── app.py
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

*Note: Update the structure above to match the actual files in your repository.*

## Getting Started

### Prerequisites

- Python 3.10 or later
- A Google Gemini API key
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/dhritiiixpaw/college-buddy-ai.git
cd college-buddy-ai
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install flask python-dotenv google-genai
```

### 4. Configure Environment Variables

Create a `.env` file in the project root, alongside `app.py`:

```env
GEMINI_API_KEY=your_gemini_api_key
FLASK_SECRET_KEY=your_secret_key
```

Replace the placeholder values with your own credentials.

### 5. Run the Application

```bash
python app.py
```

Open the following URL in your browser:

`http://127.0.0.1:5000`

## How It Works

1. The frontend sends user messages to the Flask backend.
2. Flask passes the recent conversation history to the Gemini API.
3. Gemini generates a response based on the conversation and configured system instructions.
4. The response is returned to the frontend and displayed in the chat interface.
5. Recent messages are maintained in the Flask session.

## Security

- Store API keys and secret values in environment variables.
- Do not commit `.env`, `.venv/`, or other sensitive files to version control.
- If an API key has been exposed publicly, revoke it and generate a replacement.

## Future Improvements

- Deploy the application for public access
- Add more structured college information and verified resources
- Improve conversation persistence and personalization
- Expand testing and error handling

## Author

**Dhritii**

- [GitHub Profile](https://github.com/dhritiiixpaw)
- [Project Repository](https://github.com/dhritiiixpaw/college-buddy-ai)
