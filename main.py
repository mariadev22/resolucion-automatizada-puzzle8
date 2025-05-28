import pygame
import time
from utils.puzzle import Board
from ui.display import draw_ui
from agents.bfs_agent import bfs
from agents.a_star_agent import a_star

# Tablero que sí tiene solución
BOARD = [
    [1, 2, 3],
    [8, 4, 0],
    [7, 6, 5]
]

def print_solution(agent_name, solution, elapsed_time, nodes_expanded):
    print(f"\n{agent_name} - Resultados:")
    if solution:
        print(f"  Tiempo de ejecución: {elapsed_time:.3f} segundos")
        print(f"  Nodos expandidos: {nodes_expanded}")
        print(f"  Longitud de la solución: {len(solution) - 1}")
    else:
        print(f"  Tiempo de ejecución: {elapsed_time:.3f} segundos")
        print(f"  Nodos expandidos: {nodes_expanded}")
        print("  Nose encontró solución")

def main():
    # Crear tableros para dos agentes
    board = Board(BOARD)

    print("Tablero inicial:")
    board.display_console()

    # Ejecutar BFS para el agente no informado
    star_bfs = time.perf_counter()
    bfs_solution, bfs_nodes = bfs(board)
    end_bfs = time.perf_counter()
    print_solution("Agente No Informado (BFS)", bfs_solution, end_bfs - star_bfs, bfs_nodes)

    # Ejecutar A* para el agente informado
    star_astar = time.perf_counter()
    astar_solution, astar_nodes = a_star(board)
    end_astar = time.perf_counter()
    print_solution("Agente informado (A*)", astar_solution, end_astar - star_astar, astar_nodes)

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