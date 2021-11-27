import socket

#haissam Fawaz
def printTabuleiro(tabuleiro):
    return"""
          1 2 3
        1- {}|{}|{}
           -------
        2- {}|{}|{}
           -------
        3- {}|{}|{}""".format(
                            tabuleiro[0][0], 
                            tabuleiro[1][0], 
                            tabuleiro[2][0],
                            tabuleiro[0][1],
                            tabuleiro[1][1],
                            tabuleiro[2][1],
                            tabuleiro[0][2],
                            tabuleiro[1][2],
                            tabuleiro[2][2])

def Jogar(tabuleiro, comando, jogador):
    print(comando.decode())
    comandos = "{}".format(comando.decode())
    if len(comandos) == 2:
        coluna = int(comandos[0]) - 1
        linha = int(comandos[1]) - 1 
        if coluna > 2 or linha > 2 :
            return -1
        print(linha)
        print(coluna)
        if tabuleiro[linha][coluna] != "1" and tabuleiro[linha][coluna] != "2" :
            tabuleiro[linha][coluna] = "{}".format(jogador)
            return 1
    else:
        return -1
    
    return 1

HOST = ''           #endereco de IP é o da máquina atual
PORT = 12343
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enderecoServidor = (HOST,PORT)
socketServidor.bind(enderecoServidor)
socketServidor.listen(1)
while True :
    socketCliente, enderecoCliente = socketServidor.accept()
    socketServidor.close()
    print('Cliente conectado => ', enderecoCliente)
    nome = socketCliente.recv(100)
    mensagemEnviada = 'Conectado com sucesso'
    tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]
    while True :
        print(len(printTabuleiro(tabuleiro)))
        while True:
            socketCliente.send(printTabuleiro(tabuleiro).encode())
            mensagem = socketCliente.recv(2)
            resposta = Jogar(tabuleiro, mensagem, 2)
            socketCliente.send(printTabuleiro(tabuleiro).encode())
            print(printTabuleiro(tabuleiro))
            if resposta != -1:
                break 
        while True:
            ComandoJogador = input('Entre com sua jogada : ')
            resposta = Jogar(tabuleiro, ComandoJogador.encode(), 1)
            print(printTabuleiro(tabuleiro))
            if resposta != -1:
                break 

    print('Conexao finalizada com o cliente  ' , enderecoCliente)
    socketCliente.close()
    # sys.exit(0)