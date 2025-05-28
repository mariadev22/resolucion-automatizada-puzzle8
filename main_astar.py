import pygame
import time
from utils.puzzle import Board
from ui.display import draw_ui
from agents.a_star_agent import a_star

# Tablero que sí tiene solución
BOARD = [
    [1, 2, 3],
    [8, 4, 0],
    [7, 6, 5]
]

def main():
    # Crear tablero aleatorio
    board = Board()

    # Ejecutar A* para el agente informado
    star_astar = time.perf_counter()
    astar_solution, astar_nodes = a_star(board)
    end_astar = time.perf_counter()

if __name__ == "__main__":
    main()
    