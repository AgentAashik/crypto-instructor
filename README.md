# 💰 Crypto Instructor AI Agent

An **AI-powered instructor** that teaches people how to use cryptocurrency for **daily spending**, **long-term savings**, and **secure usage**.  
The agent also **fetches latest crypto news** to keep users updated on security, regulations, and opportunities.

---

## ✨ Features
- 🔐 **Daily Crypto Guidance** – Explains wallet usage, safe transactions, and daily spending tips.  
- 💸 **Long-Term Savings Advice** – Instructs on strategies for storing and growing crypto assets.  
- 🛡️ **Security Awareness** – Warns about scams, phishing, and storage safety.  
- 📰 **Real-Time Updates** – Pulls news from [CryptoCompare API](https://min-api.cryptocompare.com/).  
- 🧠 **Memory** – Remembers past questions in the session for continuity.  

---

## ⚡ Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/AgentAashik/crypto-instructor-agent.git
   cd crypto-instructor-agent

2. Install dependencies:

   ```bash
   pip install langchain langchain-openai requests
   ```

3. Export your OpenAI API key:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

4. Run the agent:

   ```bash
   python crypto_instructor_agent.py
   ```

---

## 🛠 Example Usage

```text
You: How do I safely store my Bitcoin?
🤖 Agent: The safest method is using a **hardware wallet**...
```

```text
You: What’s the latest crypto regulation news?
🤖 Agent: Here’s what I found:
- SEC pushes new framework... (link)
- EU MiCA rules start in 2025... (link)
```

---

## 📌 Notes

* This is an **educational tool** – not financial advice.
* The agent uses the **CryptoCompare API** for news.
* Works best with the **OpenAI GPT-4o-mini model** for speed + reasoning.

---

## 📜 License

MIT License. Free to use and modify.
