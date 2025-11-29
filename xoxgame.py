import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

BG_COLOR = (255, 255, 255)
GRID_COLOR = (50, 50, 50)
P1_COLOR = (0, 0, 255)
P2_COLOR = (255, 0, 0)
UI_BG = (220, 220, 220)

cell_size = 200
game_grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

current_turn = "X"
game_over = False
winning_line = []

big_font = pygame.font.SysFont('arial', 80, bold=True)
ui_font = pygame.font.SysFont('arial', 30)

scores = {"X": 0, "O": 0}

def draw_interface():
    screen.fill(BG_COLOR)
    
    pygame.draw.line(screen, GRID_COLOR, (cell_size, 0), (cell_size, 600), 5)
    pygame.draw.line(screen, GRID_COLOR, (cell_size * 2, 0), (cell_size * 2, 600), 5)
    
    pygame.draw.line(screen, GRID_COLOR, (0, cell_size), (600, cell_size), 5)
    pygame.draw.line(screen, GRID_COLOR, (0, cell_size * 2), (600, cell_size * 2), 5)

    for r in range(3):
        for c in range(3):
            mark = game_grid[r][c]
            if mark:
                color = P1_COLOR if mark == "X" else P2_COLOR
                text_surf = big_font.render(mark, True, color)
                text_rect = text_surf.get_rect(center=(c * cell_size + 100, r * cell_size + 100))
                screen.blit(text_surf, text_rect)

    pygame.draw.rect(screen, UI_BG, (0, 600, 600, 100))
    
    score_msg = f"Score | X: {scores['X']}   O: {scores['O']}"
    score_surf = ui_font.render(score_msg, True, (0,0,0))
    screen.blit(score_surf, (20, 635))

    btn_rect = pygame.Rect(400, 620, 180, 60)
    pygame.draw.rect(screen, (180, 180, 180), btn_rect)
    pygame.draw.rect(screen, (0,0,0), btn_rect, 2)
    
    restart_text = ui_font.render("Reset", True, (0,0,0))
    text_rect = restart_text.get_rect(center=btn_rect.center)
    screen.blit(restart_text, text_rect)

    return btn_rect

def check_for_win():
    global winning_line
    
    for row in range(3):
        if game_grid[row][0] == game_grid[row][1] == game_grid[row][2] and game_grid[row][0] is not None:
            winning_line = [(row, 0), (row, 1), (row, 2)]
            return game_grid[row][0]

    for col in range(3):
        if game_grid[0][col] == game_grid[1][col] == game_grid[2][col] and game_grid[0][col] is not None:
            winning_line = [(0, col), (1, col), (2, col)]
            return game_grid[0][col]

    if game_grid[0][0] == game_grid[1][1] == game_grid[2][2] and game_grid[0][0] is not None:
        winning_line = [(0, 0), (1, 1), (2, 2)]
        return game_grid[0][0]
        
    if game_grid[0][2] == game_grid[1][1] == game_grid[2][0] and game_grid[0][2] is not None:
        winning_line = [(0, 2), (1, 1), (2, 0)]
        return game_grid[0][2]

    return None

def draw_win_line():
    if winning_line:
        start = winning_line[0]
        end = winning_line[2]
        
        start_pos = (start[1] * cell_size + 100, start[0] * cell_size + 100)
        end_pos = (end[1] * cell_size + 100, end[0] * cell_size + 100)
        
        pygame.draw.line(screen, (0, 255, 0), start_pos, end_pos, 10)

def reset_game_state():
    global game_grid, current_turn, winning_line, game_over
    game_grid = [[None]*3 for _ in range(3)]
    current_turn = "X"
    winning_line = []
    game_over = False

running = True
result_msg = ""

while running:
    restart_btn_rect = draw_interface()
    
    if winning_line:
        draw_win_line()
        
    empty_cells = sum(row.count(None) for row in game_grid)
    if not empty_cells and not winning_line:
        game_over = True
        result_msg = "Draw!"
    elif winning_line:
        game_over = True
        if not result_msg: 
             winner = "O" if current_turn == "X" else "X"
             result_msg = f"{winner} Wins!"

    if game_over:
        msg_surf = ui_font.render(result_msg, True, (0, 100, 0))
        screen.blit(msg_surf, (220, 635))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            if restart_btn_rect.collidepoint((mx, my)):
                reset_game_state()
                result_msg = ""
                
            elif my < 600 and not game_over:
                col = mx // cell_size
                row = my // cell_size
                
                if game_grid[row][col] is None:
                    game_grid[row][col] = current_turn
                    
                    winner = check_for_win()
                    if winner:
                        scores[winner] += 1
                        result_msg = f"{winner} Wins!"
                        game_over = True
                    
                    current_turn = "O" if current_turn == "X" else "X"

    clock.tick(60)