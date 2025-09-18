import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import requests

# -------------------------
# CONFIG
# -------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set your key as env var
CRYPTO_NEWS_API = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"  # Free crypto news API

# -------------------------
# HELPER: Fetch crypto news
# -------------------------
def fetch_crypto_news(limit=3):
    try:
        response = requests.get(CRYPTO_NEWS_API)
        if response.status_code == 200:
            articles = response.json().get("Data", [])[:limit]
            news_items = [f"- {a['title']} ({a['url']})" for a in articles]
            return "\n".join(news_items)
        else:
            return "Could not fetch latest news right now."
    except Exception as e:
        return f"Error fetching news: {e}"

# -------------------------
# PROMPT TEMPLATE
# -------------------------
prompt = ChatPromptTemplate.from_template("""
You are a **Crypto Instructor AI Agent**.

Your tasks:
1. Teach users how to use crypto safely on a daily basis (spending, transacting, wallets).
2. Provide long-term strategies for savings and investments.
3. Always warn about security, scams, and safe storage.
4. Stay updated by summarizing latest crypto news.

Latest Crypto Updates:
{crypto_news}

Conversation History:
{history}

User Question:
{user_input}

Answer in a clear, practical, and user-friendly manner.
""")

# -------------------------
# AGENT SETUP
# -------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)

memory = ConversationBufferMemory(memory_key="history", return_messages=True)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True
)

# -------------------------
# MAIN LOOP
# -------------------------
def main():
    print("🚀 Crypto Instructor AI Agent started! (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Stay safe with crypto.")
            break

        crypto_news = fetch_crypto_news()
        response = chain.run(user_input=user_input, crypto_news=crypto_news)
        print(f"\n🤖 Agent: {response}\n")

if __name__ == "__main__":
    main()
