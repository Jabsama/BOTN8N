<div align="center">

# 🤖 VoltageGPU Telegram AI Assistant

<img src="https://img.shields.io/badge/Powered%20by-VoltageGPU-blue?style=for-the-badge&logo=nvidia" alt="VoltageGPU">
<img src="https://img.shields.io/badge/Built%20with-n8n-orange?style=for-the-badge&logo=n8n" alt="n8n">
<img src="https://img.shields.io/badge/Platform-Telegram-26A5E4?style=for-the-badge&logo=telegram" alt="Telegram">

<br/>

<img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
<img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=flat-square" alt="Production Ready">
<img src="https://img.shields.io/badge/Model-DeepSeek--R1-purple?style=flat-square" alt="DeepSeek">

<br/><br/>

**🚀 Deploy an AI-powered Telegram bot in minutes using n8n and VoltageGPU's decentralized GPU infrastructure**

[Quick Start](#-quick-start) • [Features](#-features) • [Installation](#-installation) • [Documentation](#-documentation) • [Support](#-support)

</div>

---

## 🔥 Launch Bot Instantly from Terminal

No n8n? No problem! Run the bot directly:

<div align="center">

```bash
# 🚀 One-line quick start
python start-bot.py
```

</div>

That's it! The bot starts immediately with:
- 📊 Live statistics dashboard
- 🔄 Auto-restart on errors  
- 📝 Real-time logging
- 🎯 Direct Telegram link

---

## 🎯 What is This?

A **production-ready Telegram bot** that leverages **VoltageGPU's API** to provide intelligent AI responses at **70-90% lower cost** than traditional cloud providers. Built with **n8n workflow automation** for easy deployment and customization.

### 💡 Perfect For:
- 🏢 **Businesses** wanting AI customer support
- 👨‍💻 **Developers** building AI-powered apps
- 🎓 **Educators** creating interactive learning bots
- 🚀 **Startups** needing affordable AI infrastructure

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎨 Core Features
- ⚡ **Lightning Fast** - Responses in 1-2 seconds
- 🧠 **Smart AI** - Powered by DeepSeek-R1 model
- 💰 **Cost Effective** - 70-90% cheaper than AWS/GCP
- 🔒 **Secure** - No hardcoded secrets
- 📊 **Analytics Ready** - Optional logging support

</td>
<td width="50%">

### 🛠️ Technical Features
- 🔄 **No-Code Setup** - Visual n8n workflow
- 🌐 **API Examples** - Python, TypeScript, cURL
- 📝 **Well Documented** - Complete architecture docs
- 🎯 **Production Ready** - Error handling included
- 🚀 **Scalable** - Handles 1000+ req/min

</td>
</tr>
</table>

---

## 🚀 Quick Start

### 📋 Prerequisites

<table>
<tr>
<td align="center" width="33%">
<img src="https://n8n.io/favicon.ico" width="48" height="48"><br>
<b>n8n Account</b><br>
<a href="https://n8n.io">Get Started →</a>
</td>
<td align="center" width="33%">
<img src="https://telegram.org/favicon.ico" width="48" height="48"><br>
<b>Telegram Bot</b><br>
<a href="https://t.me/botfather">Create Bot →</a>
</td>
<td align="center" width="33%">
<img src="https://voltagegpu.com/favicon.ico" width="48" height="48"><br>
<b>VoltageGPU API</b><br>
<a href="https://voltagegpu.com">Get API Key →</a>
</td>
</tr>
</table>

### ⚡ 5-Minute Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/voltagegpu-telegram-askai.git
cd voltagegpu-telegram-askai

# 2. Copy environment template
cp .env.example .env

# 3. Add your credentials to .env
# TELEGRAM_BOT_TOKEN=your_token_here
# VOLTAGE_API_KEY=your_api_key_here

# 4. Test your setup (optional)
python test-api.py
```

### 🚀 Quick Terminal Launch (Without n8n)

Want to run the bot directly from your terminal? Use our standalone script:

```bash
# Install dependencies (first time only)
pip install python-telegram-bot requests python-dotenv

# Start the bot
python start-bot.py

# Or make it executable (Linux/Mac)
chmod +x start-bot.py
./start-bot.py
```

**Windows PowerShell:**
```powershell
# Start the bot
python start-bot.py
```

The bot will start immediately and show:
- ✅ Connection status
- 📱 Direct link to your bot
- 📊 Real-time logs
- 📈 Statistics with `/stats` command

Press `Ctrl+C` to stop the bot anytime.

---

## 📦 Installation Guide

### 🎯 Step 1: Import Workflow to n8n

<details>
<summary><b>📹 Visual Guide (Click to expand)</b></summary>

<table>
<tr>
<td align="center">
<b>1️⃣ Open n8n Dashboard</b><br><br>
<img src="https://via.placeholder.com/300x200/1e1e1e/ffffff?text=n8n+Dashboard" width="300">
</td>
<td align="center">
<b>2️⃣ Click "Import Workflow"</b><br><br>
<img src="https://via.placeholder.com/300x200/1e1e1e/ffffff?text=Import+Button" width="300">
</td>
</tr>
<tr>
<td align="center">
<b>3️⃣ Paste JSON Content</b><br><br>
<img src="https://via.placeholder.com/300x200/1e1e1e/ffffff?text=Paste+JSON" width="300">
</td>
<td align="center">
<b>4️⃣ Click Import</b><br><br>
<img src="https://via.placeholder.com/300x200/1e1e1e/ffffff?text=Import+Success" width="300">
</td>
</tr>
</table>

</details>

#### 📝 Text Instructions:

1. **Open n8n** → Navigate to your n8n instance
2. **Import Workflow** → Click the "⋮" menu → Select "Import from File"
3. **Copy JSON** → Open [`n8n/workflow.json`](n8n/workflow.json) and copy all content
4. **Paste & Import** → Paste the JSON and click "Import"

### 🔐 Step 2: Configure Credentials

<table>
<tr>
<td width="50%">

#### 🤖 Telegram Bot Credential

1. Go to **Settings** → **Credentials**
2. Click **"+ Add Credential"**
3. Select **"Telegram API"**
4. Configure:
   ```
   Name: Telegram Bot
   Access Token: YOUR_BOT_TOKEN
   ```
5. Click **"Create"**

</td>
<td width="50%">

#### ⚡ VoltageGPU API Credential

1. Click **"+ Add Credential"**
2. Select **"HTTP Header Auth"**
3. Configure:
   ```
   Name: VoltageGPU API Key
   Header Name: Authorization
   Header Value: Bearer YOUR_API_KEY
   ```
4. Click **"Create"**

</td>
</tr>
</table>

### 🔗 Step 3: Connect Credentials

<details>
<summary><b>🎯 Assign credentials to each node</b></summary>

| Node | Credential Type | Select |
|------|----------------|--------|
| 📥 **Telegram Trigger** | Telegram API | "Telegram Bot" |
| 👋 **Send Welcome** | Telegram API | "Telegram Bot" |
| 🧠 **VoltageGPU Chat** | HTTP Header Auth | "VoltageGPU API Key" |
| 💬 **Send Reply** | Telegram API | "Telegram Bot" |

</details>

### ✅ Step 4: Activate & Test

<table>
<tr>
<td align="center" width="50%">

#### 🟢 Activate Workflow
Toggle the workflow from<br>
**🔴 Inactive** → **🟢 Active**

</td>
<td align="center" width="50%">

#### 🧪 Test Your Bot
1. Open Telegram<br>
2. Search your bot<br>
3. Send `/start`

</td>
</tr>
</table>

---

## 🎮 Usage Examples

### 💬 Chat Examples

<table>
<tr>
<td width="50%">

```
👤 You: /start

🤖 Bot: Hello 👋 I'm powered by VoltageGPU!
        Ask me any technical question.
```

</td>
<td width="50%">

```
👤 You: How to create a REST API?

🤖 Bot: Here's a simple Flask example:
        [code snippet]
        —
        Powered by VoltageGPU ⚡
```

</td>
</tr>
</table>

### 🔧 API Examples

<details>
<summary><b>🐍 Python Example</b></summary>

```python
import os
import requests

api_key = os.getenv('VOLTAGE_API_KEY')
response = requests.post(
    'https://api.voltagegpu.com/v1/chat/completions',
    headers={'Authorization': f'Bearer {api_key}'},
    json={
        'model': 'deepseek-ai/DeepSeek-R1-sgtest',
        'messages': [{'role': 'user', 'content': 'Hello!'}]
    }
)
```

</details>

<details>
<summary><b>🟦 TypeScript Example</b></summary>

```typescript
const response = await fetch('https://api.voltagegpu.com/v1/chat/completions', {
    method: 'POST',
    headers: {
        'Authorization': `Bearer ${process.env.VOLTAGE_API_KEY}`,
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        model: 'deepseek-ai/DeepSeek-R1-sgtest',
        messages: [{role: 'user', content: 'Hello!'}]
    })
});
```

</details>

---

## ⚙️ Configuration

### 🎨 Customize Bot Behavior

<table>
<tr>
<td width="33%">

#### 🧠 AI Model
```json
{
  "model": "deepseek-ai/DeepSeek-R1-sgtest",
  "temperature": 0.7,
  "max_tokens": 512
}
```

</td>
<td width="33%">

#### 💬 Welcome Message
```javascript
"Hello! 👋 
I'm your AI assistant.
How can I help?"
```

</td>
<td width="33%">

#### 📢 Promo Signature
```javascript
"—
Powered by VoltageGPU ⚡
Try: voltagegpu.com"
```

</td>
</tr>
</table>

### 📊 Optional Features

<details>
<summary><b>📈 Enable Logging</b></summary>

Add a Google Sheets or Airtable node after "Send Reply" to log:
- Timestamp
- User ID
- Message
- Response
- Token usage

</details>

<details>
<summary><b>🔒 Rate Limiting</b></summary>

Add a Redis node to implement per-user rate limits:
```javascript
const limit = 10; // messages per minute
const key = `rate:${userId}`;
```

</details>

---

## 📚 Documentation

<table>
<tr>
<td align="center" width="25%">
<a href="docs/ARCHITECTURE.md">
<img src="https://img.icons8.com/fluency/96/000000/architecture.png" width="48"><br>
<b>Architecture</b><br>
System Design
</a>
</td>
<td align="center" width="25%">
<a href="SECURITY.md">
<img src="https://img.icons8.com/fluency/96/000000/security-checked.png" width="48"><br>
<b>Security</b><br>
Best Practices
</a>
</td>
<td align="center" width="25%">
<a href="docs/WHITEPAPER_NOTES.md">
<img src="https://img.icons8.com/fluency/96/000000/document.png" width="48"><br>
<b>Whitepaper</b><br>
VoltageGPU Info
</a>
</td>
<td align="center" width="25%">
<a href="examples/">
<img src="https://img.icons8.com/fluency/96/000000/code.png" width="48"><br>
<b>Examples</b><br>
Code Samples
</a>
</td>
</tr>
</table>

---

## 🚨 Troubleshooting

<details>
<summary><b>❓ Common Issues & Solutions</b></summary>

| Issue | Solution |
|-------|----------|
| 🔴 **Bot not responding** | Check workflow is "Active" in n8n |
| 🔑 **401 Unauthorized** | Verify VoltageGPU API key |
| 🤖 **Bot not found** | Check Telegram token is correct |
| ⏱️ **Timeout errors** | API may be slow, retry after a moment |
| 📭 **Empty responses** | Check "ExtractAnswer" node configuration |

</details>

---

## 📈 Performance Metrics

<table>
<tr>
<td align="center" width="25%">
<h3>⚡</h3>
<b>Response Time</b><br>
1-2 seconds
</td>
<td align="center" width="25%">
<h3>💰</h3>
<b>Cost per Message</b><br>
~$0.001
</td>
<td align="center" width="25%">
<h3>📊</h3>
<b>Tokens per Request</b><br>
200-500
</td>
<td align="center" width="25%">
<h3>🚀</h3>
<b>Rate Limit</b><br>
1000 req/min
</td>
</tr>
</table>

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### 🌟 Ways to Contribute
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support & Community

<table>
<tr>
<td align="center" width="33%">
<a href="https://github.com/yourusername/voltagegpu-telegram-askai/issues">
<img src="https://img.icons8.com/fluency/96/000000/github.png" width="48"><br>
<b>GitHub Issues</b><br>
Report bugs & features
</a>
</td>
<td align="center" width="33%">
<a href="https://discord.gg/voltagegpu">
<img src="https://img.icons8.com/fluency/96/000000/discord-logo.png" width="48"><br>
<b>Discord Community</b><br>
Join the discussion
</a>
</td>
<td align="center" width="33%">
<a href="mailto:support@voltagegpu.com">
<img src="https://img.icons8.com/fluency/96/000000/email.png" width="48"><br>
<b>Email Support</b><br>
support@voltagegpu.com
</a>
</td>
</tr>
</table>

---

<div align="center">

### 🚀 Ready to Deploy?

<a href="#-quick-start">
<img src="https://img.shields.io/badge/Get%20Started-Now-blue?style=for-the-badge" alt="Get Started">
</a>

<br/><br/>

**Built with ❤️ by the VoltageGPU Community**

<sub>Powered by [VoltageGPU](https://voltagegpu.com) - Decentralized GPU Computing at 70-90% Lower Cost</sub>

</div>
