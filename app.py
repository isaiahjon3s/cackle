from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cackle')
def cackle():
    return render_template('cackle.html')

if __name__ == '__main__':
    app.run(debug=True)