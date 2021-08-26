# Imports necessary libraries
from flask import Flask 
# Define the app
app = Flask(__name__)

# Get a welcoming message once you start the server.
@app.route('/')
def home():
    return 'Home sweet home updates!'

# If the file is run directly,start the app.
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")