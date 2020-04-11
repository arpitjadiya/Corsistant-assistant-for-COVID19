from flask import Flask           
from flask import render_template
from getLatestNews import send_news
app = Flask(__name__)
import time            


titles=[] 

news=[]
@app.route("/")
def hello():                 
    return  render_template('index.html',titles=titles, news=news)
if __name__ == "__main__":
    titles,news=send_news()  
    time.sleep(9.4)        
    app.run()                 