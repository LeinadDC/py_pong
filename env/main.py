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
activePost = str(1)
activeGet = str(2)

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
        balls=game[4],
        ballPosition=game[5],
        playerMovingBall=game[6],
        playerMovingPaddle=game[7]
    )


@app.route('/move', methods = ['POST'])
def movement():
    global activePost, ballPosition
    #Obtiene el id del form (porque en envia mediante body al ser POST)
    playerID = request.form["id"]
    #Compara si el jugador haciendo el requests es el activo
    if playerID == activePost:
        #Se genera un movimiento al azar
        playermove = randint(0,10)
        #Se compara cual jugador es el que está haciendo el movimiento
        if playerID == "1":
            game[0][1][playermove] = "X"
            game[6] = str(2)
            activePost = game[6]

        else:
            game[0][0][playermove] = "X"
            game[6] = str(1)
            activePost = game[6]
    else:
        #Si no es el turno del jugador se le duelve un texto en JSON
        return jsonify("No es su turno.")
    #Se hace una deepCopy del estado del juego actual para pasarlo al historico
    newgamerecord = copy.deepcopy(game)
    #Se agrega el estado actual del juego al historico
    gamerecord.append(newgamerecord)
    #La posición de la bola agarra el mismo valor del movimiento que hizo el jugador
    ballPosition = playermove
    #Se le regresa la zona de juego
    return jsonify(
        pongZone=game[0],
        balls=game[4],
        ballPosition=game[5],
        playerMovingBall=game[6],
        playerMovingPaddle=game[7]

    )

@app.route('/getEnemyMove/<string:player>', methods = ['GET'])
def getenemymove(player):
    global ballPosition,activeGet

    if player == activeGet:
        if player == "1":
            playerpaddle = randint(0, 10)
            if playerpaddle == ballPosition:
                game[0][1][ballPosition] = "0"
                newOrigin = randint(0, 10)
                ballPosition = newOrigin
                game[0][0][newOrigin] = "X"
                game[7] = "2"
                activeGet = game[7]
            else:
                game[4] = game[4] - 1
                game[1] = "Punto jugador 2"
        else:
            playerpaddle = ballPosition
            if playerpaddle == ballPosition:
                game[0][1][ballPosition] = "0"
                newOrigin = randint(0, 10)
                ballPosition = newOrigin
                game[0][0][newOrigin] = "X"
                game[7] = "1"
                activeGet = game[7]
            else:
                game[4] = - 1
                game[2] = "Punto jugador 1"
    else:
        return jsonify("No es su turno.")


    return jsonify(
        pongZone = game[0],
        ballPosition = game[5],
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

