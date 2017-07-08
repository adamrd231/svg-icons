
from flask import Flask, request, redirect, render_template, session, flash


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('icons.html',
          title="SVG Icons",
          category="icon",)

@app.route('/color', methods=['POST'])
def color():
    color = request.form['color']
    print(color)
    # Use color variable to assign it's value to the svg



    return render_template('icons.html',
          title="SVG Icons Colored",
          category="icon",
          color=color)

if __name__ == '__main__':
    app.run(debug=True)
