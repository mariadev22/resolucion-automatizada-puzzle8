"""
Calculo de distnacia entre entre un tablero
culaquiera y el tablero objetivo. 

Esta distancia es usada como una heurística
en el algoritmo A* para ayudar a resolver 
el puzzle 8 más eficientemente. 
"""

# Posición de cada número en el tablero objetivo 
GOAL_POSITIONS = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    8: (1, 0), 0: (1, 1), 4: (1, 2),
    7: (2, 0), 6: (2, 1), 5: (2, 2)
}

def manhattan(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value != 0:
                goal_x, goal_y = GOAL_POSITIONS[value]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance