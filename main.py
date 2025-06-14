import pygame
import tkinter as tk
import random as rand

pygame.init()

matrix = []

vetor_dir = [
    {-1, 0}, # Cima
    {-1, -1}, # cima_esq
    {-1, 1}, # cima_dir
    {1, 0},  # Baixo
    {1, -1}, # Baixo_esq
    {1, 1}, # Baixo_dir
    {0, -1}, # Esquerda
    {0, 1}   # Direita
]

def unveil(r,c):
    print(f'{r}{c}')
    
def create_matrix_game(size):

    for line_counter in range(size):
        linha = []
        
        for column_counter in range(size):
            linha.append(0)
        
        matrix.append(linha)
        
    for row in matrix:
        print(row)
    
    print("")
    print("")
    
    put_flags(size)
    return
        
def put_flags(size):
    n_flags = round(size * 1.5)
    
    flag_counter = 0
    
    while flag_counter < n_flags:
        x = rand.randint(0,size-1)
        y = rand.randint(0,size-1)
        
        if matrix[x][y] == -5:
            continue
        
        matrix[x][y] = -5
        flag_counter += 1
    
    for row in matrix:
        print(row)
        
    fufiel_matrix(size)
        
    return

def fufiel_matrix(size):
    
    for line_counter in range(size):
        for column_counter in range(size):
            
            if matrix[line_counter][column_counter] == -5:
                continue
            
            n_falgs = get_flag_number(line_counter,column_counter) 


def get_flag_number(line,column):
    
    aux_line = 0
    aux_column = 0
    
    for i in range(8):
        
        aux_line = line + vetor_dir[i][0]
        aux_column = column + vetor_dir[i][1]
        
    

def create_button_grid(size):
    janela = tk.Tk()
    janela.title(f"{size} x {size} Button Grid")
    janela.geometry(f"{size*size*2}x{size*size*2}")

    for row in range(size):
        for col in range(size):
            botao = tk.Button(
                janela,
                text=f" ",
                width=1,
                height=1,
                command=lambda r=row, c=col: unveil(r, c),
            )
            botao.grid(row=row, column=col, padx=1, pady=1)

    janela.mainloop()


def main(size):

    # Screen dimensions
    width = size
    height = size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jogo das bombinhas")

    create_matrix_game(size)
    create_button_grid(size)
    


def board_dimensions(text):
    global size
    size = int(text.split()[0])
    print(size)
    janela.destroy()
    main(size)
    
    #define screen size
janela = tk.Tk()
janela.title("Interface Gráfica em Python")
janela.geometry("500x400")

# Widgets
label_nome = tk.Label(janela, text="Chose the board dimensions:")
label_nome.pack()

botao = tk.Button(janela, text="10 x 10", command=lambda: board_dimensions("10 x 10"))
botao.pack()
botao = tk.Button(janela, text="20 x 20", command=lambda: board_dimensions("20 x 20"))
botao.pack()
botao = tk.Button(janela, text="30 x 30", command=lambda: board_dimensions("30 x 30"))
botao.pack()
botao = tk.Button(janela, text="40 x 40", command=lambda: board_dimensions("40 x 40"))
botao.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Loop da interface
janela.mainloop()


# if __name__ == "__main__":
#    main()
