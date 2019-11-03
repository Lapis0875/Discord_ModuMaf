from discord import User
from player import Player
from jobs import *


class Game:
    # game variables
    guildname = ''
    gamemode = ''
    players: list = []
    time: int = 0
    job_Classic_dict = {'시민팀' : [Citizen, Police, Doctor], '마피아팀' : [Mafia], '교주팀' : []}
    job_Extended_dict = {'시민팀' : [], '마피아팀' : [Spy], '교주팀' : []}
    is_setuped: bool = False
    on_game: bool = False

    # info variables
    info = "디스코드에서 채팅만으로 즐길 수 있는 마피아 게임! 모두의 마피아입니다."
    modes = '클래식 , 확장 , 크레이지 '

    def __init__(self, guildname: str, gamemode: str):
        self.guildname = guildname
        self.gamemode = gamemode
        self.players: list = []
        self.time: int = 0
        self.on_game: bool = False
        print('[game.py] Game object initialized.')

    def player_join(self, user: User):
        player = Player(user.name)
        self.players.append(player)

    def setup(self):
        # 플레이어들에게 배정할 직업 리스트
        job_list = []
        # 모드에 따라 job_list 설정
        if self.gamemode == '클래식':
            for key in self.job_dict:
                for job in self.job_dict[key]:
                    job_list.append(job)
        elif self.gamemode == '확장':
            for key in self.job_dict:
                for job in self.job_dict[key]:
                    job_list.append(job)
        elif self.gamemode == '크레이지':
            for key in self.job_dict:
                for job in self.job_dict[key]:
                    job_list.append(job)
        else:
            return False
        
        print(job_list)         # 디버그

        for player in self.players:
            from random import randrange
            player.job = job_list[randrange(0,len(job_list))]
            job_list.remove(player.job)


    def start(self):
        if self.is_setuped is True:
            print('Starting Game')
        else:
            return False



