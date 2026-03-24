from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Name: Yashwardhan Singh | AppID: 2410459"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)