import pygame as p
from ChessEngine import GameState

HEIGHT = WIDTH = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def load_images():
    for val in ['wP','wB','wN','wR','wQ','wK','bP','bB','bN','bR','bQ','bK']:
        IMAGES[val] = p.transform.scale(p.image.load(f"./images/{val}.png"), (SQ_SIZE,SQ_SIZE))

def draw_game_state(game_state, screen):
    draw_board(screen)
    draw_pieces(game_state.board, screen)

def draw_board(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            tile_color = colors[(r+c)%2]
            p.draw.rect(screen, tile_color,[c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE])

def draw_pieces(board, screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]

            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = GameState()
    load_images()
    running = True
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(gs, screen)
        clock.tick(MAX_FPS)
        p.display.flip()
if __name__ == "__main__":
    main()