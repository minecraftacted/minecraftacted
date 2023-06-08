import discord

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True
token = "MTExNjI5MzI5MDU3NzM3NTI1Mw.GMQeGn.VMrH1SauNiR3V2ysrFRSPNVOWyEOh-fDvEBScg"

# クライアントの生成
client = discord.Client(intents=intents)
announce_channel = 1098025440997814313
rule_channel = 1098024296200290395

# discordと接続した時に呼ばれる
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game('お仕事中...  ( ..)φ'))
    print(f'We have logged in as {client.user}')

# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
    # 自分のメッセージを無効
    if message.author == client.user:
        return

    # メッセージが"$hello"で始まっていたら"Hello!"と応答
    if message.content.startswith('$hello'):
        await message.channel.send('こんちくわ🥓←これはベーコン')
    if message.channel.id == rule_channel:
        messages = [channel_message async for channel_message in message.channel.history(limit=2,oldest_first=True)]
        await client.get_channel(announce_channel).send("(*'▽')RCAがルールの変更をお知らせします\n[[改正前]]\n\n"+messages[0].content+"\n\n\n\n\n\n\n[[改正後]]\n\n"+messages[1].content+"\n\nご一読お願いします!!!!!")
        await messages[0].delete()

# クライアントの実行
client.run(token)