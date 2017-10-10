import json
#Se declaran las variables
game = {}
pongZone = []
score_p1 = 5
score_p2 = 0
gameRound = 0
balls = 3
ballPosition = 0
gamerecord = []
activePost = ""
activeGet = ""
playerPaddle = ""

game['pongZone'] = pongZone
game['score_p1'] = score_p1
game['score_p2'] = score_p2
game['gameRound'] = gameRound
game['balls'] = balls
game['ballPosition'] = ballPosition
game['activeGet'] = activeGet
game['activePost'] = activePost

for x in range(2):
    pongZone.append(["0"] * 11)

toJson = json.dumps(game)
loaded = json.loads(toJson)

test= loaded['score_p1'] + 2

print(test)