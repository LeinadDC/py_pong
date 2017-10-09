from flask import Flask,jsonify, request
import copy
from random import randint

app = Flask(__name__)


#Se declaran las variables
game =[]
pongZone = []
score_p1 = 0
score_p2 = 0
gameRound = 1
balls = 3
ballPosition = 0
gamerecord = []
activePost = "1"
activeGet = "2"
playerPaddle = ""

for x in range(2):
    pongZone.append(["0"] * 11)

game.append(pongZone)
game.append(score_p1)
game.append(score_p2)
game.append(gameRound)
game.append(balls)
game.append(ballPosition)
game.append(activePost)
game.append(activeGet)
game.append(playerPaddle)


def show_gamezone(zone):
    for row in zone:
        print(" ".join(row))

@app.route('/getInfo', methods = ['GET'])
def index():
    return jsonify(
        pongZone=game[0],
        score_p1=game[1],
        score_p2=game[2],
        gameRound=game[3],
        balls=game[4],
        ballPosition=game[5],
        playerMovingBall=game[6],
        playerMovingPaddle=game[7],
        playerPaddle=game[8]
    )


@app.route('/moveBall', methods = ['POST'])
def movement():
    playerID = request.form["id"]

    if game[6] == game[7]:
        return jsonify("Mueva la raqueta antes de mover la bola")
    else:
        if playerID == game[6]:
            playermove = randint(0,10)
            if playerID == "1":
                game[0][1][playermove] = "X"
                game[6] = str(2)
            else:
                game[0][0][playermove] = "X"
                game[6] = str(1)
        else:
            return jsonify("No le toca mover la bola")
    newgamerecord = copy.deepcopy(game)
    gamerecord.append(newgamerecord)
    game[5] = playermove
    return jsonify(
        pongZone=game[0],
        balls=game[4],
        ballPosition=game[5],
        playerPaddle=game[8],
        playerMovingBall=game[6],
        playerMovingPaddle=game[7]

    )

@app.route('/movePaddle/<string:player>', methods = ['GET'])
def getenemymove(player):
    ballPosition = game[5]

    if ballPosition == 0:
        "Debe esperar a que el otro jugador mueva"
    else:
            if player == game[7]:
                if player == "1":
                    playerpaddle = str(randint(0,10))
                    game[8] = playerpaddle
                    if playerpaddle == str(ballPosition):
                        game[0][0][ballPosition] = "0"
                        newOrigin = randint(0,10)
                        game[5] = newOrigin
                        game[0][1][newOrigin] = "X"
                        game[7] = "2"
                    else:
                        game[0][0][ballPosition] = "0"
                        game[0][1][ballPosition] = "0"
                        game[2] = game[2] + 1
                        game[4] = game[4] - 1
                        game[7] = "2"

                else:
                    playerpaddle = str(randint(0,10))
                    game[8] = playerpaddle

                    if playerpaddle == str(ballPosition):
                        game[0][1][ballPosition] = "0"
                        newOrigin = randint(0,10)
                        game[5] = newOrigin
                        game[0][0][newOrigin] = "X"
                        game[7] = "1"
                    else:
                        game[0][0][ballPosition] = "0"
                        game[0][1][ballPosition] = "0"
                        game[1] = game[1] + 1
                        game[4] = game[4] - 1
                        game[7] = "1"
            else:
                return jsonify("No le toca mover la raqueta")


    return jsonify(
        pongZone = game[0],
        ballPosition = game[5],
        playerPaddle=game[8],
        score_p1 = game[1],
        score_p2 = game[2],
        playerMovingBall=game[6],
        playerMovingPaddle=game[7],
        balls=game[4]

    )


@app.route('/getRecord', methods =['GET'])
def getrecord():
    return jsonify(
        gameRecord = gamerecord
    )

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

