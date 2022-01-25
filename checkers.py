import sys

import pygame

from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = WIDTH
square_size = WIDTH // 8

pygame.display.set_caption("Checkers")

black = pygame.transform.scale(pygame.image.load("chess/checkers-final/black.png"), (square_size, square_size))
white = pygame.transform.scale(pygame.image.load("chess/checkers-final/white.png"), (square_size, square_size))
black_q = pygame.transform.scale(pygame.image.load("chess/checkers-final/black_q.png"), (square_size, square_size))
white_q = pygame.transform.scale(pygame.image.load("chess/checkers-final/white_q.png"), (square_size, square_size))

## The plan of the board, b for black piece, w for white piece
boardState = [
    ["-", "b", "-", "b", "-", "b", "-", "b"],
    ["b", "-", "b", "-", "b", "-", "b", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "w", "-", "w", "-", "w", "-", "w"],
    ["w", "-", "w", "-", "w", "-", "w", "-"],
]


def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(pygame.Color((245, 222, 179)))
    selected = ()
    clicks = []
    onMove = True
    onDiagonal = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // 100
                row = location[1] // 100
                # print(col, row)
                if selected == (row, col):
                    selected = ()
                    clicks = []
                else:
                    selected = (row, col)
                    clicks.append(selected)
                    selected = ()

            if len(clicks) == 2:
                # print(clicks)
                movingPiece = boardState[clicks[0][0]][clicks[0][1]]
                if movingPiece == "b" and onMove != True:
                    if clicks[1][0] == clicks[0][0] + 1 and (clicks[1][1] == clicks[0][1] + 1 or clicks[1][1] == clicks[0][1] - 1):
                        if boardState[clicks[1][0]][clicks[1][1]] == "b" or boardState[clicks[1][0]][clicks[1][1]] == "w":
                            pass
                        if boardState[clicks[1][0]][clicks[1][1]] == "bq" or boardState[clicks[1][0]][clicks[1][1]] == "wq":
                            pass
                        elif boardState[clicks[1][0]][clicks[1][1]] == "-":
                            boardState[clicks[0][0]][clicks[0][1]] = "-"
                            boardState[clicks[1][0]][clicks[1][1]] = movingPiece
                            onMove = True

                    elif clicks[1][0] == clicks[0][0] + 2 and (clicks[1][1] == clicks[0][1] + 2 or clicks[1][1] == clicks[0][1] - 2):
                        if (boardState[clicks[1][0] - 1][clicks[1][1] - 1] == "w" or boardState[clicks[1][0] - 1][clicks[1][1] - 1] == "wq") and boardState[clicks[1][0]][clicks[1][1]] == "-" and clicks[1][1] > clicks[0][1]:
                            boardState[clicks[0][0]][clicks[0][1]] = "-"
                            boardState[clicks[1][0] - 1][clicks[1][1] - 1] = "-"
                            boardState[clicks[1][0]][clicks[1][1]] = movingPiece
                            onMove = True
                        elif (boardState[clicks[1][0] - 1][clicks[1][1] + 1] == "w" or boardState[clicks[1][0] - 1][clicks[1][1] + 1] == "wq") and boardState[clicks[1][0]][clicks[1][1]] == "-":
                            boardState[clicks[0][0]][clicks[0][1]] = "-"
                            boardState[clicks[1][0] - 1][clicks[1][1] + 1] = "-"
                            boardState[clicks[1][0]][clicks[1][1]] = movingPiece
                            onMove = True
                        else:
                            pass
                    else:
                        pass

                elif movingPiece == "w" and onMove == True:
                    if clicks[1][0] == clicks[0][0] - 1 and (clicks[1][1] == clicks[0][1] + 1 or clicks[1][1] == clicks[0][1] - 1):
                        if boardState[clicks[1][0]][clicks[1][1]] == "b" or boardState[clicks[1][0]][clicks[1][1]] == "w":
                            pass
                        if boardState[clicks[1][0]][clicks[1][1]] == "bq" or boardState[clicks[1][0]][clicks[1][1]] == "wq":
                            pass
                        elif boardState[clicks[1][0]][clicks[1][1]] == "-":
                            boardState[clicks[0][0]][clicks[0][1]] = "-"
                            boardState[clicks[1][0]][clicks[1][1]] = movingPiece
                            onMove = False

                    elif clicks[1][0] == clicks[0][0] - 2 and (clicks[1][1] == clicks[0][1] + 2 or clicks[1][1] == clicks[0][1] - 2):
                        if (boardState[clicks[1][0] + 1][clicks[1][1] - 1] == "b" or boardState[clicks[1][0] + 1][clicks[1][1] - 1] == "bq") and boardState[clicks[1][0]][clicks[1][1]] == "-" and clicks[1][1] > clicks[0][1]:
                            boardState[clicks[0][0]][clicks[0][1]] = "-"
                            boardState[clicks[1][0] + 1][clicks[1][1] - 1] = "-"
                            boardState[clicks[1][0]][clicks[1][1]] = movingPiece
                            onMove = False
                        elif (boardState[clicks[1][0] + 1][clicks[1][1] + 1] == "b" or boardState[clicks[1][0] + 1][clicks[1][1] + 1] == "bq") and boardState[clicks[1][0]][clicks[1][1]] == "-":
                            boardState[clicks[0][0]][clicks[0][1]] = "-"
                            boardState[clicks[1][0] + 1][clicks[1][1] + 1] = "-"
                            boardState[clicks[1][0]][clicks[1][1]] = movingPiece
                            onMove = False
                        else:
                            pass
                    else:
                        pass

                elif movingPiece == "bq" and onMove != True:
                    if abs(clicks[0][0] - clicks[1][0]) == abs(clicks[0][1] - clicks[1][1]) and boardState[clicks[1][0]][clicks[1][1]] == "-":
                            onDiagonal = True
                    else:
                            onDiagonal = False
                            
                    if onDiagonal:
                        boardState[clicks[0][0]][clicks[0][1]] = "-"
                        boardState[clicks[1][0]][clicks[1][1]] = movingPiece
                        onMove = True

                elif movingPiece == "wq" and onMove == True:
                    if abs(clicks[0][0] - clicks[1][0]) == abs(clicks[0][1] - clicks[1][1]) and boardState[clicks[1][0]][clicks[1][1]] == "-":
                            onDiagonal = True
                    else:
                            onDiagonal = False
                            
                    if onDiagonal:
                        boardState[clicks[0][0]][clicks[0][1]] = "-"
                        boardState[clicks[1][0]][clicks[1][1]] = movingPiece
                        onMove = False
                            

                for i in range(8):
                    if boardState[0][i] == "w":
                        boardState[0][i] = "wq"
                    if boardState[7][i] == "b":
                        boardState[7][i] = "bq"

                wS = 0
                bS = 0

                for i in range(8):
                    for j in range(8):
                        if boardState[i][j] == "w" or boardState[i][j] == "wq":
                            wS += 1
                        elif boardState[i][j] == "b" or boardState[i][j] == "bq":
                            bS += 1

                if wS == 0 or bS == 0:
                    return
                
                selected = ()
                clicks = []
                
                
        drawBoard(window)
        drawPieces(window, boardState)
        pygame.display.flip()

def drawBoard(window):
    for row in range(8):
        for col in range(8):
            if row%2 == 0:
                if col%2 != 0:
                    pygame.draw.rect(window, (160, 82, 45), pygame.Rect(col*square_size, row*square_size, square_size, square_size))
                else:
                    pygame.draw.rect(window, (245, 222, 179), pygame.Rect(col*square_size, row*square_size, square_size, square_size))
            else:
                if col%2 == 0:
                    pygame.draw.rect(window, (160, 82, 45), pygame.Rect(col*square_size, row*square_size, square_size, square_size))
                else:
                    pygame.draw.rect(window, (245, 222, 179), pygame.Rect(col*square_size, row*square_size, square_size, square_size))

def drawPieces(window, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == "b":
                window.blit(black, pygame.Rect(col*square_size, row*square_size, square_size, square_size))
            elif piece == "w":
                window.blit(white, pygame.Rect(col*square_size, row*square_size, square_size, square_size))
            elif piece == "bq":
                window.blit(black_q, pygame.Rect(col*square_size, row*square_size, square_size, square_size))
            elif piece == "wq":
                window.blit(white_q, pygame.Rect(col*square_size, row*square_size, square_size, square_size))

if __name__ == "__main__":
    main()