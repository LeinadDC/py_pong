from flask import Flask,jsonify, request,json
import copy
from random import randint

app = Flask(__name__)


#Se declaran las variables
game = {}
pongZone = []
score_p1 = 0
score_p2 = 0
gameRound = 0
balls = 3
ballPosition = 0
gamerecord = []
activePost = ""
activeGet = ""
<<<<<<< HEAD
playerPaddle = ""
=======
playerPaddle = 0
>>>>>>> 6d9d90cd2db65c045ffcee0aa9264c91cf05f883

for x in range(2):
    pongZone.append(["0"] * 11)


game['pongZone'] = pongZone
game['score_p1'] = score_p1
game['score_p2'] = score_p2
game['gameRound'] = gameRound
game['balls'] = balls
game['ballPosition'] = ballPosition
game['activeGet'] = activeGet
game['activePost'] = activePost
game['playerPaddle'] = playerPaddle



def show_gamezone(zone):
    for row in zone:
        print(" ".join(row))

@app.route('/getInfo', methods = ['GET'])
def index():
    gameJson = json.dumps(game)
    return gameJson


@app.route('/startGame', methods = ['POST'])
def movement():
    playerID = request.form["id"]

<<<<<<< HEAD
    if game[6] == "" and game[7] == "":
        if playerID == "1":
            game[7] = "2"
            game[6] = "1"
        else:
            game[7] = "1"
            game[6] = "2"

    if game[6] == game[7]:
        return jsonify("Mueva la raqueta antes de mover la bola")
=======
    defineTurns(playerID)

    if game['activeGet'] == game['activePost']:
        return jsonify("Ya se hizo el movimiento inicial")
>>>>>>> 6d9d90cd2db65c045ffcee0aa9264c91cf05f883
    else:
        if playerID == game['activePost']:
            playermove = randint(0,10)
            if playerID == "1":
                firstPlayerMovement(playermove)
            else:
                secondPlayerMovement(playermove)
        else:
            return jsonify("No le toca mover la bola")
<<<<<<< HEAD
    addRecord()
    game[5] = playermove
    return jsonify(
        pongZone=game[0],
        balls=game[4],
        ballPosition=game[5],
        playerPaddle=game[8],
        playerMovingBall=game[6],
        playerMovingPaddle=game[7]
=======

    addToRecord()
    game['ballPosition'] = playermove
    gameJson = json.dumps(game)
    return gameJson


def firstPlayerMovement(playermove):
    game['pongZone'][1][playermove] = "X"
    game['activePost'] = str(2)
    game['gameRound'] = 1


def secondPlayerMovement(playermove):
    game['pongZone'][0][playermove] = "X"
    game['activePost'] = str(1)
    game['gameRound'] = 1


def addToRecord():
    newgamerecord = copy.deepcopy(game)
    gamerecord.append(newgamerecord)
>>>>>>> 6d9d90cd2db65c045ffcee0aa9264c91cf05f883


def defineTurns(playerID):
    if game['activeGet'] == "" and game['activePost'] == "":
        if playerID == "1":
            game['activeGet'] = "2"
            game['activePost'] = "1"
        else:
            game['activeGet'] = "1"
            game['activePost'] = "2"



def addRecord():
    newgamerecord = copy.deepcopy(game)
    gamerecord.append(newgamerecord)


@app.route('/movePaddle/<string:player>', methods = ['GET'])
def getenemymove(player):
<<<<<<< HEAD
    ballPosition = game[5]
    if game[3] > 0:

        if game[6] == "" and game[7] == "":
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
                            addRecord()
                        else:
                            game[0][0][ballPosition] = "0"
                            game[0][1][ballPosition] = "0"
                            game[2] = game[2] + 1
                            game[4] = game[4] - 1
                            game[7] = "2"
                            addRecord()

                    else:
                        playerpaddle = str(randint(0,10))
                        game[8] = playerpaddle

                        if playerpaddle == str(ballPosition):
                            game[0][1][ballPosition] = "0"
                            newOrigin = randint(0,10)
                            game[5] = newOrigin
                            game[0][0][newOrigin] = "X"
                            game[7] = "1"
                            addRecord()
                        else:
                            game[0][0][ballPosition] = "0"
                            game[0][1][ballPosition] = "0"
                            game[1] = game[1] + 1
                            game[4] = game[4] - 1
                            game[7] = "1"
                            addRecord()
                else:
                    return jsonify("No le toca mover la raqueta")
    else:
        return jsonify("Se terminó el juego")
    return jsonify(
        pongZone = game[0],
        ballPosition = game[5],
        playerPaddle=game[8],
        score_p1 = game[1],
        score_p2 = game[2],
        playerMovingBall=game[6],
        playerMovingPaddle=game[7],
        balls=game[4]
=======
    if game['balls'] > 0:
        if game['activeGet'] == "" and game['activePost'] == "":
            "Debe esperar a que el otro jugador mueva"
        else:
            if game['gameRound'] == 1:
                if player == game['activeGet']:
                    if player == "1":
                        playerpaddle = generatePaddleMovement()
                        game['playerPaddle'] = playerpaddle
                        if playerpaddle == game['ballPosition']:
                            firstPlayerBounce(game['ballPosition'])
                            addToRecord()
                        else:
                            firstPlayerScored(game['ballPosition'])
                            addToRecord()
                    else:
                        playerpaddle = generatePaddleMovement()
                        game['playerPaddle'] = playerpaddle
                        if playerpaddle == game['ballPosition']:
                            secondPlayerBounce(game['ballPosition'])
                            addToRecord()
                        else:
                            secondPlayerScored(game['ballPosition'])
                            addToRecord()
                else:
                    return jsonify("No le toca mover la raqueta")
            else:
                return jsonify("Se debe iniciar otra ronda")
    else:
        return ("Partida finalizada")
    gameJson = json.dumps(game)
    return gameJson


def generatePaddleMovement():
    playerpaddle = randint(0, 10)
    return playerpaddle
>>>>>>> 6d9d90cd2db65c045ffcee0aa9264c91cf05f883


def firstPlayerBounce(ballPosition):
    game['pongZone'][0][ballPosition] = "0"
    newOrigin = randint(0, 10)
    game['ballPosition'] = newOrigin
    game['pongZone'][1][newOrigin] = "X"
    game['activeGet'] = "2"


def secondPlayerBounce(ballPosition):
    game['pongZone'][1][ballPosition] = "0"
    newOrigin = randint(0, 10)
    game['ballPosition'] = newOrigin
    game['pongZone'][0][newOrigin] = "X"
    game['activeGet'] = "1"



def firstPlayerScored(ballPosition):
    game['pongZone'][0][ballPosition] = "0"
    game['pongZone'][1][ballPosition] = "0"
    game['score_p1'] = game['score_p1'] + 1
    game['balls'] = game['balls'] - 1
    game['activeGet'] = "2"
    game[gameRound] = 0
    game['playerPaddle'] = 0


def secondPlayerScored(ballPosition):
    game['pongZone'][0][ballPosition] = "0"
    game['pongZone'][1][ballPosition] = "0"
    game['score_p2'] =  game['score_p2'] + 1
    game['balls'] = game['balls'] - 1
    game['activeGet'] = "1"
    game['gameRound'] = 0
    game['playerPaddle'] = 0


dumpToJSON = json.dumps(game)
converToJSON = json.loads(dumpToJSON)
@app.route('/getRecord', methods =['GET'])
def getrecord():
    return jsonify(
        gameRecord = gamerecord
    )

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

