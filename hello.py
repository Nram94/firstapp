from flask import Flask

app = Flask(__name__) # Create an instans of the Flask object using module's name as parameter.


@app.route("/") # Flask uses decorators for URL routing
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(port=5000, debug=True)