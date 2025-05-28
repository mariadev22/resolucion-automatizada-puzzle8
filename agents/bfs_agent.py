"""
Agente no informado: BFS

Breadth-First Search o Búsqueda en Anchura: Busca 
el camino más corto desde un tablero iicial hasta 
el tablero final (objtivo).
"""

from collections import deque
from utils.puzzle import Board, GOAL_STATE

def bfs(start_board):
    visited_node = set()
    queue = deque([(start_board, [])])  # Nodo raíz
    nodes_expanded = 0

    goal = Board(GOAL_STATE)

    while queue:
        current, path = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            return path + [current], nodes_expanded # Tiene solución -> ruta + actual

        state_tuple = current.to_tuple()
        if state_tuple in visited_node:
            continue

        visited_node.add(state_tuple)

        for neighbor in current.get_neighbors():
            if neighbor.to_tuple() not in visited_node:
                queue.append((neighbor, path + [current]))

    return None, nodes_expanded  # No tiene solución
