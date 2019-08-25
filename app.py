from flask import Flask, render_template as render
from news import getNews

app = Flask(__name__)

@app.route('/')
def index():
    link_text, links = getNews()
    counter = len(link_text)
    return render('index.html',link=links,link_text=link_text,counter=counter)

if __name__ == "__main__":
    app.run(debug=True)
