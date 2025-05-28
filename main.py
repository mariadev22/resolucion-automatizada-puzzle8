import pygame
from utils.puzzle import Board
from ui.display import draw_ui
from agents.bfs_agent import bfs

def print_solution(solution, title):
    print(f"\n{title} (pasos: {len(solution) - 1})")
    for i, step in enumerate(solution):
        print(f"\nPaso {i}")
        step.display_console() 

def main():
    # Crear tableros para dos agentes
    board1 = Board()
    board2 = Board()

    print("Agente NO informado - Tablero:")
    board1.display_console()

    # Ejecutar BFS para el agente no informado
    solution = bfs(board1)
    if solution:
        print_solution(solution, "Agente No Informado (BFS)")
    else:
        print("\nNo se encotró solución.") 

    print("\nAgente INFORMADO - Tablero:")
    board2.display_console()

    # Configurar la ventana de pygame
    pygame.init()
    screen = pygame.display.set_mode((750, 400))
    pygame.display.set_caption("Puzzle 8 - Resolución Automatizada")

    draw_ui(screen, board1.board, board2.board)

    # Esperar a cerrar la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()