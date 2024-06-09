import os,discord
from dotenv import load_dotenv

load_dotenv()

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'"{os.environ["ROLE_NAME"]}" のロール一覧')
    guild = bot.guilds[0]  # 最初のサーバー（ギルド）を対象とする
    role = discord.utils.get(guild.roles, name=os.environ['ROLE_NAME'])

    if role:
        members_with_role = [member for member in guild.members if role in member.roles]
        for member in members_with_role:
            # discord ユーザ名の表示
            print(f'{member.name}')
    else:
        print(f'Role "{os.environ["ROLE_NAME"]}" not found')

    await bot.close()

bot.run(os.environ['TOKEN'])
