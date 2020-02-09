import json


class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year


tournaments = {"Aeroflot Open": 2010,
               "FIDE World Cup": 2018,
               "FIDE Grand Prix": 2016
               }

json_data = json.dumps(tournaments, indent=2)  # serialization
print(json_data)

loaded = json.loads(json_data)  # deserialization
print(type(loaded))
print(loaded)

t1 = Tournament("Aeroflot Open", 2010)
json_data = json.dumps(t1.__dict__)
print(json_data)
t = Tournament(**json.loads(json_data))
print(f'name = {t.name}, year = {t.year}')


class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments


t1 = Tournament("Aeroflot Open", 2010)
t2 = Tournament("FIDE World Cup", 2018)
t3 = Tournament("FIDE Grand Prix", 2016)
p1 = ChessPlayer([t1, t2, t3])

# default parameter uses if json.dumps can't serialize data.
# (default=lambda obj: obj.__dict__) will return p1.__dict__, t1.__dict__, t2.__dict__, t3.__dict__
json_data = json.dumps(p1, default=lambda obj: obj.__dict__)
print(json_data)

decode_player = ChessPlayer(**json.loads(json_data))
print(decode_player)
player_tournament = decode_player.tournaments[0]
print(type(player_tournament))  # <class 'dict'> but must be type Tournament
print(player_tournament)
print('----------------------------')


class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)


class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournaments = list(map(Tournament.from_json, json_data['tournaments']))
        return cls(tournaments)


t1 = Tournament("Aeroflot Open", 2010)
t2 = Tournament("FIDE World Cup", 2018)
t3 = Tournament("FIDE Grand Prix", 2016)
p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1, default=lambda obj: obj.__dict__, indent=4, sort_keys=True)
print(type(json_data))
print(json_data)

decode_player = ChessPlayer.from_json(json.loads(json_data))
print(decode_player)
print(decode_player.tournaments)

with open('player.json', 'w') as file:
    json.dump(p1, file, default=lambda obj: obj.__dict__)

with open('player.json', 'r') as read_file:
    data = json.load(read_file)

print('----------------------------------------')
print(data)
print('----------------------------------------')

decode_player = ChessPlayer.from_json(data)
print(decode_player)
print(decode_player.tournaments)



