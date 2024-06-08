from flask import Flask 

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/dojo")
def dojo():
    return"Dojo"

@app.route("/say/<name>")
def say(name):
    return ("Hi " + name)

@app.route("/repeat/<int:times>/<string>")
def repeatWord(times, string):
    repeated= string * times
    return repeated

if __name__ == "__main__":
    app.run(debug=True, port= 5001)
