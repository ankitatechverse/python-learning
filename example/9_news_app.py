"""
Use the NewsAPI and the requests module to fetch the daily news related to different topics.
Go to: https://newsapi.org/
and explore the various options to build you application
"""

import requests
from datetime import datetime, timedelta

API_KEY = '81f'  # Replace with your NewsAPI key
BASE_URL = 'https://newsapi.org/v2/'

CATEGORIES = {
    '1': 'business',      # stock
    '2': 'entertainment', # bollywood
    '3': 'health',
    '4': 'education',     # not a NewsAPI category, will use 'general'
    '5': 'general'        # latest
}

LANGUAGES = {
    '1': 'en',  # English
    '2': 'hi',  # Hindi
    '3': 'gu',  # Gujarati
    '4': 'mr',  # Marathi
    '5': 'ta',  # Tamil
    '6': 'te',  # Telugu
    '7': 'bn',  # Bengali
    '8': 'ur',  # Urdu
}

def get_user_input():
    print("Select Category:")
    print("1. Stock (Business)")
    print("2. Bollywood (Entertainment)")
    print("3. Health")
    print("4. Education")
    print("5. Latest News")
    cat_choice = input("Enter choice (1-5): ").strip()
    category = CATEGORIES.get(cat_choice, 'general')
    if category == 'education':
        category = 'general'  # NewsAPI does not have 'education' category

    country = input("Enter country code (e.g., 'in' for India, 'us' for USA): ").strip().lower()

    print("Select Language:")
    for k, v in LANGUAGES.items():
        print(f"{k}. {v}")
    lang_choice = input("Enter language choice (1-8): ").strip()
    language = LANGUAGES.get(lang_choice, 'en')

    return category, country, language

def fetch_news(category, country, language):
    # Top headlines
    params = {
        'apiKey': API_KEY,
        'category': category,
        'country': country,
        'language': language,
        'pageSize': 5
    }
    top_url = BASE_URL + 'top-headlines'
    top_resp = requests.get(top_url, params=params)
    top_data = top_resp.json()

    print("\n--- Top Headlines ---")
    if top_data.get('articles'):
        for art in top_data['articles']:
            print(f"- {art['title']}")
    else:
        print("No top headlines found.")

    # Latest 5 days news
    print("\n--- News from Last 5 Days ---")
    for i in range(5):
        day = datetime.now() - timedelta(days=i)
        date_str = day.strftime('%Y-%m-%d')
        params = {
            'apiKey': API_KEY,
            'q': category,
            'language': language,
            'from': date_str,
            'to': date_str,
            'sortBy': 'publishedAt',
            'pageSize': 5
        }
        everything_url = BASE_URL + 'everything'
        everything_resp = requests.get(everything_url, params=params)
        everything_data = everything_resp.json()
        print(f"\nDate: {date_str}")
        if everything_data.get('articles'):
            for art in everything_data['articles']:
                print(f"- {art['title']}")
        else:
            print("No articles found for this day.")

if __name__ == "__main__":
    category, country, language = get_user_input()
    fetch_news(category, country, language)