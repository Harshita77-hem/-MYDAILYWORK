# ============================================================
#  Simple Rule-Based Chatbot
#  Uses if-elif-else + keyword matching for basic conversation
# ============================================================

def get_response(user_input):
    """
    Takes a user message, matches it against known patterns,
    and returns an appropriate response string.
    """

    # Normalise: lowercase + strip surrounding spaces
    text = user_input.lower().strip()

    # ── 1. GREETINGS ─────────────────────────────────────────
    if any(word in text for word in ["hello", "hi", "hey", "howdy", "greetings"]):
        return "Hey there! 👋 I'm EduBot. How can I help you today?"

    # ── 2. HOW ARE YOU ────────────────────────────────────────
    elif any(phrase in text for phrase in ["how are you", "how r u", "how are u",
                                           "how's it going", "wassup", "what's up"]):
        return "I'm doing great, thanks for asking! 😊 What's on your mind?"

    # ── 3. BOT'S NAME ─────────────────────────────────────────
    elif any(phrase in text for phrase in ["your name", "who are you",
                                           "what are you", "introduce yourself"]):
        return ("I'm EduBot 🤖 — a simple rule-based chatbot built in Python. "
                "I'm here to chat and answer your questions!")

    # ── 4. ABOUT AIML ─────────────────────────────────────────
    elif any(word in text for word in ["aiml", "ai ml", "artificial intelligence",
                                       "machine learning", "ai and ml"]):
        return ("AIML stands for Artificial Intelligence & Machine Learning. 🧠\n"
                "It's a fascinating branch of Computer Science that teaches machines\n"
                "to learn from data and make intelligent decisions.\n"
                "Key topics: Python, Statistics, Neural Networks, Deep Learning & more!")

    # ── 5. ABOUT COLLEGE / DEPARTMENT ────────────────────────
    elif any(word in text for word in ["college", "university", "department",
                                       "campus", "institute", "faculty"]):
        return ("I belong to the AIML Department! 🏫\n"
                "We offer cutting-edge courses in Artificial Intelligence,\n"
                "Machine Learning, Data Science, and Computer Vision.\n"
                "It's one of the most exciting departments to be part of!")

    # ── 6. COURSES / SUBJECTS ─────────────────────────────────
    elif any(word in text for word in ["course", "subject", "curriculum",
                                       "syllabus", "study", "learn"]):
        return ("Some popular AIML subjects include:\n"
                "  📌 Python Programming\n"
                "  📌 Data Structures & Algorithms\n"
                "  📌 Machine Learning\n"
                "  📌 Deep Learning & Neural Networks\n"
                "  📌 Natural Language Processing\n"
                "  📌 Computer Vision\n"
                "Which one interests you the most?")

    # ── 7. JOKES ──────────────────────────────────────────────
    elif any(word in text for word in ["joke", "funny", "laugh", "humor"]):
        return ("Here's one for you 😄:\n"
                "Why do programmers prefer dark mode?\n"
                "Because light attracts bugs! 🐛")

    # ── 8. CREATOR / WHO MADE YOU ────────────────────────────
    elif any(phrase in text for phrase in ["who made you", "who built you",
                                           "who created you", "your creator"]):
        return ("I was created by a Python enthusiast as a beginner-friendly\n"
                "rule-based chatbot project. 💻 Simple, clean, and effective!")

    # ── 9. THANKS ─────────────────────────────────────────────
    elif any(word in text for word in ["thank", "thanks", "thank you",
                                       "thx", "ty", "appreciate"]):
        return "You're very welcome! 😊 Feel free to ask anything else."

    # ── 10. TIME / DATE ───────────────────────────────────────
    elif any(word in text for word in ["time", "date", "today", "day"]):
        import datetime
        now = datetime.datetime.now()
        return (f"Right now it's {now.strftime('%I:%M %p')} on "
                f"{now.strftime('%A, %d %B %Y')}. 🕐")

    # ── 11. HELP ──────────────────────────────────────────────
    elif any(word in text for word in ["help", "assist", "support", "option"]):
        return ("Sure! Here are things you can ask me about:\n"
                "  • Greetings (hi, hello)\n"
                "  • My name / who I am\n"
                "  • AIML / Artificial Intelligence\n"
                "  • College / Department info\n"
                "  • Courses & subjects\n"
                "  • Jokes 😄\n"
                "  • Current time & date\n"
                "  • Type 'bye' or 'exit' to quit")

    # ── 12. EXIT ──────────────────────────────────────────────
    elif any(word in text for word in ["bye", "exit", "quit", "goodbye",
                                       "see you", "cya", "farewell"]):
        return "EXIT"   # Sentinel value — main loop will catch this

    # ── 13. EMPTY INPUT ───────────────────────────────────────
    elif text == "":
        return "Hmm, it looks like you didn't type anything. Go ahead, ask me something! 😊"

    # ── 14. DEFAULT / FALLBACK ───────────────────────────────
    else:
        return ("Sorry, I didn't understand that. 🤔\n"
                "Type 'help' to see what I can do!")


# ════════════════════════════════════════════════════════════
#  MAIN LOOP — keeps the conversation going until user exits
# ════════════════════════════════════════════════════════════
def main():
    print("=" * 55)
    print("       Welcome to EduBot 🤖 — Your AI Assistant!")
    print("  Type 'help' for options  |  'bye' or 'exit' to quit")
    print("=" * 55)
    print()

    while True:
        # Get input from the user
        user_input = input("You: ")

        # Get the bot's response
        response = get_response(user_input)

        # Check for exit sentinel
        if response == "EXIT":
            print("EduBot: Goodbye! 👋 Have a wonderful day. See you soon!")
            break

        # Print response with a blank line for readability
        print(f"EduBot: {response}")
        print()


# Entry point
if __name__ == "__main__":
    main()
