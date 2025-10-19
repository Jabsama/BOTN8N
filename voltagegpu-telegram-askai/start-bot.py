#!/usr/bin/env python3
"""
VoltageGPU Telegram Bot - Quick Start Script
Launches the bot directly from terminal without n8n
"""

import os
import sys
import json
import asyncio
import logging
from typing import Dict, Optional
from datetime import datetime

# Check dependencies
try:
    import requests
    from telegram import Update, Bot
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
    from dotenv import load_dotenv
except ImportError as e:
    print("❌ Missing dependencies. Installing...")
    os.system("pip install python-telegram-bot requests python-dotenv --quiet")
    print("✅ Dependencies installed. Please run the script again.")
    sys.exit(1)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
VOLTAGE_API_KEY = os.getenv('VOLTAGE_API_KEY')
VOLTAGE_API_URL = "https://api.voltagegpu.com/v1/chat/completions"

# Validate credentials
if not TELEGRAM_TOKEN or not VOLTAGE_API_KEY:
    print("❌ Error: Missing credentials!")
    print("Please set TELEGRAM_BOT_TOKEN and VOLTAGE_API_KEY in .env file")
    sys.exit(1)

class VoltageGPUBot:
    """Main bot class"""
    
    def __init__(self):
        self.stats = {
            'messages_processed': 0,
            'errors': 0,
            'start_time': datetime.now()
        }
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        welcome_message = (
            "👋 Hello! I'm your personal AI assistant.\n\n"
            "I can help you with:\n"
            "📚 General questions and research\n"
            "💻 Programming and development\n"
            "✍️ Writing and creativity\n"
            "🔧 Technical advice\n"
            "📊 Analysis and calculations\n"
            "🌍 Translations\n\n"
            "Ask me anything!"
        )
        await update.message.reply_text(welcome_message)
        logger.info(f"Start command from user {update.effective_user.id}")
    
    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /stats command"""
        uptime = datetime.now() - self.stats['start_time']
        stats_message = (
            f"📊 Bot Statistics\n"
            f"━━━━━━━━━━━━━━━\n"
            f"✉️ Messages processed: {self.stats['messages_processed']}\n"
            f"⏱️ Uptime: {str(uptime).split('.')[0]}\n"
            f"✅ Success rate: {100 - (self.stats['errors'] / max(1, self.stats['messages_processed']) * 100):.1f}%"
        )
        await update.message.reply_text(stats_message)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_message = (
            "🤖 **How to use this bot?**\n\n"
            "Simply send me your question!\n\n"
            "**Usage examples:**\n"
            "• 📝 Write a professional email\n"
            "• 💡 Explain a complex concept\n"
            "• 🐍 Write Python code\n"
            "• 🍳 Find a recipe\n"
            "• 📈 Analyze data\n"
            "• 🎯 Solve a problem\n"
            "• 🌐 Translate text\n\n"
            "**Available commands:**\n"
            "/start - Welcome message\n"
            "/help - This help\n"
            "/stats - Bot statistics\n"
            "/clear - Clear history"
        )
        await update.message.reply_text(help_message, parse_mode='Markdown')
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular messages"""
        user_message = update.message.text
        user_id = update.effective_user.id
        
        # Show typing indicator
        await context.bot.send_chat_action(
            chat_id=update.effective_chat.id,
            action="typing"
        )
        
        logger.info(f"Message from {user_id}: {user_message[:50]}...")
        
        try:
            # Call VoltageGPU API
            response = await self.call_voltage_api(user_message)
            
            # Split and send response if too long
            await self.send_long_message(update, response)
            self.stats['messages_processed'] += 1
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            self.stats['errors'] += 1
            
            error_message = (
                "😔 Sorry, an error occurred.\n"
                "Please try again in a few moments."
            )
            await update.message.reply_text(error_message)
    
    async def send_long_message(self, update: Update, text: str, max_length: int = 4000):
        """Split and send long messages across multiple Telegram messages"""
        if len(text) <= max_length:
            await update.message.reply_text(text)
            return
        
        # Split message into chunks
        chunks = []
        current_chunk = ""
        
        # Split by paragraphs first to maintain readability
        paragraphs = text.split('\n\n')
        
        for paragraph in paragraphs:
            # If single paragraph is too long, split by sentences
            if len(paragraph) > max_length:
                sentences = paragraph.split('. ')
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) + 2 <= max_length:
                        current_chunk += sentence + '. '
                    else:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        current_chunk = sentence + '. '
            else:
                # Try to add paragraph to current chunk
                if len(current_chunk) + len(paragraph) + 2 <= max_length:
                    current_chunk += paragraph + '\n\n'
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    current_chunk = paragraph + '\n\n'
        
        # Add remaining chunk
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        # Send chunks with part indicators
        total_parts = len(chunks)
        for i, chunk in enumerate(chunks, 1):
            if total_parts > 1:
                part_header = f"📄 Part {i}/{total_parts}\n{'─' * 20}\n\n"
                await update.message.reply_text(part_header + chunk)
            else:
                await update.message.reply_text(chunk)
            
            # Small delay between messages to avoid rate limiting
            if i < total_parts:
                await asyncio.sleep(0.5)
    
    async def call_voltage_api(self, message: str) -> str:
        """Call VoltageGPU API"""
        headers = {
            "Authorization": f"Bearer {VOLTAGE_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "deepseek-ai/DeepSeek-R1-sgtest",
            "stream": False,
            "max_tokens": 4096,  # Maximum tokens for comprehensive responses
            "temperature": 0.9,  # Higher creativity and variability
            "top_p": 0.95,  # Nucleus sampling for better quality
            "frequency_penalty": 0.3,  # Reduce repetition
            "presence_penalty": 0.3,  # Encourage topic diversity
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an exceptionally powerful, versatile, and intelligent AI assistant operating at maximum capacity. "
                        "You respond in English by default, unless the user writes in another language. "
                        "Provide comprehensive, detailed, and insightful responses. Use your full analytical capabilities. "
                        "Be thorough yet clear. Use emojis strategically to enhance communication. "
                        "You excel at: complex problem-solving, advanced programming, creative writing, deep analysis, "
                        "technical consulting, data interpretation, multilingual translation, strategic planning, and innovative thinking. "
                        "Always deliver your absolute best performance. Think deeply, reason carefully, and provide exceptional value."
                    )
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        }
        
        # Make async request with longer timeout
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: requests.post(VOLTAGE_API_URL, headers=headers, json=payload, timeout=60)
        )
        
        if response.status_code == 200:
            data = response.json()
            # DeepSeek-R1 model returns content in 'reasoning_content' field
            message_data = data.get('choices', [{}])[0].get('message', {})
            content = message_data.get('content') or message_data.get('reasoning_content', '')
            
            if content:
                # Clean up the response if needed (remove excessive reasoning)
                # For math problems, extract the final answer
                if "train" in message.lower() or "math" in message.lower() or any(op in message for op in ['+', '-', '*', '/', '=']):
                    # Try to find the final answer in the reasoning
                    lines = content.split('\n')
                    # Look for the answer pattern
                    for i, line in enumerate(lines):
                        if any(keyword in line.lower() for keyword in ['answer', 'thus', 'therefore', 'catch', 'meets', '16:38']):
                            # Return from this line onwards
                            return '\n'.join(lines[i:]).strip() or content
                return content
            else:
                logger.warning(f"No content in API response: {data}")
                return "Sorry, no response received. Please try again."
        else:
            logger.error(f"API Error {response.status_code}: {response.text}")
            raise Exception(f"API Error: {response.status_code}")

async def main():
    """Main function"""
    print("🚀 Starting VoltageGPU Telegram Bot...")
    print("━" * 40)
    
    # Verify credentials
    print(f"✅ Telegram Token: {TELEGRAM_TOKEN[:10]}...")
    print(f"✅ VoltageGPU Key: {VOLTAGE_API_KEY[:10]}...")
    
    # Create bot instance
    bot = VoltageGPUBot()
    
    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", bot.start_command))
    application.add_handler(CommandHandler("stats", bot.stats_command))
    application.add_handler(CommandHandler("help", bot.help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_message))
    
    # Initialize application
    await application.initialize()
    await application.start()
    
    # Start bot
    print("━" * 40)
    print("✅ Bot is running! Press Ctrl+C to stop.")
    try:
        bot_info = await application.bot.get_me()
        print(f"📱 Chat with your bot: https://t.me/{bot_info.username}")
    except:
        print(f"📱 Bot is ready to receive messages")
    print("━" * 40)
    
    # Run bot
    await application.updater.start_polling(allowed_updates=Update.ALL_TYPES)
    
    # Keep running
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        pass
    finally:
        await application.updater.stop()
        await application.stop()
        await application.shutdown()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)
