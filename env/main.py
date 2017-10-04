from flask import Flask,jsonify, request,json
from random import randint

app = Flask(__name__)


#Se declaran las variables
game =[]
pongZone = []
score_p1 = 0
score_p2 = 0
gameRound = 1
balls = 3
origin = 0
gamerecord = []


for x in range(2):
    pongZone.append(["0"] * 11)

game.append(pongZone)
game.append(score_p1)
game.append(score_p2)
game.append(gameRound)
game.append(balls)
game.append(origin)


def show_gamezone(zone):
    for row in zone:
        print(" ".join(row))

@app.route('/getGame', methods = ['GET'])
def index():
    return jsonify(
        pongZone=game[0],
        score_p1=game[1],
        score_p2=game[2],
        gameRound=game[3],
        balls=game[4]
    )


@app.route('/move', methods = ['POST'])
def movement():

    playerID = request.form["id"]

    playermove = randint(0,10)
    if playerID == 1:
        game[0][1][playermove] = "X"

    else:
        game[0][0][playermove] = "X"
    gamerecord.append(game)
    origin = playermove
    return jsonify(
        pongZone=game[0]
    )

@app.route('/getEnemyMove/<int:player>', methods = ['GET'])
def getenemymove(player):

    if player == 1:
        playerpaddle = randint(0, 10)
        if playerpaddle == origin:
            game[0][0][origin] = "0"
            newOrigin = randint(0, 10)
            origin = newOrigin
            game[0][1][newOrigin] = "X"
        else:
            game[2] =+ 1

    elif player == 2:
        playerpaddle = randint(0, 10)
        if playerpaddle == origin:
            game[0][1][origin] = "0"
            newOrigin = randint(0, 10)
            origin = newOrigin
            game[0][0][newOrigin] = "X"
        else:
            game[1] =+ 1

    return jsonify(
        pongZone = game[0],
        origin = game[5],
        score_p1 = game[1],
        score_p2 = game[2]
    )


@app.route('/getRecord', methods =['GET'])
def getrecord():
    return jsonify(
        gameRecord = gamerecord
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')

