import pygame

TILE_SIZE = 100
MARGIN = 5
WIDTH = HEIGHT = TILE_SIZE * 3 + MARGIN * 4
FONT_SIZE = 48
LABEL_FONT_SIZE = 28
METRIC_FONT_SIZE = 24
WHITE = (255, 255, 255)
BG_COLOR = (30, 30, 30)
METRIC_POS_Y = 370

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

def draw_label(screen, label, suffix=""):
    label_font = pygame.font.SysFont(None, LABEL_FONT_SIZE)
    title_label = label_font.render(f"{label} {suffix}", True, WHITE)
    screen.blit(title_label, (10, 20))

def draw_metrics(screen, nodes, steps, elapsed_time):
    metric_font = pygame.font.SysFont(None, METRIC_FONT_SIZE)
    metrics = [f"Nodos: {nodes}", f"Solución: {steps}", f"Tiempo: {elapsed_time:.6f}s"]
    for i, text in enumerate(metrics):
        metric = metric_font.render(text, True, WHITE)
        screen.blit(metric, (10, METRIC_POS_Y + i * 20))

def render_final_state(label, screen, board, nodes, steps, elapsed_time):
    screen.fill(BG_COLOR)
    draw_label(screen, label)
    draw_board(screen, board, offset_x=10, offset_y=50)
    draw_metrics(screen, nodes, steps, elapsed_time)
    pygame.display.flip()

def animate_solution(label, screen, solution, nodes, steps, elapsed_time):
    for state in solution:
        screen.fill(BG_COLOR)
        draw_label(screen, label,  suffix="Resolviendo...")
        draw_board(screen, state.board, offset_x=10, offset_y=50)
        pygame.event.pump()
        pygame.display.flip()
        pygame.time.delay(500)
    render_final_state(label, screen, solution[-1].board, nodes, steps, elapsed_time)

def draw_ui(label, screen, solution, nodes, steps, elapsed_time):
    if solution:
        animate_solution(label, screen, solution, nodes, steps, elapsed_time)
    else:
        render_final_state(label, screen, solution.board, nodes, 0, elapsed_time)