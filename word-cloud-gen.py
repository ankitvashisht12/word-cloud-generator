from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt


filename = "text.txt"
words = ""
with open(filename) as file:
    for lines in file.readlines():
        for word in lines.split(" "):
            words += word + " "
print(words)


wc = WordCloud(width = 400, height = 400, 
                background_color ='white', 
                stopwords = set(STOPWORDS), 
                min_font_size = 10).generate(words)

 

fig = plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wc) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
fig.savefig('line plot.jpg', bbox_inches='tight', dpi=150)

  
plt.show() 
