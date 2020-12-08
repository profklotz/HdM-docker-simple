from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hdm_simple():
    return 'Hello, HdM!'


if __name__ == '__main__':
    app.run()
