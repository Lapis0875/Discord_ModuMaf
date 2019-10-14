class Player:
    name: str = 'none'
    faction: str = 'none'
    job = 'none'
    isKilled: bool = False

    # constructor
    def __init__(self, name):
        self.name = name

    def set_faction(self, faction):
        self.faction = faction

    def set_job(self, job):
        self.job = job



