import pygame

TILE_SIZE = 100
MARGIN = 5
WIDTH = HEIGHT = TILE_SIZE * 3 + MARGIN * 4
FONT_SIZE = 48
LABEL_FONT_SIZE = 28
METRIC_FONT_SIZE = 24

def draw_board(screen, board, offset_x=0, offset_y=0):
    font = pygame.font.SysFont(None, FONT_SIZE)

    for i in range(3):
        for j in range(3):
            value = board[i][j]
            rect = pygame.Rect(
                offset_x + j * TILE_SIZE + MARGIN * (j + 1),
                offset_y + i * TILE_SIZE + MARGIN * (i + 1),
                TILE_SIZE,
                TILE_SIZE
            )
            pygame.draw.rect(screen, (200, 200, 200), rect)
            if value != 0:
                text = font.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

def draw_label(screen, label):
    label_font = pygame.font.SysFont(None, LABEL_FONT_SIZE)

    title_label = label_font.render(f"{label}", True, (255, 255, 255))
    screen.blit(title_label, (10, 20))

def draw_metrics(screen, _nodes, _len, _time):
    metric_font = pygame.font.SysFont(None, METRIC_FONT_SIZE)

    metrics = [
        f"Nodos: {_nodes}",
        f"Solución: {_len}",
        f"Tiempo: {_time:.6f}s"
    ]
    for i, text in enumerate(metrics):
        metric = metric_font.render(text, True, (255, 255, 255))
        screen.blit(metric, (10, 370 + i * 20))

def draw_ui(label, screen, board, _nodes, _len, _time):
    draw_label(screen, label)
    draw_metrics(screen, _nodes, _len, _time)
    draw_board(screen, board, offset_x=10, offset_y=50)
    pygame.display.flip()

def animate_solution(label, screen, solution, _nodes, _len, _time):
    delay=500

    for state in solution:
        screen.fill((30, 30, 30))
        draw_label(screen, label + " Resolviendo...")
        draw_board(screen, state.board, offset_x=10, offset_y=50)
        pygame.event.pump()
        pygame.display.flip()
        pygame.time.delay(delay)

    screen.fill((30, 30, 30))  
    draw_label(screen, label)
    draw_board(screen, solution[-1].board, offset_x=10, offset_y=50)
    draw_metrics(screen, _nodes, _len, _time)
    pygame.display.flip()
    