import pygame
import time
from multiprocessing import Process
from utils.puzzle import Board
from ui.display import draw_ui
from agents.bfs_agent import bfs
from agents.a_star_agent import a_star

def pygame_init():
    # Configurar la ventana de pygame
    pygame.init()
    screen = pygame.display.set_mode((350, 450))
    pygame.display.set_caption("Puzzle 8")
    return screen

def pygame_quit():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

def run_bfs(board):
    # Configurar la ventana de pygame
    screen = pygame_init()

    # Ejecutar BFS para el agente no informado
    star_bfs = time.perf_counter()
    bfs_solution, bfs_nodes = bfs(board)
    end_bfs = time.perf_counter()

    draw_ui(
        "Agente BFS", 
        screen, 
        bfs_solution, 
        bfs_nodes, 
        len(bfs_solution) - 1, 
        end_bfs - star_bfs
    )

    # Esperar a cerrar la ventana
    pygame_quit()

def run_astar(board):
    # Configurar la ventana de pygame
    screen = pygame_init()

    # Ejecutar A* para el agente informado
    star_astar = time.perf_counter()
    astar_solution, astar_nodes = a_star(board)
    end_astar = time.perf_counter()

    draw_ui(
        "Agente A*", 
        screen, 
        astar_solution, 
        astar_nodes, 
        len(astar_solution) - 1, 
        end_astar - star_astar
    )

    # Esperar a cerrar la ventana
    pygame_quit()


def main():
    # Crear tablero aleatorio
    board = Board()

    board.display_console()

    # Crea procesos para BFS y A*
    bfs_process = Process(target=run_bfs, args=(board,))
    astar_process = Process(target=run_astar, args=(board,))

    # Inicia ambos procesos
    bfs_process.start()
    astar_process.start()

    # Espera a que terminen
    bfs_process.join()
    astar_process.join()

if __name__ == "__main__":
    main()