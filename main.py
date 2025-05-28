import pygame
from utils.puzzle import Board
from ui.display import draw_ui
from agents.bfs_agent import bfs
from agents.a_star_agent import a_star

def print_solution(solution, title):
    print(f"\n{title} (pasos: {len(solution) - 1})")
    for i, step in enumerate(solution):
        print(f"\nPaso {i}")
        step.display_console() 

def main():
    # Crear tableros para dos agentes
    board_bfs = Board()
    board_astar = Board(board_bfs.board) # Copia exacta para comparar

    print("Tablero inicial:")
    board_bfs.display_console()

    # Ejecutar BFS para el agente no informado
    solution_bfs = bfs(board_bfs)
    if solution_bfs:
        print_solution(solution_bfs, "Agente No Informado (BFS)")
    else:
        print("\nBFS: No se encotró solución.") 

    # Ejecutar A* para el agente informado
    solution_astar = a_star(board_astar)
    if solution_astar:
        print_solution(solution_astar, "Agente informado (A*)")
    else:
        print("\nA*: No se encontro solución.")

    # Configurar la ventana de pygame
    pygame.init()
    screen = pygame.display.set_mode((750, 400))
    pygame.display.set_caption("Puzzle 8 - Resolución Automatizada")

    draw_ui(screen, board_bfs.board, board_astar.board)

    # Esperar a cerrar la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()