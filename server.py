import socket, sys
from time import sleep
from threading import Thread
from chess import *

SIZE = 100000
HOST = '127.0.0.1'
PORT = 12345
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = (HOST, PORT)
serverSocket.bind(serverAddress)
serverSocket.listen(5)

def chess():
    print('Cliente conectado => ', clientAddress)
    message = welcome()
    clientSocket.send(message.encode())
    while True:
        clientResponse = clientSocket.recv(SIZE).decode()
        if not clientResponse: break
        while True:
            clientResponse = clientSocket.recv(SIZE).decode()
            if not clientResponse: break
            if clientResponse == 'jogar':
                break
            message = toPlayOrNotToPlay()
            clientSocket.send(message.encode())
        message = weArePlaying()
        clientSocket.send(message.encode())
        clientResponse = clientSocket.recv(SIZE).decode()
        if not clientResponse: break
        while True:
            if clientResponse == 'preto' or clientResponse == 'branco':
                break
            message = chooseYourColor()
            clientSocket.send(message.encode())
            clientResponse = clientSocket.recv(SIZE).decode()
            if not clientResponse: break
        clientColor, serverColor = assignColors(clientResponse)
        clientPieces, serverPieces = assignPieces(clientColor)
        matrix = createTable(clientColor)
        table = renderTable(matrix)
        if clientResponse == "preto":
            print('O cliente está jogando com as peças pretas')
            print('O servidor jogará com as peças brancas')
        elif clientResponse == "branco":
            print('O cliente está jogando com as peças brancas')
            print('O servidor jogará com as peças pretas')
        sleep(3)
        if clientColor == "preto":
            table = renderTable(matrix, True)
            while True:
                print(table)
                play = input("Sua vez : ")
                matrix, message, valid = turn(matrix, serverPieces, play)
                table = renderTable(matrix)
                if valid:
                    break
                print(message)
        message = table + '\n' + blackOrWhite(clientResponse)
        winner = False
        while True:
            clientSocket.send(message.encode())
            print("O cliente está jogando...")
            clientResponse = clientSocket.recv(SIZE).decode()
            if not clientResponse: break
            # client
            while True:
                matrix, message, valid = turn(matrix, clientPieces, clientResponse, True)
                if valid:
                    break
                clientSocket.send(message.encode())
                clientResponse = clientSocket.recv(SIZE).decode()
                if not clientResponse: break
            winner = theKingIsDead(clientPieces,serverPieces)
            if winner:
                break
            table = renderTable(matrix, True)
            # server
            while True:
                print(table)
                print(message)
                play = input("Sua vez : ")
                matrix, message, valid = turn(matrix, serverPieces, play)
                if valid:
                    break
            winner = theKingIsDead(clientPieces,serverPieces)
            if winner:
                break
            table = renderTable(matrix)
            message = table + '\nSua vez'
        if winner == "client":
            message = "Parabéns! Você venceu!\nJogar novamente?"
        else:
            message = "Que pena! Você perdeu!\nJogar novamente?"
        clientSocket.send(message.encode())
    print('Conexão finalizada com o cliente  ', clientAddress)
    clientSocket.close()
    sys.exit(0)

while True:
    clientSocket, clientAddress = serverSocket.accept()
    Thread(target=chess).start()