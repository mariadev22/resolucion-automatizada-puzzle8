import pygame
import time
from utils.puzzle import Board
from ui.display import draw_ui
from agents.bfs_agent import bfs

# Tablero que sí tiene solución
BOARD = [
    [1, 2, 3],
    [8, 4, 0],
    [7, 6, 5]
]

def main():
    # Crear tableros para dos agentes
    board = Board(BOARD)


    # Ejecutar BFS para el agente no informado
    star_bfs = time.perf_counter()
    bfs_solution, bfs_nodes = bfs(board)
    end_bfs = time.perf_counter()

    # Configurar la ventana de pygame
    pygame.init()
    screen = pygame.display.set_mode((750, 400))
    pygame.display.set_caption("Puzzle 8 - Resolución Automatizada")

    draw_ui(screen, board.board, board.board)

    # Esperar a cerrar la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()