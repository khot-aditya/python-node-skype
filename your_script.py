# your_script.py
from skpy import Skype
import sys

if len(sys.argv) != 5:
    print("Usage: python your_script.py <username> <password> <chatID> <message>")
    sys.exit(1)

# Retrieve command-line arguments
username = sys.argv[1]
password = sys.argv[2]
chatID = sys.argv[3]
message = sys.argv[4]

try:
    # Create a Skype connection
    sk = Skype(username, password)

    contact_username = chatID
    contact = sk.contacts[contact_username]

    # Send a text message
    message_content = message
    contact.chat.sendMsg(message_content)

    print("Message sent successfully.")

except Exception as e:
    print(f"Error in Skype connection: {e}")
    sys.exit(1)

finally:
    # Close the Skype connection to ensure proper cleanup
    if sk:
        sk.conn.close()
        print("Skype connection closed.")