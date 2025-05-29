import pygame
import time
from utils.puzzle import Board
from ui.display import draw_ui, animate_solution
from agents.bfs_agent import bfs

# Tablero que sí tiene solución
BOARD = [
    [1, 2, 3],
    [8, 4, 5],
    [7, 0, 6]
]

def main():
    # Crear tablero aleatorio
    board = Board(BOARD)


    # Ejecutar BFS para el agente no informado
    star_bfs = time.perf_counter()
    bfs_solution, bfs_nodes = bfs(board)
    end_bfs = time.perf_counter()

    # Configurar la ventana de pygame
    pygame.init()
    screen = pygame.display.set_mode((350, 450))
    pygame.display.set_caption("Puzzle 8 - Resolución Automatizada")

    if bfs_solution:
        animate_solution(
            "Agente BFS", 
            screen, 
            bfs_solution,
            bfs_nodes,
            len(bfs_solution) - 1,
            end_bfs - star_bfs
        )
    else:
        draw_ui(
            "Agente BFS", 
            screen, 
            board.board, 
            bfs_nodes, 
            0, 
            end_bfs - star_bfs
        )
    

    # Esperar a cerrar la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()