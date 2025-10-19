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
            "👋 Bonjour! Je suis votre assistant IA personnel.\n\n"
            "Je peux vous aider avec:\n"
            "📚 Questions générales et recherches\n"
            "💻 Programmation et développement\n"
            "✍️ Rédaction et créativité\n"
            "🔧 Conseils techniques\n"
            "📊 Analyse et calculs\n"
            "🌍 Traductions\n\n"
            "Posez-moi n'importe quelle question!"
        )
        await update.message.reply_text(welcome_message)
        logger.info(f"Start command from user {update.effective_user.id}")
    
    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /stats command"""
        uptime = datetime.now() - self.stats['start_time']
        stats_message = (
            f"📊 Statistiques du Bot\n"
            f"━━━━━━━━━━━━━━━\n"
            f"✉️ Messages traités: {self.stats['messages_processed']}\n"
            f"⏱️ Temps de fonctionnement: {str(uptime).split('.')[0]}\n"
            f"✅ Taux de réussite: {100 - (self.stats['errors'] / max(1, self.stats['messages_processed']) * 100):.1f}%"
        )
        await update.message.reply_text(stats_message)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_message = (
            "🤖 **Comment utiliser ce bot?**\n\n"
            "Envoyez-moi simplement votre question!\n\n"
            "**Exemples d'utilisation:**\n"
            "• 📝 Rédiger un email professionnel\n"
            "• 💡 Expliquer un concept complexe\n"
            "• 🐍 Écrire du code Python\n"
            "• 🍳 Trouver une recette de cuisine\n"
            "• 📈 Analyser des données\n"
            "• 🎯 Résoudre un problème\n"
            "• 🌐 Traduire un texte\n\n"
            "**Commandes disponibles:**\n"
            "/start - Message de bienvenue\n"
            "/help - Cette aide\n"
            "/stats - Statistiques du bot\n"
            "/clear - Effacer l'historique"
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
            
            # Send response (no promotional signature for better user experience)
            await update.message.reply_text(response)
            self.stats['messages_processed'] += 1
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            self.stats['errors'] += 1
            
            error_message = (
                "😔 Désolé, une erreur s'est produite.\n"
                "Veuillez réessayer dans quelques instants."
            )
            await update.message.reply_text(error_message)
    
    async def call_voltage_api(self, message: str) -> str:
        """Call VoltageGPU API"""
        headers = {
            "Authorization": f"Bearer {VOLTAGE_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "deepseek-ai/DeepSeek-R1-sgtest",
            "stream": False,
            "max_tokens": 512,
            "temperature": 0.7,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Tu es un assistant IA polyvalent, intelligent et serviable. "
                        "Tu réponds en français par défaut, sauf si l'utilisateur écrit dans une autre langue. "
                        "Sois concis mais complet. Utilise des emojis pour rendre les réponses plus agréables. "
                        "Tu peux aider avec: questions générales, programmation, rédaction, traduction, "
                        "conseils, analyse, créativité, et bien plus. Adapte ton ton selon le contexte."
                    )
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        }
        
        # Make async request
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: requests.post(VOLTAGE_API_URL, headers=headers, json=payload, timeout=30)
        )
        
        if response.status_code == 200:
            data = response.json()
            content = data.get('choices', [{}])[0].get('message', {}).get('content', '')
            return content or "Désolé, aucune réponse reçue."
        else:
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
