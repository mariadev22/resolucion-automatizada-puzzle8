import pygame
import time
from utils.puzzle import Board
from ui.display import draw_ui, animate_solution
from agents.a_star_agent import a_star

# Tablero que sí tiene solución
BOARD = [
    [1, 2, 3],
    [8, 4, 5],
    [7, 0, 6]
]

def main():
    # Crear tablero aleatorio
    board = Board(BOARD)

    # Ejecutar A* para el agente informado
    star_astar = time.perf_counter()
    astar_solution, astar_nodes = a_star(board)
    end_astar = time.perf_counter()

    # Configurar la ventana de pygame
    pygame.init()
    screen = pygame.display.set_mode((350, 450))
    pygame.display.set_caption("Puzzle 8 - Resolución Automatizada")

    if astar_solution:
        animate_solution(
            "Agente A*", 
            screen, 
            astar_solution,
            astar_nodes,
            len(astar_solution) - 1,
            end_astar - star_astar
        )
    else:
        draw_ui(
            "Agente A*", 
            screen, 
            board.board, 
            astar_nodes, 
            0, 
            end_astar - star_astar
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
    