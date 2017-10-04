import requests, time

url = "http://192.168.0.10:5000/"

def getGame():
    response = requests.get("http://192.168.0.10:5000/getGame")
    print(response.json())
    time.sleep(15)

def postMovement():
    request = requests.post("http://192.168.0.10:5000/move",data={'id':1})
    print(request.json())
    time.sleep(18)


while True:
    postMovement()
