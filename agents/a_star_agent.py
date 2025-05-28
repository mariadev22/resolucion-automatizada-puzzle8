"""
Agente informado: A*

A* es un algoritmo inteligante que encuentra
el camino más corto para llegar de un estado 
inicial al estado meta, utilizando una
heurística (en este caso, la distancia de 
Manhattan).
"""

import heapq
import itertools
from utils.puzzle import Board, GOAL_STATE
from utils.heuristics import manhattan

def a_star(start_board):
    # Tablero que representa la meta
    goal_board = Board(GOAL_STATE)
    # Generador de números únicos
    counter = itertools.count()
    nodes_expanded = 0  

    # Cola de prioridad
    open_set = []
    """
    f=h: ya que g=0 al principio
    g=0: pasos desde el inicio
    star_board: tablero inicial
    []: camino recorrido hasta ahora
    """
    # Tupla: (f, contador, g, board, path)
    heapq.heappush(open_set, (manhattan(start_board.board), 0, next(counter), start_board, []))
    visited_node = set()

    # Explorar nodos
    while open_set:
        est_total_cost, cost_so_far, _, current, path = heapq.heappop(open_set)
        nodes_expanded += 1

        if current == goal_board:
            return path + [current], nodes_expanded # Tiene solución -> ruta + actual

        state_tuple = current.to_tuple()
        if state_tuple in visited_node:
            continue
        visited_node.add(state_tuple)

        # Explorar vecinos
        for neighbor in current.get_neighbors():
            if neighbor.to_tuple() not in visited_node:
                """
                g: aumentamos el costo porque dimos un paso más
                h: calculamos la heurítica
                f=g+h: suma estimada del costo total
                """
                g = cost_so_far + 1
                h = manhattan(neighbor.board)
                f = g + h
                heapq.heappush(open_set, (f, g, next(counter), neighbor, path + [current]))

    return None, nodes_expanded  # No tiene solución