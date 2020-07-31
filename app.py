from flask import Flask, render_template
import os
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    pass


if __name__ == "__main__":
    app.run(debug=True)