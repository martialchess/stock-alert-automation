# 📈 Tesla Stock Alert Automation

## 🔎 Overview
This project is an **automated stock alert system** that tracks Tesla (TSLA) stock price changes.  
When the stock moves more than a set threshold (default: 5%) between two days, the system:
1. Fetches relevant news articles about Tesla.
2. Sends formatted alerts via Twilio SMS/WhatsApp.

This project blends **finance, automation, and communication APIs** into one workflow.

---

## 🛠️ Tech Stack
- **Python** – Core language
- **Alpha Vantage API** – Stock market data
- **NewsAPI** – News articles relevant to Tesla/stock prices
- **Twilio API** – SMS/WhatsApp notifications
- **dotenv** – Securely load API keys from `.env`
- **Git** – Version control

---

## 🚀 What We Built
- Automated detection of significant stock price changes
- News scraping filtered for financial impact
- Real-time alerts directly to your phone

---

## 📚 What We Learned
- Working with multiple external APIs in Python
- Handling JSON responses & filtering useful data
- Securing credentials with `.env` files
- Automating real-world workflows with minimal manual effort
- Using Twilio to send SMS/WhatsApp programmatically

---

## 🌍 Why It’s Relevant Today
- Financial markets move fast — manual tracking is inefficient.  
- Automation gives **real-time alerts** without constant monitoring.  
- Combines finance + news + communication into a **practical AI/automation workflow**.  
- This kind of system is **directly applicable to traders, analysts, and developers** looking to scale decision-making.

---

## ⚡ Example Alert
TSLA: 🔺5.02%
Headline: Tesla’s stock surges after AI Day
Brief: Investors reacted positively to Tesla’s new AI initiatives.
URL: https://example.com/tesla-news


---

## 🧑‍💻 How to Run
1. Clone repo https://github.com/martialchess/stock-alert-automation.git
2. Create a `.env` file with:

STOCK_API=your_alpha_vantage_api_key
NEWS_API=your_newsapi_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM=+123456789
TWILIO_TO=+987654321

3. Install dependencies:
```bash
pip install requests twilio python-dotenv

4. Run:

   python main.py

🔮 Future Improvements

Extend to multiple stocks (AAPL, AMZN, etc.)

Store news + stock data in a database

Add sentiment analysis on headlines

Build a simple dashboard with Flask/Streamlit