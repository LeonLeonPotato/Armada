class Character:
    def __init__(self, fullname: str, rarity: int, maxlevel: int, maxpromotion: int, skills: dict) -> None:
        self.fullname : str = fullname
        self.rarity : int = rarity
        self.maxlevel : int = maxlevel
        self.maxpromotion : int = maxpromotion
        self.skills : dict = skills

        self.id : int = int(fullname.split("_")[1])
        self.name : str = fullname.split("_")[2]

        self.modules = []

    def __str__(self) -> str:
        return self.fullname

    def skillCount(self):
        if(self.fullname == "char_002_amiya"):
            return 3

        match self.rarity:
            case 1 | 2:
                return 0
            case 3:
                return 1
            case 4 | 5:
                return 2
            case 6:
                return 3
            case _:
                return 0