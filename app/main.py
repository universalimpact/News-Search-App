#Importing flask and newsapi
from flask import Flask,render_template,request
from newsapi import NewsApiClient

app = Flask(__name__)
 
#Uses My API Key
newsapi = NewsApiClient(api_key='35f569d394e44eb8a271c936044ce125')
 
@app.route('/')
def home():
    return render_template('index.html',news='')
     
@app.route('/articles/',methods=['POST']) 
def display_articles():
    #Get the keyword and category from the user
    keyword = request.form['keyword']
    section = request.form['category']
    
    #Get the top headlines given the keyword and category chosen
    news = newsapi.get_top_headlines(q=keyword,category=section,language='en',country="us")
    
    #Send the articles to the html file to display in a user-friendly format
    return render_template('index.html',news=news['articles'])