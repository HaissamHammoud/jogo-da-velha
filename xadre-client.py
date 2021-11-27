"""
Aqui sera desenvolvido a parte de cliente 
sera carregado a interface do jogo da velha e ele ira enviar as
informações e ações para o servidor
"""
# -*- coding: utf-8 -*-

import tkinter as tk
import socket
import time

player = "x"
sua_vez = True

class Application:

    def __init__(self, master=None):
        self.color = "white"
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.buttons = []
        for i in range(8):
            self.buttons.append([])
            self.color = "gray" if self.color == "white" else "white"
            for j in range(8):
                self.buttons[i].append(tk.Button(self.frame, fg = "black", width = 5, height = 5, bd = 0, bg = self.get_collor(), cursor = "hand2", name=(str(i)+(str(j)))))
                self.buttons[i][j]["command"] = lambda pl = player, ab = self.buttons[i][j]: self.press_button(pl,ab)
                self.buttons[i][j]["text"] = ""#str(i+j)
                self.buttons[i][j].grid(row = i, column = j, columnspan = 1, padx = 1, pady = 1)
                print(f"{self.buttons[-1]}")
        # self.info_frame = tk.Frame(self.frame, width = 100000, height = 100000, bg = "grey")
        # self.info_frame.pack()
        # self.status = tk.Message(self.info_frame, width = 1000)
        # self.status["text"] = "sua vez"
        # self.status.pack()
        self.put_pieces()
    def press_button(self, player, actual_button):
        row = actual_button.grid_info()["row"]
        column = actual_button.grid_info()["column"]
        print(f"Row:{row}   column: {column}")
        if actual_button["text"] == "-":
            actual_button["text"] = player
            self.status["text"] = "vez do outro"
            mensagem = row+column
            while True:
                print("aguardando")
                time.sleep(1)


    # def send_to_server(self, message):
    #     socketCliente.send("{}".format(mensagem).encode())
    def put_pieces(self):
        traz = ["T","B","\u265E","\u2654","\u2655","\u265E","B","T "]
        for i in range(8):
            self.buttons[0][i].config(font=100)
            self.buttons[0][i]["text"] = traz[i]
            print(f"{self.buttons[0][i]}")
            self.buttons[1][i]["text"] = "P"
            print(f"{self.buttons[1][i]}")

            self.buttons[7][i]["text"] = traz[i]
            self.buttons[7][i]["fg"]= "yellow"
            print(f"{self.buttons[0][i]}")
            self.buttons[6][i]["text"] = "P"
            self.buttons[6][i]["fg"]= "yellow"
            print(f"{self.buttons[1][i]}")


    def get_collor(self):
        if self.color == "gray":
            self.color = "white"
            return self.color
        else:
            self.color = "gray"
            return self.color

    def connect_to_server():
        time.sleep(1)
        print("conectando ao servidor")
        HOST = '192.168.0.1'    #endereco IP do servidor OBRIGATORIO
        PORT = 12343
        socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        enderecoServidor = (HOST, PORT)
        socketCliente.connect(enderecoServidor)
        print("servidor conectado!!")

        print ('Digite X para sair')
        nome = input('Digite seu nome : ').encode()
        mensagem = nome
        socketCliente.send(nome)
        while mensagem != b'X' :
            # recebe o tabuleiro
            mensagemRecebida = socketCliente.recv(105)
            print('Mensagem Recebida = \n', mensagemRecebida.decode())
            mensagem = input('Entre com sua jogada : ')
            socketCliente.send("{}".format(mensagem).encode())
            mensagemRecebida = socketCliente.recv(105)
        socketCliente.close()


    # self.button_one.pack()
root = tk.Tk()
root.geometry("1000x1000")
root.resizable(0,0)
root.title("Jogo da velha")
Application(root)
# Application.connect_to_server()
root.mainloop()