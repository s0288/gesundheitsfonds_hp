from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    headline="abc"
    paragraph="def"
    return render_template('main.html', 
        headline=headline, paragraph=paragraph)

if __name__ == '__main__':
    app.run(debug=True)
