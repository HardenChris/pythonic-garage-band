
class Band:

    members_count = 0

    band_count = 0

    def __init__(self, name="unknown"):
        self.name = name
        Band.band_count +=1

    def __init__(self, members="unknown"):
        self.members = members
        Band.members_count += 1

    @classmethod
    def get_members_count(cls):
        return cls.members_count

    @classmethod
    def get_band_count(cls):
        return cls.band_count

    def play_solos(self):
        return
class Musician(Band):
    def __init__(self, name="unknown"):
        self.name = name

    def play_solo(self):
        return "playing solo"
class Guitarist(Musican):
    def get_instruments(self): 
        return f"{name} has their Guitar"

class Bassist(Musician):
    def get_instruments(self):
        return f"{name} has their Bass Guitar"

class Drummer(Musician):
    def get_instruments(self):
        return f"{name} has their Drums"
