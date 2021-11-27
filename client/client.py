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


class Application:

    def __init__(self, master=None):
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.buttons_frame = tk.Frame(self.frame, width = 312, height = 272.5, bg = "grey")
        self.buttons_frame.pack()

        self.button_one = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", name = "1")
        self.button_one["command"] = lambda: self.press_button(player,self.button_one)
        self.button_one.grid(row = 1, column = 0, columnspan = 1, padx = 1, pady = 1)
        self.button_two = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
        self.button_two["command"] = lambda: self.press_button(player,self.button_two)
        self.button_two.grid(row = 1, column = 1, columnspan = 1, padx = 1, pady = 1)
        self.button_three = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
        self.button_three["command"] = lambda: self.press_button( player, self.button_three)
        self.button_three.grid(row = 1, column = 2, columnspan = 1, padx = 1, pady = 1)

        self.button_four = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
        self.button_four["command"] = lambda: self.press_button(player, self.button_four)
        self.button_four.grid(row = 2, column = 0, columnspan = 1, padx = 1, pady = 1)
        self.button_five = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
        self.button_five["command"] = lambda: self.press_button(player, self.button_five)
        self.button_five.grid(row = 2, column = 1, columnspan = 1, padx = 1, pady = 1)
        self.button_six = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
        self.button_six["command"] = lambda: self.press_button(player, self.button_six)
        self.button_six.grid(row = 2, column = 2, columnspan = 1, padx = 1, pady = 1)

        self.button_seven = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
        self.button_seven["command"] = lambda: self.press_button(player, self.button_seven)
        self.button_seven.grid(row = 3, column = 0, columnspan = 1, padx = 1, pady = 1)
        self.button_eight = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
        self.button_eight["command"] = lambda: self.press_button(player, self.button_eight)
        self.button_eight.grid(row = 3, column = 1, columnspan = 1, padx = 1, pady = 1)
        self.button_nine = tk.Button(self.buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2")
        self.button_nine["command"] = lambda: self.press_button(player, self.button_nine)
        self.button_nine.grid(row = 3, column = 2, columnspan = 1, padx = 1, pady = 1)

        self.info_frame = tk.Frame(self.frame, width = 312, height = 272.5, bg = "grey")
        self.info_frame.pack()
        self.status = tk.Message(self.info_frame, width = 1000)
        self.status["text"] = "sua vez"
        self.status.pack()

    def press_button(self, player, actual_button):
        row = actual_button.grid_info()['row']
        column = actual_button.grid_info()["column"]
        print(f"Row:{row}   column: {column}")
        if actual_button["text"] == "-":
            actual_button["text"] = player
            self.status["text"] = "vez do outro"
            mensagem = row+column
            socketCliente.send("{}".format(mensagem).encode())
            while True:
                print("aguardando")
                time.sleep(1)
            # Enviar dados para o servidor
            # receber resposta do servidor
            # aguardar proxima resposta do servidor

    def send_to_server(self, message):
        socketCliente.send("{}".format(mensagem).encode())


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
root.geometry("312x324")
root.resizable(0,0)
root.title("Jogo da velha")
Application(root)
# Application.connect_to_server()
root.mainloop()