# Import flask module
from flask import Flask

# create an app using Flask
app = Flask(__name__)

# defined the basic route / and its corresponding request handler
@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()
