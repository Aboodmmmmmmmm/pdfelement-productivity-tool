# build c6c77befac
# (auto) c766a1
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
