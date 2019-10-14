from player import Player


class Job:
    job_name: str = ''
    ability_info: str = ''
    faction: str = ''
    isAbilityUsed: bool = False
    isReligious: bool = False

    def use_ability(self, user: Player, target: Player):
        return f'{user.name} used a ability to {target.name}'



class Citizen(Job):
    job_name: str = '시민'
    faction = '시민팀'
    ability_info: str = '시민팀에 속하는 능력없는 평범한 시민입니다.'

    def use_ability(self, user: Player, target: Player):
        return f'{user.name} used a ability to {target.name}'


class Police(Citizen):
    job_name: str = '경찰'
    ability_info: str = '시민팀에 속하는 경찰입니다. 매일 밤 플레이어들 중 한 명을 조사해 마피아편인지 아닌지 알아냅니다.'

    def use_ability(self, user: Player, target: Player):
        return f'{user.name}(경찰)이 {target.name}를 조사했습니다!'


class Doctor(Citizen):
    job_name: str = '의사'
    ability_info: str = '시민팀에 속하는 의사입니다. 매일 밤 플레이어들 중 한 명을 지정해 치료할 수 있습니다.'

    def use_ability(self, user: Player, target: Player):
        return f'{user.name}(의사)가 {target.name}를 치료했습니다!'


class Mafia(Job):
    job_name: str = '마피아'
    faction = '마피아팀'
    ability_info: str = '매일 밤 사람을 한 명 죽일 수 있습니다. 밤에 마피아팀 전용 채팅방에서 자신의 팀원과 대화할 수 있습니다.'

    def use_ability(self, user: Player, target: Player):
        return f'{user.name}(마피아)이 {target.name}를 살해했습니다!'



class Spy(Job):
    job_name: str = '스파이'
    faction = '마피아팀'
    ability_info: str = '밤마다 플레이어중 하나를 선택하여 그 사람의 직업을 알아낼 수 있다.'

    def use_ability(self, user: Player, target: Player):
        return f'{user.name}{target.name}'



