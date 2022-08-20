from email.policy import default


class Character:
    def __init__(self, fullname: str, rarity: int, maxlevel: int, maxpromotion: int) -> None:
        self.fullname : str = fullname
        self.rarity : int = rarity
        self.maxlevel : int = maxlevel
        self.maxpromotion : int = maxpromotion

        self.id : int = int(fullname.split("_")[1])
        self.name : str = fullname.split("_")[2]

    def __str__(self) -> str:
        return self.fullname

    