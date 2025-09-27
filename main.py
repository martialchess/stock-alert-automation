import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# --- ENV VARS ---
load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_FROM")
to_number = os.getenv("TWILIO_TO")
stock_api_key = os.getenv("STOCK_API")
news_api_key = os.getenv("NEWS_API")

# --- CONFIG ---
symbol = "TSLA"
company = "Tesla Inc"
query = '"Tesla stock" OR "Tesla shares" OR TSLA OR "Tesla earnings" OR "Tesla price"'

# --- STOCK API ---
def check_stock(data, symbol, query):
    """Check stock change and trigger news + SMS if needed."""
    time_series = data["Time Series (Daily)"]
    last_2_days = list(time_series.items())[:2]

    today_date, today_values = last_2_days[0]
    yesterday_date, yesterday_values = last_2_days[1]

    today_close = float(today_values["4. close"])
    yesterday_close = float(yesterday_values["4. close"])

    percent_change = ((today_close - yesterday_close) / yesterday_close) * 100
    arrow = "🔺" if percent_change > 0 else "🔻"

    print(f"📅 {today_date} close: {today_close}")
    print(f"📅 {yesterday_date} close: {yesterday_close}")
    print(f"📊 Change: {arrow}{percent_change:.2f}%")

    if abs(percent_change) >= 4:
        articles = get_news(query)
        for article in articles:
            message = (
                f"{symbol}: {arrow}{percent_change:.2f}%\n"
                f"Headline: {article['title']}\n"
                f"Brief: {article['description']}\n"
                f"URL: {article['url']}"
            )
            print("🚨 Sending SMS:", message)
            send_sms(message)

# --- NEWS API ---
def get_news(query, limit=3):
    """Fetch top news articles about a company impacting stock prices."""
    news_url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&"
        f"language=en&"
        f"sortBy=popularity&pageSize={limit}&"
        f"apiKey={news_api_key}"
    )
    response = requests.get(news_url)
    response.raise_for_status()
    articles = response.json().get("articles", [])
    return [
        {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
        }
        for article in articles
    ]

# --- TWILIO ---
def send_sms(message):
    """Send an SMS alert with Twilio."""
    client = Client(account_sid, auth_token)
    sms = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number,
    )
    return sms.sid

# --- MAIN EXECUTION ---
stock_url = (
    f"https://www.alphavantage.co/query?"
    f"function=TIME_SERIES_DAILY&outputsize=compact&symbol={symbol}&apikey={stock_api_key}"
)

response = requests.get(stock_url)
response.raise_for_status()
data = response.json()

if "Time Series (Daily)" in data:
    check_stock(data, symbol, query)
else:
    print("API error:", data)
