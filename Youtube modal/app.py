from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'Wind@wswil24d'  # Used for flashing messages, replace with a secure key



@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
