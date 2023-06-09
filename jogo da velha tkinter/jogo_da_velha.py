#este codigo foi feito pelo canal, https://www.youtube.com/@usandopython, todos os creditos ao mesmo
#é a meu primeiro programa propriamente dito com python, possui erros mas estou feliz :)


import tkinter
from tkinter import *
from tkinter import ttk

# cores ---------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

#criando janela principal
janela = Tk()
janela.title('JOGO DA VELHA')
janela.geometry('260x440')
janela.configure(bg=fundo)

#dividindo a janela em dois frames

frame_cima= Frame (janela, width=240, height=100, bg=co3, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo= Frame (janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)



#CONFIG FRAME CIMA
player_x = Label(frame_cima, text='X', bg=co3, height=1, relief='flat', anchor='center', font='Ivy 50 bold', fg=co7)
player_x.place(x=25, y=10)

player_x = Label(frame_cima, text='Jogador 1', bg=co3, height=1, relief='flat', anchor='center', font='Ivy 7 bold', fg=co0)
player_x.place(x=25, y=75)

player_x_points = Label(frame_cima, text='0', bg=co3, height=1, relief='flat', anchor='center', font='Ivy 30 bold', fg=co0)
player_x_points.place(x=85, y=25)
 #separador
separator_points = Label(frame_cima, text=':', bg=co3, height=1, relief='flat', anchor='center', font='Ivy 18 bold', fg=co0)
separator_points.place(x=110, y=32)

#player 2

player_0 = Label(frame_cima, text='O', bg=co3, height=1, relief='flat', anchor='center', font='Ivy 50 bold', fg=co4)
player_0.place(x=155, y=8)

player_o= Label(frame_cima, text='Jogador 2', bg=co3, height=1, relief='flat', anchor='center', font='Ivy 7 bold', fg=co0)
player_o.place(x=159, y=75)

player_0_points = Label(frame_cima, text='0', bg=co3, height=1, relief='flat', anchor='center', font='Ivy 30 bold', fg=co0)
player_0_points.place(x=120, y=25)

#CONFIG FRAME BAIXO



#Logica do jogo

jogador1= "X"
jogador2= "O"

score_1= 0
score_2= 0

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

playing = 'X'
play= ''
counter = 0



def start_game():
    #game rules
    def game_control(i):
        global playing
        global counter
        global play
      
        #comparando valor recebido
        #CONDIÇÕES DE VITORIA BOTOES
        if i==str(1):
            #espaço 0
            #verificando se a posição esta vazia
            if botao_0['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co4
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_0['fg']= cor
                botao_0['text']= playing
                board[0][0] = playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 2'
                else:
                    playing = 'X'
                    play = 'Jogador 1'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                #contador >= 5 verifica se há vencedor
               
        
        if i==str(2):
            #espaço 1
            #verificando se a posição esta vazia
            if botao_1['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co8
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_1['fg']= cor
                botao_1['text']= playing
                board[0][1]= playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                #contador >= 5 verifica se há vencedor
               
                    
        if i==str(3):
            #espaço 2
            #verificando se a posição esta vazia
            if botao_2['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co8
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_2['fg']= cor
                botao_2['text']= playing
                board[0][2]= playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                      
                 
        if i==str(4):
            #espaço 3
            #verificando se a posição esta vazia
            if botao_3['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co8
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_3['fg']= cor
                botao_3['text']= playing
                board[1][0]= playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                #contador >= 5 verifica se há vencedor
                          
        
        if i==str(5):
            #espaço 4
            #verificando se a posição esta vazia
            if botao_4['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co8
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_4['fg']= cor
                botao_4['text']= playing
                board[1][1]= playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                #contador >= 5 verifica se há vencedor
              
        if i==str(6):
            #espaço 5
            #verificando se a posição esta vazia
            if botao_5['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co8
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_5['fg']= cor
                botao_5['text']= playing
                board[1][2]= playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                #contador >= 5 verifica se há vencedor
                
        if i==str(7):
            #espaço 6
            #verificando se a posição esta vazia
            if botao_6['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co8
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_6['fg']= cor
                botao_6['text']= playing
                board[2][0]= playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                #contador >= 5 verifica se há vencedor
               
                 
        if i==str(8):
            #espaço 7
            #verificando se a posição esta vazia
            if botao_7['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co8
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_7['fg']= cor
                botao_7['text']= playing
                board[2][1]= playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                #contador >= 5 verifica se há vencedor
                           
       
        if i==str(9):
            #espaço 8
            #verificando se a posição esta vazia
            if botao_8['text']== '':
                #verificando quem ocupa a posição
                if playing == 'X':
                    cor=co7
                if playing == 'O':
                    cor=co8
                #definindo a cor do botão e marcar a posição como ocupada pelo jogador atual
                botao_8['fg']= cor
                botao_8['text']= playing
                board[2][2]= playing
                #verificando quem esta jogando para poder trocar a vez
                if playing == 'X':
                    playing = 'O'
                    play = 'Jogador 1'
                else:
                    playing = 'X'
                    play = 'Jogador 2'
                #incrementar o contador de pontos para a proxima jogada
                counter +=1
                #contador >= 5 verifica se há vencedor
                
         #contador >= 5 verifica se há vencedor
        if counter >=5:
                    #linhas
            if board[0][0]== board[0][1] ==board[0][2]!="":
                        winner_select(playing)
            elif board[1][0] == board[1][1] ==board[1][2]!="":
                        winner_select(playing)
            elif board[2][0]== board[2][1] ==board[2][2]!="":
                        winner_select(playing)
                        
                    #colunas
            if board[0][0] == board[1][0] ==board[2][0]!="":
                        winner_select(playing)
            elif board[0][1] == board[1][1] ==board[2][1]!="":
                        winner_select(playing)
            elif board[0][2] == board[1][2] ==board[2][2]!="":
                        winner_select(playing)
                        
                    #diagonal
            if board[0][0] == board[1][1] ==board[2][2]!="":
                        winner_select(playing)
            elif board[0][2] == board[1][1] ==board[2][0]!="":
                        winner_select(playing)
                    
                    #EMPATE
            if counter >= 9:
                winner_select('Empate!')                                 

    #winner select
    def winner_select(i):
        global round_counter
        global counter
        global playing
        global board
        global score_1
        global score_2
        
       
        
        
        winner = Label(frame_baixo, width=17, text='', height=1, padx=0, relief="raised", anchor='center', font=('Ivy 12 bold'), bg=co1, fg=co2)
        winner.place(x=30, y=90)
        
        if i == 'Empate!':
            winner['text']='FOI EMPATE!'
            
        if i == 'X':
            score_2+=1
            player_0_points['text']=score_2
            winner['text']='Jogador 2 venceu!'
        if i == 'O':
            score_1+=1
            player_x_points['text']=score_1
            winner['text']='Jogador 1 venceu!'
            
        
        def start():
            # limpando os botoes
            botao_0['text']=''
            botao_1['text']=''
            botao_2['text']=''
            botao_3['text']=''
            botao_4['text']=''
            botao_5['text']=''
            botao_6['text']=''
            botao_7['text']=''
            botao_8['text']=''

            botao_0['state']='normal'
            botao_1['state']='normal'
            botao_2['state']='normal'
            botao_3['state']='normal'
            botao_4['state']='normal'
            botao_5['state']='normal'
            botao_6['state']='normal'
            botao_7['state']='normal'
            botao_8['state']='normal'
            
            winner.destroy()
            play_button.destroy()
            
            play_button= Button(frame_baixo, command=start, text='Proxima rodada', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
            play_button.place(x=70, y=197)

            
        def jogo_acabou():
            play_button.destroy()
            winner.destroy()

            end_game()

        if round_counter>=5:
            jogo_acabou()
        else:
            round_counter+=1
            # reiniciando a tabela
            board = [['', '', ''], ['', '', ''], ['', '', '']]
            counter = 0
    
    #End game
    def end_game():
        global round_counter
        global counter
        global board
        global score_1
        global score_2
        
        boarboard = [['', '', ''],['', '', ''],['', '', '']]
        round_counter = 0
        score_1 = 0
        score_2 = 0
        counter = 0
        
        botao_0['state']='disable'
        botao_1['state']='disable'
        botao_2['state']='disable'
        botao_3['state']='disable'
        botao_4['state']='disable'
        botao_5['state']='disable'
        botao_6['state']='disable'
        botao_7['state']='disable'
        botao_8['state']='disable'

        app_fim = Label(frame_baixo, text='Jogo Acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_fim.place(x=25, y=90)
        
        def jogar_denovo():
            player_x_points['text'] = '0'
            player_0_points['text'] = '0'
            app_fim.destroy()
            play_button.destroy()
            
            start_game()
            
        play_button = Button(frame_baixo, command=jogar_denovo, text='Jogar de novo', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        play_button.place(x=80, y=197)


        
    
    
    
        #linhas verticais

    grid = Label(frame_baixo, text='', bg=co0, height=19, relief='flat', pady=5,  anchor='center', font='Ivy 7 bold', fg=co7)
    grid.place(x=90, y=15)
    grid = Label(frame_baixo, text='', bg=co0, height=19, relief='flat', pady=5,  anchor='center', font='Ivy 7 bold', fg=co7)
    grid.place(x=160, y=15)

    #linhas horizontais


    grid_hori = Label(frame_baixo, text='', bg=co0, width=190, relief='flat', padx=2, pady=1,  anchor='center', font=('Ivy 1 bold'), fg=co7)
    grid_hori.place(x=30, y=80)

    grid_hori = Label(frame_baixo, text='', bg=co0, width=190, relief='flat', padx=2, pady=1, anchor='center', font='Ivy 1 bold', fg=co7)
    grid_hori.place(x=30, y=160)



    #botões linha 0
    
    botao_0 = Button(frame_baixo,command=lambda:game_control('1'),  text='', bg=fundo, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_0.place(x=27, y=20)
    
    botao_1 = Button(frame_baixo,command=lambda:game_control('2'),  text='', bg=fundo, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_1.place(x=97, y=20)
    
    botao_2 = Button(frame_baixo,command=lambda:game_control('3'),  text='', bg=fundo, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_2.place(x=169, y=20)
    #linha 1
    botao_3 = Button(frame_baixo,command=lambda:game_control('4'),  text='', bg=fundo, height=1, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_3.place(x=27, y=97)

    botao_4 = Button(frame_baixo,command=lambda:game_control('5'),  text='', bg=fundo, height=1, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_4.place(x=97, y=97)

    botao_5 = Button(frame_baixo,command=lambda:game_control('6'),  text='', bg=fundo, height=1, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_5.place(x=169, y=97)

    #linha 2

    botao_6 = Button(frame_baixo,command=lambda:game_control('7'),  text='', bg=fundo, height=1, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_6.place(x=27, y=175)

    botao_7 = Button(frame_baixo,command=lambda:game_control('8'),  text='', bg=fundo, height=1, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_7.place(x=97, y=175)

    botao_8 = Button(frame_baixo,command=lambda:game_control('9'),  text='', bg=fundo, height=1, width=3, font=('Ivy 20 bold'), overrelief=RIDGE,relief=FLAT, fg=co7)
    botao_8.place(x=169, y=175)

#botão play

play_button = Button(frame_baixo, command=start_game, text='Jogar', bg=fundo, height=1, width=8, font=('Ivy 14 bold'), overrelief=RIDGE,relief='raised', fg=co6)
play_button.place(x=78, y=255)


















janela.mainloop()
