# 🐰 bunny.ai: AI-Powered College Guidance Chatbot

bunny.ai is a web-based chatbot that helps students explore academic options, career paths and college-related questions through conversational AI. It uses Flask for the backend and Google's Gemini API to generate responses.

🌐 **Live demo:** [Try bunny.ai](https://college-buddy-ai-1.onrender.com)
*(Hosted on Render's free tier, so the first load can take up to a minute while it wakes up.)*

📦 **Repository:** [college-buddy-ai](https://github.com/dhritiiixpaw/college-buddy-ai)

## 🖼️ Preview

![bunny.ai chatbot interface](screenshots/Screenshot%202026-10-25%20214846.png)

## ✨ Features

- AI-generated responses using the Google Gemini API
- Suggested prompts for course exploration, fees and budgeting, and career guidance
- Conversation history stored in the Flask session
- Voice input using browser speech recognition, where supported
- Responsive chat interface with a pastel-themed design
- New-chat button to clear the current conversation
- Error handling for API and connectivity issues

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI integration:** Google Gemini API, Google Gen AI SDK (`google-genai`)
- **Frontend:** HTML, CSS, JavaScript
- **Configuration:** python-dotenv
- **Hosting:** Render

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- A Google Gemini API key ([get one from Google AI Studio](https://aistudio.google.com/))
- Git

### 1. Clone the repository

```bash
git clone https://github.com/dhritiiixpaw/college-buddy-ai.git
cd college-buddy-ai/college-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```powershell
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask python-dotenv google-genai
```

### 4. Configure environment variables

Create a `.env` file next to `app.py`:

```env
GEMINI_API_KEY=your_gemini_api_key
FLASK_SECRET_KEY=your_secret_key
```

Replace the placeholder values with your own credentials.

### 5. Run the application

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## ⚙️ How It Works

1. The frontend sends the user's message to the Flask backend.
2. Flask passes the recent conversation history to the Gemini API.
3. Gemini generates a response based on the conversation.
4. The response is returned to the frontend and shown in the chat.
5. Recent messages are kept in the Flask session so the chat keeps its context.

## ⚠️ Please Note

bunny.ai uses a generative AI model, so like any AI it can sometimes give wrong or outdated answers. Check important details such as fees, eligibility and deadlines with the college itself.

## 🔐 Security

- API keys and secret values are stored in environment variables.
- `.env`, `.venv/` and other sensitive files are not committed to version control.
- If an API key is ever exposed publicly, revoke it and generate a new one.

## 🌷 Future Improvements

- Add more structured college information and verified resources
- Improve conversation persistence and personalization
- Expand testing and error handling

## 👩‍💻 Author

**Dhritileena Roy**

- [GitHub Profile](https://github.com/dhritiiixpaw)
- [Portfolio: My Little Corner](https://dhritiiixpaw.github.io/my-little-corner/)
