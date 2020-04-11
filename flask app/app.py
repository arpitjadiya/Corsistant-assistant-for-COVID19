from flask import Flask           
from flask import render_template
from getLatestNews import send_news
app = Flask(__name__)            

@app.route("/")                  
def hello():
    titles,news=send_news()                     
    return  render_template('index.html',titles=titles, news=news)
if __name__ == "__main__":        
    app.run()                 