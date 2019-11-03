from jobs import Job


class Player:
    name: str = 'none'
    faction: str = 'none'
    job: Job = 'none'
    isKilled: bool = False

    # constructor
    def __init__(self, name):
        self.name = name

    def set_faction(self, faction):
        self.faction = faction

    def set_job(self, job: Job):
        self.job = job



