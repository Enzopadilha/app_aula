from flask import Flask


app = Flask(__name__)


@app.route('/')

def hello():

        return("Hello World")

@app.route('/hora')
def hora():
        import time
        return  strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
