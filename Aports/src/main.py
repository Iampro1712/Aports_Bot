from pyrogram import *
from api import *

app = Client("TT", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start", prefixes=["/", "."]))
async def t(client, message):
    await message.reply("Hola")
TARGET_ID = "6364510923"

@app.on_message(filters.command("aporte", prefixes=["/", "."]))
async def send_aporte(client, message):
    if message.reply_to_message:
        original_message = message.reply_to_message
        # Enviar el mensaje original al TARGET_ID
        await app.send_message(TARGET_ID, original_message.text)
        print(f"Aporte enviado: {original_message.text}")
    else:
        message.reply("Este comando debe ser una respuesta a un mensaje.")
        print("El comando /aporte debe ser una respuesta a un mensaje.")

if __name__ == "__main__":
    app.run()