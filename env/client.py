import requests, time,json, sys


#Declaracion de variables basicas del servidor
protocolo = "http://"
server_ip = ""
port = ""
full_url = ""

#Path de los metodos para jugar
getGamePath = "/getInfo"
postMovementPath = "/startGame"
movePaddlePath = "/movePaddle/1"

#Creacion de URLs completos para las acciones del cliente
getGameUrl = full_url+getGamePath
postMoveUrl = full_url+postMovementPath
getEnemyMoveUrl = full_url+movePaddlePath

def getServerInfo():
    global server_ip ,port,full_url,getGameUrl,postMoveUrl,getEnemyMoveUrl

    server_ip = input("Ingrese la IP del servidor: ")
    port = input("Ingrese el puerto del servidor")
    full_url = protocolo + server_ip + ":" + port
    getGameUrl = full_url + getGamePath
    postMoveUrl = full_url + postMovementPath
    getEnemyMoveUrl = full_url + movePaddlePath

getServerInfo()


def testConnection():
    while True:
        try:
            #Hacemos una prueba de conexion para ver si el juego sigue
            request = requests.get(getGameUrl)
            return False
        except requests.exceptions.RequestException:
            print("Error de conexion. Intente ingresando la informacion del servidor de nuevo.")
            getServerInfo()



testConnection()

def getGameInfo():
    request = requests.get(getGameUrl)
    gameInfoJSON = json.dumps(request.json())
    gameInfoJSONParse = json.loads(gameInfoJSON)
    ##recibe bolas e info del juego
    return gameInfoJSONParse


def post():
    request = requests.post(postMoveUrl, data={'id': "1"})
    try:
        gamePostJSON = json.dumps(request.json())
        gamePostJSONParse = json.loads(gamePostJSON)
    except:
        print(gamePostJSONParse)

    return gamePostJSONParse

def movePaddle():
    request = requests.get(getEnemyMoveUrl)
    try:
        gameGetJSON = json.dumps(request.json())
        gameGetJSONParse = json.loads(gameGetJSON)
    except:
        print(gameGetJSONParse)
    return gameGetJSONParse


def juega():
    while True:
            gameInfo = getGameInfo()
            puntaje_p1 = gameInfo["score_p1"]
            puntaje_p2 = gameInfo["score_p2"]
            if (puntaje_p1 != 2) and (puntaje_p2 != 2):
                gameInfo = getGameInfo()
                turnoMovimiento = gameInfo["activePost"]
                if turnoMovimiento == "1":
                    postResponse= mueveBola()
                    if "balls" not in postResponse:
                        mueveRaqueta()
                    else:
                        mueveBola()
                else:
                    mueveBola()
            else:
                sys.exit("Fin del juego")


def mueveBola():
    time.sleep(3)
    postResponse = post()
    print("Jugador 1 hace post")
    print(postResponse)
    return postResponse

def mueveRaqueta():
<<<<<<< HEAD
    time.sleep(4)
=======
    time.sleep(5)
>>>>>>> 6d9d90cd2db65c045ffcee0aa9264c91cf05f883
    print("Jugador 1 hace get")
    getResponse = movePaddle()
    print(getResponse)







juega()
