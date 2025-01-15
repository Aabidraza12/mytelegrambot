import telebot
import qrcode
from io import BytesIO

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = '7656734388:AAEa479uuROaDPQypjqah-WO7cM9gikS9Nc'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(
        message, 
        "Welcome to the QR  Bot! 🎉\nSend me any text, and I'll generate a QR code for you!"
    )

@bot.message_handler(func=lambda message: True)
def generate_qr(message):
    text = message.text
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    bio = BytesIO()
    bio.name = 'qr.png'
    img.save(bio, 'PNG')
    bio.seek(0)

    # Send the image back to the user
    bot.send_photo(message.chat.id, photo=bio, caption="Here's your QR code!")

# Start the bot
print("Bot is running...")
bot.infinity_polling()
