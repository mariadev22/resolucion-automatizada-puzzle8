import pygame

TILE_SIZE = 100
MARGIN = 5
FONT_SIZE = 48
BOARD_GAP = 50  # Espacio entre tableros

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

def draw_ui(screen, board1, board2):
    screen.fill((30, 30, 30))
    draw_board(screen, board1, offset_x=50, offset_y=50)
    draw_board(screen, board2, offset_x=400, offset_y=50)
    pygame.display.flip()