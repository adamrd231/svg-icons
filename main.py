
from flask import Flask, request, redirect, render_template, session, flash


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('icons.html',
          title="SVG Icons",
          category="icon",)


if __name__ == '__main__':
    app.run(debug=True)
