import discord, json
from discord.ext import commands

from game import Game


# 디스코드 봇의 토큰. 디스코드 개발자 패널의 모두의 마피아 봇 토큰. 혹여나 공개될시 반드시 리젠해서 보안 문제가 일어나지 않도록 하자.
token = "NjMxODQyMDM2NzMwOTUzNzM5.XZ8uzg.J7kXwUvvC-769N_XA3w0KK6L3jE"

# 디스코드 봇의 설명.
description = "디스코드에서 채팅만으로도 즐길 수 있도록 하기 위한 봇! \n" \
              "저는 디스코드용 마피아 미니게임 봇 '모두의 마피아' 봇이에요! \n" \
              "제 명령어 프리픽스는 모두맢 이에요!"

# 디스코드 봇이 저장하는 변수들.
guilds_dict = {}
guilds_games = {}

'''
디스코드 봇을 생성합니다.
@:arg
command_prefix="모두맢 "
프리픽스(명령어 앞에 붙이는 문자열을 칭함)를 "파랑아 "로 설정한다.
description=description
봇의 설명을 봇 생성과 함께 전달한다. 위에 설명을 저장해둔 description 변수를 description= 의 인자로 넘긴다.
'''

bot = commands.Bot(description=description, command_prefix='모두맢 ', owner_id=280855156608860160)

'''
[EveryoneMafia] - Event

개발 방법 :
@bot.event()
async def 이벤트명(필요한 인자들):
    ...구현할 내용
    await 넘길 인자들...
    
*사용중인 이벤트 설명
on_ready() : 봇이 실행될 때 실행되는 이벤트.
on_disconnect() : 봇과 디스코드 간의 연결이 끊어졌을 때 호출되는 이벤트.
on_guild_join(guild) : 봇이 서버(디스코드에서는 'guild'라는 개념으로 부름.)에 참여할 때 실행되는 이벤트.
on_guild_remove(guild) : 봇이 서버(위와 동일한 guild)에서 나갈때 실행되는 이벤트.

'''


@bot.event
async def on_ready():
    print("========================")
    print("모두의 마피아 봇을 시작합니다.")
    print("다음으로 로그인합니다 : ")
    print("봇 이름 :", bot.user.name)
    print("봇 id :", bot.user.id)
    print("봇 프리픽스 :", bot.command_prefix)
    print("개발자 id :", bot.owner_id)
    print("========================")

    for guild in bot.guilds:
        global guilds_dict, guilds_games
        print(f'{guild.name} : {guild.id}')
        # 소속된 길드 목록 업데이트
        guilds_dict.update({guild.name: guild.id})
        # 게임 객체 생성.
        guilds_games.update({guild.name : Game(guild.name)})

    print(f'현재 봇이 소속된 서버 : {guilds_dict}')


    # 봇이 플레이중인 게임을 설정할 수 있다. 아래의 "반갑습니다"를 수정하면 된다.
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name="모두가 즐거운 미니게임을 즐길 수 있는 세상을 만들자!", type=1))


# 봇과 디스코드 간의 연결이 끊어졌을 때 호출되는 이벤트.
@bot.event
async def on_disconnect():
    print("========================")
    print("모두의 마피아 봇을 종료합니다.")
    print("다음으로 로그인했습니다 : ")
    print("사용자명 :", bot.user.name)
    print("사용자 id :", bot.user.id)
    print("개발자 id :", bot.owner_id)
    print("========================")


# 봇이 서버(디스코드에서는 'guild'라는 개념으로 부름.)에 참여할 때 실행되는 이벤트.
@bot.event
async def on_guild_join(guild):
    guilds_dict.update({guild.name : guild.id})
    await None


# 봇이 서버(위와 동일한 guild)에서 나갈때 실행되는 이벤트.
@bot.event
async def on_guild_remove(guild):
    del guilds_dict[guild.name]
    await None


'''
@bot.event
async def on_message(message):
    print(f'{message.author} : {message.content}')
    if message.content == '모두맢 프리픽스설정':
        print(f'message.author = {message.author}')
        print(message.author.id)
        if message.author.id == lapis_discord_id:
            print(True)
'''

'''
[모두의 마피아봇 명령어] - ver 0.0.1 test

개발 방법 :
async def 명령어(ctx, 그 외 필요한 인자들):
    ...구현할 내용
    await 넘길 인자들...
    
*명령어가 사용된 채팅방에 메세지를 전송할 때에는, 
    ctx.send(전송할 메세지: str)
 을 이용한다.
 async def 메세지받기(ctx, msg)
    await ctx.send("이러한 메세지를 받았어요! : {0}".format(msg))
    혹은
    await ctx.send("이러한 메세지를 받았어요! :", msg)

디스코드 내 사용법 : 
모두맢 명령어


'''


# help 명령어(임시). 제대로 된 도움 명령어는 HelpCommand 클래스를 이용해 만든 후 봇 생성시 help_command= 인자로 넘겨주자.
@bot.command()
async def 도움말(ctx):
    help_embed = discord.Embed(
        title='모두의 마피아',
        description='사용할 수 있는 모든 파랑봇 명령어를 나열해둔 도움말입니다.',
        colour=discord.Colour.red(),
        _footer='도움 메세지는 아직 준비중입니다! | 현재 봇 버전 : v 0.1',
        _image="https://cdn.discordapp.com/avatars/541645954256863252/e5001111b6743f6f4fb68bbd29309fb4.png?size=1024",
        _thumbnail="https://cdn.discordapp.com/avatars/541645954256863252/e5001111b6743f6f4fb68bbd29309fb4.png?size=1024"
    )
    help_embed.set_author(name="모두의 마피아 봇 도움말",
                          icon_url="https://cdn.discordapp.com/avatars/541645954256863252/e5001111b6743f6f4fb68bbd29309fb4.png?size=1024")
    help_embed.add_field(name="모두의 마피아 게임 소개", value=Game.info, inline=False)
    help_embed.add_field(name="모드", value=Game.modes, inline=False)
    help_embed.add_field(name="직업", value='일반모드와 크레이지모드로 나뉨', inline=False)
    help_embed.add_field(name="일반모드 직업", value=None, inline=True)
    help_embed.add_field(name="크레이지모드 전용 직업", value=None, inline=True)

    await ctx.send(embed=help_embed)


'''
[ 모두의 마피아 게임 명령어 ]
게임설정 : 파티(플레이어 대기열)를 생성하고, 사용자가 지정한 모드로 게임을 준비합니다.
게임시작 : 준비된 게임을 시작합니다. 게임은 서버당 한개씩만 진행됩니다. (추후 능력이 되면 늘려보자)
'''


@bot.command()
async def 게임설정(ctx, mode: str):
    if mode == '클래식':
        print('[modumaf.bot][game] mode set classic')
        game = Game(guildname=ctx.guild.name, gamemode='클래식')
        guilds_games.update({ctx.guild.name : game})
        await ctx.send('클래식 모드로 설정했습니다.')

    elif mode == '확장':
        print('[modumaf.bot][game] mode set normal')
        game = Game(guildname=ctx.guild.name, gamemode='확장')
        guilds_games.update({ctx.guild.name : game})
        await ctx.send('확장 모드로 설정했습니다.')

    elif mode == '크레이지':
        print('[modumaf.bot][game] mode set crazy')
        game = Game(guildname=ctx.guild.name, gamemode='크레이지')
        guilds_games.update({ctx.guild.name : game})
        await ctx.send('크레이지 모드로 설정했습니다.')
    else:
        print('[modumaf.bot][game] unknown request : unknown mode. ')
        await ctx.send('잘못된 모드를 입력하셨습니다.')

# 디스코드 임베드 메세지 테스트
@bot.command()
async def 개발자(ctx):
    my_embed = discord.Embed(
        title='개발자 소개',
        description='라피스 1인개발',
        colour=discord.Colour.blue()
    )

    my_embed.set_footer(text='현재 봇 버전 :v 0.1')
    my_embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/280855156608860160/f40d49e61106594f5b7f7c1eabb145c8.png?size=1024")
    my_embed.set_author(name="라피스 (봇 개발자)",
                        icon_url="https://cdn.discordapp.com/avatars/280855156608860160/f40d49e61106594f5b7f7c1eabb145c8.png?size=1024")
    my_embed.add_field(name="사용 언어", value="Python, Java, C#(야매)", inline=True)
    my_embed.add_field(name="특징", value="고1, 학업과 병행하며 개발중(힘들어요 ㅠㅠ)", inline=True)
    my_embed.add_field(name="지망하는 대학과 학부", value="한양대 컴퓨터소프트웨어학부\n 정보 주시면 감사하겠습니다!", inline=True)
    await ctx.send(embed=my_embed)


@bot.command()
async def 소개(ctx):
    await ctx.send(bot.description)


@bot.command()
async def 핑(ctx):
    await ctx.send(f'퐁! ({round(bot.latency * 1000, 2)} ms)')


# 봇 실행
bot.run(token)
