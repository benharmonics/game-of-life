import pygame as pg
import settings as s
import numpy as np
import objects as obj


def update_board(current_board, all_squares_group):
    for square in all_squares_group:
        current_board[square.row][square.col] = 1 if square.living else 0
    return current_board


pg.init()

window = pg.display.set_mode((s.screen_width, s.screen_height))
pg.display.set_caption(s.screen_title)

frame_count = 0
clock = pg.time.Clock()
entry_mode = False
saved_board = None

all_cells = pg.sprite.Group()
selected_cell = None
board = np.zeros((s.cells_per_side, s.cells_per_side))
for i in range(s.cells_per_side):
    for j in range(s.cells_per_side):
        all_cells.add(obj.Cell(row=i, col=j))

all_buttons = pg.sprite.Group()
all_buttons.add(obj.ClearButton())
all_buttons.add(obj.SaveButton())
all_buttons.add(obj.ResetButton())
text = obj.Text()

run = True
while run:
    clock.tick(s.fps)
    frame_count += 1
    pos = pg.mouse.get_pos()
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and pos[0] > s.game_board_x_max:  # checking button collision
            for button in all_buttons:
                if button.hover(pos) and isinstance(button, obj.ClearButton):
                    for cell in all_cells:
                        cell.clear()
                    board = update_board(board, all_cells)
                    button.set_highlight()
                if button.hover(pos) and isinstance(button, obj.SaveButton):
                    saved_board = np.array(board)
                    button.set_highlight()
                if button.hover(pos) and isinstance(button, obj.ResetButton):
                    try:
                        for cell in all_cells:
                            cell = cell.reset_to_state(saved_board)
                        board = update_board(board, all_cells)
                        button.set_highlight()
                    except:
                        print('No board saved to revert back to')
        if event.type == pg.MOUSEBUTTONDOWN and not keys[pg.K_SPACE] and pos[0] < s.game_board_x_max:
            # only enter entry mode if you're over the board & not updating the board simultaneously
            entry_mode = True
        if event.type == pg.MOUSEBUTTONUP:
            entry_mode = False
            selected_cell = None
        if event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:  # clearing
            for cell in all_cells:
                cell.clear()
            board = update_board(board, all_cells)
        if event.type == pg.KEYDOWN and event.key == pg.K_s:  # saving a board
            saved_board = np.array(board)
        if event.type == pg.KEYDOWN and event.key == pg.K_r:  # reverting to a saved board
            try:
                for cell in all_cells:
                    cell = cell.reset_to_state(saved_board)
                board = update_board(board, all_cells)
            except:
                print('No board saved to revert back to')

    if entry_mode:  # click square if hovering over it
        for cell in all_cells:
            if cell.hover(pos) and cell != selected_cell:
                cell.click(board)
                selected_cell = cell

    # updating
    if keys[pg.K_SPACE]:  # update squares by holding spacebar
        all_cells.update(board, frame_count)  # first update squares using old board layout
        board = update_board(board, all_cells)  # then update board using new squares layout
    all_buttons.update(pos)

    # drawing
    window.fill(s.background_color)
    for cell in all_cells:
        cell.draw(window)
    for button in all_buttons:
        button.draw(window)
    text.update()
    text.draw(window)
    pg.display.flip()

pg.quit()
