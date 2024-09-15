import discord
import json

# Discord botunun doğru çalışması için intents belirliyoruz
intents = discord.Intents.default()
intents.message_content = True  # Mesajları dinleyebilmek için
client = discord.Client(intents=intents)

# Soruları ve cevapları JSON dosyasından yüklüyoruz
with open('sorular_ve_cevaplar.json', 'r', encoding='utf-8') as f:
    sorular_ve_cevaplar = json.load(f)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı!')

# Kullanıcı mesajlarını dinleyen event
@client.event
async def on_message(message):
    # Botun kendi mesajlarına cevap vermemesi için
    if message.author == client.user:
        return

    # Kullanıcı 'merhaba' yazdığında tetiklenen yanıt
    if message.content.lower() == 'merhaba':
        await message.channel.send("Merhaba! Çevre kirliliği ve iklim değişikliği hakkında sorular sorabilirsin.")

    # JSON dosyasındaki sorulara göre kullanıcıya yanıt verme
    for soru, cevap in sorular_ve_cevaplar.items():
        if soru.lower() in message.content.lower():
            await message.channel.send(cevap)
            break

# Bot tokenını buraya ekleyin
client.run('DC BOT TOKEN')
