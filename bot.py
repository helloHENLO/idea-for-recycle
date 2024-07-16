import discord
from sifreOlusturucu import sifreOlusturucu
from sifreOlusturucu import tokenn
from yaziTura import yaziTura


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$sifre'):
        await message.channel.send(sifreOlusturucu(10))
    elif message.content.startswith('$yazi_mi_tura_mi'):
        await message.channel.send(yaziTura(1))
    else:
        await message.channel.send("im admin rn")

client.run(tokenn)