from flask import Flask, request, jsonify
from skpy import Skype

app = Flask(__name__)
skype_client = None  # Initialize Skype client as None

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    global skype_client

    try:
        skype_client = Skype(username, password,"./token.txt")  # Authenticate with Skype
        token = skype_client.conn.tokens  # Retrieve the authentication token
        
        return jsonify(token), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Add a route for sending messages using the obtained token (example)
@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.json.get('username')
    password = request.json.get('password')
    chatId = request.json.get('chatId')
    message = request.json.get('message')

    global skype_client

    try:
        skype_client = Skype(None, None,"./token.txt")  # Authenticate with Skype
        token = skype_client.conn.tokens  # Retrieve the authentication token
        
        contact_username = chatId
        contact = skype_client.contacts[contact_username]

        # Send a text message
        message_content = message
        contact.chat.sendMsg(message_content)
        return jsonify(token), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask server