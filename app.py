from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Basic route to check if the server is working
@app.route('/')
def home():
    return "Welcome to Mohan Kirushna's Chatbot API!"

# Helper function to process user messages and generate bot replies
def get_bot_reply(user_message):
    user_message = user_message.lower()  # Normalize user input
    
    # Define basic replies
    if "hi" in user_message or "hello" in user_message:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_message:
        return "I'm doing great, thank you for asking! How about you?"
    elif "what are you doing" in user_message or "what r u doing" in user_message:
        return "I'm here to chat with you! How can I help?"
    elif "portfolio" in user_message or "projects" in user_message:
        return "You can check out my work on my portfolio at 'projects.html' where I showcase various projects I've worked on."
    elif "skills" in user_message:
        return "I have experience in Python, Flask, HTML, CSS, JavaScript, Three.js, and machine learning."
    elif "github" in user_message:
        return "You can find my projects and code on my GitHub at https://github.com/Mohankirushna."
    elif "contact" in user_message or "reach me" in user_message:
        return "You can reach me through my portfolio website or email me at my official contact."
    elif "name" in user_message:
        return "My name is Mohan Kirushna R, and I am a passionate software developer."
    elif "resume" in user_message:
        return "You can download my resume from the 'Downloadable Resume' section of my portfolio."
    else:
        return "I'm sorry, I didn't understand that. Can you ask something else?"

# Chatbot API route
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')  # Get the user message from the request body
    
    # Validate the input and generate a reply
    if user_message:
        bot_reply = get_bot_reply(user_message)
    else:
        bot_reply = "Please send a message!"
    
    # Return the bot's reply as a JSON response
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
