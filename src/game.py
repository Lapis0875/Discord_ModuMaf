from discord import User
from player import Player
from jobs import *


class Game:
    # game variables
    guildname = ''
    players: list = []
    time: int = 0
    job_classic_dict = {'시민팀' : [Citizen, Police, Doctor], '마피아팀' : [Mafia, Spy], '교주팀' : []}
    on_game: bool = False

    def __init__(self, guildname: str):
        self.guildname = guildname
        self.players: list = []
        self.time: int = 0
        self.on_game: bool = False
        print('[game.py] Game object initialized.')

    def player_join(self, user: User):
        player = Player(user.name)
        self.players.append(player)

    def setup(self, mode: str):
        # 플레이어들에게 배정할 직업 리스트
        job_list = []
        # 모드에 따라 job_list 설정
        if mode == '클래식':
            for key in self.job_dict:
                for job in self.job_dict[key]:
                    job_list.append(job)
        elif mode == '확장':
            for key in self.job_dict:
                for job in self.job_dict[key]:
                    job_list.append(job)
        elif mode == '크레이지':
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

