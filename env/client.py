import requests, time,json


#Declaracion de variables basicas del servidor
protocolo = "http://"
server_ip = ""
port = ""
full_url = ""

#Path de los metodos para jugar
getGamePath = "/getGame"
postMovementPath = "/move"
getEnemyMovePath = "/getEnemyMove"

#Creacion de URLs completos para las acciones del cliente
getGameUrl = full_url+getGamePath
postMoveUrl = full_url+postMovementPath
getEnemyMoveUrl = full_url+getEnemyMovePath

def getServerInfo():
    global server_ip ,port,full_url,getGameUrl,postMoveUrl,getEnemyMoveUrl

    server_ip = input("Ingrese la IP del servidor: ")
    port = input("Ingrese el puerto del servidor")
    full_url = protocolo + server_ip + ":" + port
    getGameUrl = full_url + getGamePath
    postMoveUrl = full_url + postMovementPath
    getEnemyMoveUrl = full_url + getEnemyMovePath

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
    gamePostJSON = json.dumps(request.json())
    gamePostJSONParse = json.loads(gamePostJSON)

    return gamePostJSONParse

def get():
    request = requests.get(getEnemyMoveUrl, data={'id': "1"})
    try:
        gameGetJSON = json.dumps(request.json())
        gameGetJSONParse = json.loads(gameGetJSON)
    except:
        return("No es su turno")
    return gameGetJSONParse


def juega():
    while True:
            postResponse = post()
            print(postResponse)

            if "balls" in postResponse:
                getResponse = get()
                print(getResponse)
                if "balls" not in getResponse:
                    return False


juega()





'''


            game = json.dumps(request.json())
            gameTest = json.loads(game)

            if 'pongZone' not in gameTest:
                print("Falta el otro cliente")
                return False
            else:
                test = requests.post(postMoveUrl, data={'id': "1"})
                print("Haciendo movimiento")
                

            return False
            # time.sleep(18)
def postMovement():
    try:
        request = requests.post(postMoveUrl,data={'id':1})
        #print(request.json())
        #time.sleep(18)
    except requests.exceptions.RequestException:
        print("Error de conexion. Intente ingresando la informacion del servidor de nuevo.")
        getServerInfo()
        printInfo()
        
def getGame():
    response = requests.get(getGameUrl)
    print(response.json())
    #time.sleep(15)



while True:
    postMovement()
'''
