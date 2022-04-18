import pygame
import sys
import numpy

pygame.init()

WIDTH = 300
HEIGHT = 300
BG_COLOR = (20, 189, 172)
LINE_COLOR = (13, 161, 146)
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (255, 255, 255)
CROSS_WIDTH = 25
CROSS_SPACE = SQUARE_SIZE // 4
CROSS_COLOR = (84, 84, 84)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Need to make constants later
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

player = 1
gameover = False

# board
board = numpy.zeros((BOARD_ROWS, BOARD_COLS))

def mark_square(row, col, player):
    board[row][col] = player

def square_is_avaliable(row, col):
    return board[row][col] == 0

def board_is_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True            

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR, (row * SQUARE_SIZE + CROSS_SPACE, col * SQUARE_SIZE + SQUARE_SIZE - CROSS_SPACE), (row * SQUARE_SIZE + SQUARE_SIZE - CROSS_SPACE, col * SQUARE_SIZE + CROSS_SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (row * SQUARE_SIZE + CROSS_SPACE, col * SQUARE_SIZE + CROSS_SPACE), (row * SQUARE_SIZE + SQUARE_SIZE - CROSS_SPACE, col * SQUARE_SIZE + SQUARE_SIZE - CROSS_SPACE), CROSS_WIDTH)

            if board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (row * SQUARE_SIZE + SQUARE_SIZE // 2, col * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)

def check_win(player):
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True        

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False    

def draw_horizontal_winning_line(row, player):
    pos_x = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen, color, (pos_x, 15), (pos_x, HEIGHT - 15), 15)    

def draw_vertical_winning_line(col, player):
    pos_y = col * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen, color, (15, pos_y), (WIDTH - 15, pos_y), 15)  

def draw_asc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15) 

def draw_desc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15) 

def restart():
    global player, gameover
    screen.fill(BG_COLOR)
    draw_playground()
    player = 1
    gameover = False
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

def draw_playground():
    line_pos = [
        ((0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE)),
        ((0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2)),
        ((SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT)),
        ((SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, HEIGHT)),
    ]

    for pos in line_pos:
        pygame.draw.line(screen, LINE_COLOR, pos[0], pos[1], LINE_WIDTH)

draw_playground()

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            mouse_x = event.pos[0] 
            mouse_y = event.pos[1]

            clicked_row = mouse_x // SQUARE_SIZE
            clicked_col = mouse_y // SQUARE_SIZE

            # print(clicked_row)
            # print(clicked_col)

            if square_is_avaliable(clicked_row, clicked_col):   
                mark_square(clicked_row, clicked_col, player)
                draw_figures()  
                if check_win(player):
                    gameover = True
                if player == 1:
                    player = 2
                else:
                    player = 1 

            # print(board)  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart() 

    pygame.display.update()        