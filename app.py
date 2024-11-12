from flask import Flask, render_template
import requests
import time
from datetime import datetime
import os

app = Flask(__name__)

# You can get a free API key from https://newsapi.org/
NEWS_API_KEY = 'dbf736bcb8d44511b34908cb40f8b844'  # Replace with your API key
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

def get_news():
    try:
        params = {
            'country': 'in',  # Change to your preferred country code
            'apiKey': NEWS_API_KEY,
            'pageSize': 10  # Number of news items to fetch
        }
        
        response = requests.get(NEWS_API_ENDPOINT, params=params)
        
        if response.status_code == 200:
            news_data = response.json()
            news_items = []
            
            for article in news_data.get('articles', []):
                # Convert timestamp to readable format
                published_at = datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00'))
                formatted_time = published_at.strftime('%B %d, %Y %I:%M %p')
                
                news_items.append({
                    'title': article.get('title', ''),
                    'content': article.get('description', ''),
                    'time': formatted_time,
                    'url': article.get('url', ''),
                    'image': article.get('urlToImage', ''),
                    'source': article.get('source', {}).get('name', '')
                })
            
            return news_items
        else:
            print(f"Error fetching news: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"Error getting news: {e}")
        return []

@app.route('/')
def index():
    news_items = get_news()
    return render_template('index.html', news_items=news_items)

if __name__ == '__main__':
    app.run(debug=True)