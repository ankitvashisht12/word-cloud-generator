import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
import os
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import random



app = Flask(__name__)



def save_word_cloud(data):
    text = data.get("text")
    maxnum = data['maxnum']
    if 'stopwords' in data:
        isStopwords = True
    else: isStopwords = False


    if len(maxnum) > 0:
        maxNum = int(maxnum)
    else: maxNum = 200

    if isStopwords:    
        wc = WordCloud(width = 100, height = 100, 
                    background_color ='white',
                    stopwords=',!?. ',
                    min_font_size = 10, max_words=maxNum).generate(text)
    else:
        wc = WordCloud(width = 400, height = 400, 
                background_color ='white', 
                min_font_size = 10, max_words=maxNum).generate(text)

    # saving image
    imgCode = text[-1]+text[0]+str(random.randint(0,100))
    fig = plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wc) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    fig.savefig('static/imgs/word-cloud-' + imgCode +'.jpg', bbox_inches='tight', dpi=150)
    return imgCode


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result", methods=["POST"])
def result():

    data = request.form
    imgCode = save_word_cloud(data)
   
    return render_template("result.html", img=imgCode)


if __name__ == "__main__":
    app.run(debug=True)