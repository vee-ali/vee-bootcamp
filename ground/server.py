from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/play')
def grid_one():
    return render_template("index.html",num=3,color="green")

@app.route('/play/<int:num>')
def grid_two(num):
    return render_template("index.html", num=num, color="green")

@app.route('/play/<int:num>/<string:color>')
def grid_three(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)