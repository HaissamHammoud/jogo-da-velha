"""
Aqui sera desenvolvido a parte de cliente 
sera carregado a interface do jogo da velha e ele ira enviar as
informações e ações para o servidor
"""
# -*- coding: utf-8 -*-

import tkinter as tk
import socket
import time
from tkinter import font as tkFont
player = "x"
sua_vez = True
REI_BRANCO = "\u2654"
DAMA_BRANCA = "\u2655"
TORRE_BRANCA = "\u2656"
BISPO_BRANCO = "\u2657"
CAVALO_BRANCO = "\u2658"
PEAO_BRANCO = "\u2659"
REI_PRETO = "\u265A"
DAMA_PRETA = "\u265B"
TORRE_PRETA = "\u265C"
BISPO_PRETO = "\u265D"
CAVALO_PRETO = "\u265E"
PEAO_PRETO = "\u265F"
PECAS_BRANCAS = [REI_BRANCO,DAMA_BRANCA,TORRE_BRANCA,BISPO_BRANCO,CAVALO_BRANCO,PEAO_BRANCO]
class Application:

    def __init__(self, master=None):
        self.color = "white"
        self.SELECTED_PIECE = tk.Button()
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.YOUR_COLLOR = "white"
        self.your_turn = True
        self.buttons = []
        self.connection = self.connect_to_server() 
        self.build_board()
        self.put_pieces()

    def build_board(self):
        for i in range(8):
            self.buttons.append([])
            self.color = "gray" if self.color == "white" else "white"
            for j in range(8):
                self.buttons[i].append(tk.Button(self.frame, 
                    fg = "black", 
                    width = 3,
                    height = 3, 
                    bd = 0, 
                    bg = self.get_collor(), 
                    cursor = "hand2", name=(str(i)+(str(j)))))
                self.buttons[i][j]["command"] = lambda pl = player, ab = self.buttons[i][j]: self.press_button(pl,ab, self.connection)
                self.buttons[i][j]["text"] = ""#str(i+j)
                self.buttons[i][j].grid(row = i, column = j)

    def press_button(self, player, actual_button,connection):
        if not self.your_turn:
            return

        from_row = str(actual_button.grid_info()["row"])
        from_column = str(actual_button.grid_info()["column"])
        if self.SELECTED_PIECE["text"] == "" and actual_button["text"] in PECAS_BRANCAS :
            self.SELECTED_PIECE = actual_button
            return

        if self.SELECTED_PIECE["text"] != "" and actual_button != "" and actual_button["text"] not in PECAS_BRANCAS:
            to_row = str(self.SELECTED_PIECE.grid_info()["row"])
            to_column = str(self.SELECTED_PIECE.grid_info()["column"])
            #SEND RESPONSE
            #GET RESPONSE
            #IF RESPONDE TRUE THAN ...
            #IF NOT UNDONE THE MOVEMENT OR CLEAR THE PIECE
            print(connection)
            print(from_row+from_column+","+to_row+to_column)
            connection.send((from_row+from_column+","+to_row+to_column).encode())
            recieve = connection.recv(2)
            if recieve.decode() == "ok":
                actual_button["text"] = self.SELECTED_PIECE["text"]
                # self.SELECTED_PIECE["text"] = ""                
                self.move_pieces(self.SELECTED_PIECE, actual_button)

                # self.move_pieces(self.SELECTED_PIECE, actual_button)
                # connection.send("oi".encode())

                response = connection.recv(1)
                print(response.decode())
                # self.your_turn = False
                response = connection.recv(5)
                self.move_pieces_enemy(response.decode())
                self.your_turn = True
            else:
                print("invalid movement")
            # self.your_turn = not(self.your_turn)
            return   

    
    def move_pieces_enemy(self, path):
        from_place = self.buttons[int(path[0])][int(path[1])]
        to_place = self.buttons[int(path[3])][int(path[4])]

        self.move_pieces( from_place, to_place)

    def move_pieces(self, actual_position, next_position):
        next_position["text"] = actual_position["text"]
        actual_position["text"] = ""

    def put_pieces(self):
        traz_preto = [TORRE_PRETA,BISPO_PRETO,CAVALO_PRETO,REI_PRETO,DAMA_PRETA,CAVALO_PRETO,BISPO_PRETO,TORRE_PRETA]
        traz_branco = [TORRE_BRANCA,BISPO_BRANCO,CAVALO_BRANCO,REI_BRANCO,DAMA_BRANCA,CAVALO_BRANCO,BISPO_BRANCO,TORRE_BRANCA]

        for i in range(8):
            helv36 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
            self.buttons[0][i].config(font = helv36)
            self.buttons[1][i].config(font = helv36)
            self.buttons[2][i].config(font = helv36)
            self.buttons[3][i].config(font = helv36)
            self.buttons[4][i].config(font = helv36)
            self.buttons[5][i].config(font = helv36)
            self.buttons[6][i].config(font = helv36)
            self.buttons[7][i].config(font = helv36)
            self.buttons[0][i]["text"] = traz_preto[i]
            print(f"{self.buttons[0][i]}")
            self.buttons[1][i]["text"] = PEAO_PRETO
            print(f"{self.buttons[1][i]}")

            self.buttons[7][i]["text"] = traz_branco[i]
            print(f"{self.buttons[0][i]}")
            self.buttons[6][i]["text"] = PEAO_BRANCO
            print(f"{self.buttons[1][i]}")

    def get_collor(self):
        if self.color == "gray":
            self.color = "white"
            return self.color
        else:
            self.color = "gray"
            return self.color

    def connect_to_server(self):
        time.sleep(1)
        print("conectando ao servidor")
        HOST = 'localhost'    #endereco IP do servidor OBRIGATORIO
        PORT = 12341
        socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        enderecoServidor = (HOST, PORT)
        socketCliente.connect(enderecoServidor)
        
        return socketCliente


    # self.button_one.pack()
root = tk.Tk()
root.geometry("1000x1000")
root.resizable(0,0)
root.title("Jogo da velha")
Application(root)
# Application.connect_to_server()
root.mainloop()