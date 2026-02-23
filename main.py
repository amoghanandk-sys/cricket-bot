import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🎯 Catch Drop", callback_data="catch")],
        [InlineKeyboardButton("💥 Last Ball Six", callback_data="six")],
        [InlineKeyboardButton("⚡ 2 Wickets Spell", callback_data="wickets")],
        [InlineKeyboardButton("🎲 51 Ball Theory", callback_data="ball51")]
    ]

    await update.message.reply_text(
        "✅ Auto Alert System Active\nSelect trigger:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    signals = {
        "catch": "🚨 CHASE SIGNAL\nCatch dropped early\n👉 Support chasing team",
        "six": "💥 JACKPOT THEORY\nLast ball six\n👉 Opportunity time",
        "wickets": "⚡ MOMENTUM SHIFT\n2 wickets spell\n👉 Market volatility",
        "ball51": "🎲 51 BALL THEORY\nPattern zone\n👉 Watch closely"
    }

    await query.message.reply_text(signals.get(query.data, "Signal detected"))


app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
