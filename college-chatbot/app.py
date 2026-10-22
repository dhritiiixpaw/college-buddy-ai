
import os

from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

# Keep the Gemini model that you successfully tested.
MODEL = "gemini-3.5-flash-lite"

# Keep the recent conversation short enough to send with each request.
MAX_HISTORY_MESSAGES = 12

SYSTEM_INSTRUCTION = """
You are College Buddy, a friendly AI college guidance assistant.

Help students explore courses, subjects, study strategies, and career options.
Be conversational, supportive, clear, and encouraging.
Understand casual language, slang, spelling mistakes, and follow-up questions.
Use recent conversation history to understand references such as "that course"
or "what about the other option?"

Never invent official college fees, placements, admission deadlines, or policies.
If you do not know an official college-specific fact, say so and recommend
checking the college's official website or admissions office.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_response():
    msg = request.form.get("msg", "").strip()

    if not msg:
        return "Please type a message first.", 400

    if len(msg) > 2000:
        return "Please keep your message under 2,000 characters.", 400

    if client is None:
        app.logger.error("GEMINI_API_KEY is missing.")
        return (
            "Bunny's AI isn't configured yet. Please check your .env setup.",
            503,
        )

    # Keep the last five exchanges (up to 10 messages), then add the new
    # question. This gives Gemini recent context without growing endlessly.
    history = session.get("chat_history", [])[-10:]
    history.append({"role": "user", "text": msg})

    contents = [
        {
            "role": item["role"],
            "parts": [{"text": item["text"]}],
        }
        for item in history
    ]

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7,
                max_output_tokens=400,
            ),
        )

        reply = response.text

        if not reply:
            reply = (
                "I couldn't come up with a reply just now. "
                "Could you try asking me another way? 🐰"
            )

        history.append({"role": "model", "text": reply})
        session["chat_history"] = history[-MAX_HISTORY_MESSAGES:]

        return reply

    except Exception as error:
        app.logger.exception("Gemini request failed.")

        # Gemini may be temporarily busy or your request quota may be reached.
        error_details = str(error).lower()
        status_code = (
            getattr(error, "code", None)
            or getattr(error, "status_code", None)
        )

        if (
            status_code == 429
            or "429" in error_details
            or "resource_exhausted" in error_details
            or "quota" in error_details
        ):
            return (
                "Bunny's getting lots of questions right now! 🐰💗 "
                "Please wait a little and try again.",
                429,
            )

        if (
            status_code == 503
            or "503" in error_details
            or "unavailable" in error_details
            or "overloaded" in error_details
        ):
            return (
                "Gemini is a little busy at the moment. 🌷 "
                "Please wait a few seconds and try again.",
                503,
            )

        if (
            status_code in (400, 401, 403, 404)
            or "api key" in error_details
            or "permission denied" in error_details
            or "not found" in error_details
        ):
            return (
                "Bunny couldn't connect to the AI service. "
                "Please check the setup and your terminal for details.",
                502,
            )

        return (
            "Oops, bunny hit a little bump! 🐰 "
            "Please try again in a moment.",
            502,
        )


@app.route("/history")
def get_history():
    """Return conversation history in the format used by the chat page."""
    messages = session.get("chat_history", [])
    conversations = []
    pending_user_message = None

    for item in messages:
        if item.get("role") == "user":
            pending_user_message = item.get("text", "")
        elif item.get("role") == "model" and pending_user_message is not None:
            conversations.append(
                {
                    "user": pending_user_message,
                    "bot": item.get("text", ""),
                }
            )
            pending_user_message = None

    # Include the latest user message if a reply hasn't been saved yet.
    if pending_user_message is not None:
        conversations.append({"user": pending_user_message, "bot": ""})

    return jsonify(conversations)


@app.route("/clear", methods=["POST"])
def clear_history():
    session.pop("chat_history", None)
    return jsonify({"message": "Conversation cleared."})


if __name__ == "__main__":
    if not app.secret_key:
        raise RuntimeError(
            "FLASK_SECRET_KEY is missing from your .env file."
        )

    app.run(debug=True)
