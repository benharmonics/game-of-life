"""objects.py -- sprites and objects for game of life"""

import pygame as pg
from time import time
import settings as s


class Cell(pg.sprite.Sprite):
    """Cell on the game board"""
    def __init__(self, row, col):
        pg.sprite.Sprite.__init__(self)

        self.pos = (row, col)
        self.row = row
        self.col = col

        self.image = pg.Surface([s.cell_sidelength, s.cell_sidelength])
        self.rect = self.image.get_rect()
        self.rect.x = row * (s.cell_sidelength + s.cell_separation) + s.cell_x0
        self.rect.y = col * (s.cell_sidelength + s.cell_separation) + s.cell_y0

        self.neighbors = self.neighbors()

        self.living = False
        self.color = s.cell_color  # "dead" color
        self.hcolor = s.cell_hcolor  # "alive" color

    def neighbors(self):
        neighbors = [
            [self.row - 1, self.col - 1], [self.row - 1, self.col], [self.row - 1, self.col + 1],
            [self.row, self.col - 1],                               [self.row, self.col + 1],
            [self.row + 1, self.col - 1], [self.row + 1, self.col], [self.row + 1, self.col + 1]
        ]
        neighbors_in_bounds = []
        for neighbor in neighbors:
            if not (neighbor[0] < 0 or neighbor[0] > s.cells_per_side - 1):       # row OOB check
                if not (neighbor[1] < 0 or neighbor[1] > s.cells_per_side - 1):   # col OOB check
                    neighbors_in_bounds.append(neighbor)
        return neighbors_in_bounds

    def hover(self, pos):
        x, y = self.rect.x, self.rect.y
        if x < pos[0] < x + s.cell_sidelength and y < pos[1] < y + s.cell_sidelength:
            return True
        else:
            return False

    def click(self, board):
        if not self.living:
            self.living = True
            board[self.row][self.col] = 1
        else:
            self.living = False
            board[self.row][self.col] = 0

    def clear(self):
        self.living = False

    def reset_to_state(self, saved_board):
        self.living = True if saved_board[self.row][self.col] > 0 else False

    def update(self, board, frame_count):
        if frame_count % int(s.fps / 20) == 0:
            living_neighbors = 0
            for neighbor in self.neighbors:
                if board[neighbor[0]][neighbor[1]] > 0:
                    living_neighbors += 1
            if self.living and (living_neighbors > 3 or living_neighbors < 2):
                self.living = False
            if not self.living and living_neighbors == 3:
                self.living = True

    def draw(self, window):
        if self.living:
            self.image.fill(self.hcolor)
        else:
            self.image.fill(self.color)
        window.blit(self.image, self.rect)


class ClearButton(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.time_last_interacted = time() - s.highlight_duration

        self.color = s.clear_button_color
        self.hcolor = s.clear_button_hcolor
        self.fill_color = self.color

        self.font = pg.font.Font(s.font, s.font_size)
        self.text_img = self.font.render(s.clear_button_text, True, s.text_color, None)
        self.text_rect = self.text_img.get_rect()

        self.dropshadow_img = self.font.render(s.clear_button_text, True, s.dropshadow_color, None)
        self.dropshadow_rect = self.dropshadow_img.get_rect()

        self.image = pg.Surface((s.clear_button_width, s.clear_button_height))
        self.rect = self.image.get_rect()

        self.rect.center = s.clear_button_center
        self.text_rect.center = s.clear_button_text_center
        self.dropshadow_rect.center = s.clear_button_dropshadow_center

    def set_highlight(self):
        self.time_last_interacted = time()

    def update(self, pos):
        self.fill_color = self.hcolor if self.hover(pos) else self.color
        if self.time_last_interacted + s.highlight_duration > time():
            self.fill_color = s.highlight_color

    def draw(self, window):
        self.image.fill(self.fill_color)
        self.image.blit(self.dropshadow_img, self.dropshadow_rect)
        self.image.blit(self.text_img, self.text_rect)
        window.blit(self.image, self.rect)

    def hover(self, pos):
        x, y = self.rect.x, self.rect.y
        if x < pos[0] < x + s.clear_button_width and y < pos[1] < y + s.clear_button_height:
            return True
        else:
            return False


class SaveButton(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.time_last_interacted = time() - s.highlight_duration

        self.color = s.save_button_color
        self.hcolor = s.save_button_hcolor
        self.fill_color = self.color

        self.font = pg.font.Font(s.font, s.font_size)
        self.text_img = self.font.render(s.save_button_text, True, s.text_color, None)
        self.text_rect = self.text_img.get_rect()
        self.dropshadow_img = self.font.render(s.save_button_text, True, s.dropshadow_color, None)
        self.dropshadow_rect = self.dropshadow_img.get_rect()

        self.image = pg.Surface((s.save_button_width, s.save_button_height))
        self.rect = self.image.get_rect()

        self.rect.center = s.save_button_center
        self.text_rect.center = s.save_button_text_center
        self.dropshadow_rect.center = s.save_button_dropshadow_center

    def set_highlight(self):
        self.time_last_interacted = time()

    def update(self, pos):
        self.fill_color = self.hcolor if self.hover(pos) else self.color
        if self.time_last_interacted + s.highlight_duration > time():
            self.fill_color = s.highlight_color

    def draw(self, window):
        self.image.fill(self.fill_color)
        self.image.blit(self.dropshadow_img, self.dropshadow_rect)
        self.image.blit(self.text_img, self.text_rect)
        window.blit(self.image, self.rect)

    def hover(self, pos):
        x, y = self.rect.x, self.rect.y
        if x < pos[0] < x + s.save_button_width and y < pos[1] < y + s.save_button_height:
            return True
        else:
            return False


class ResetButton(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.time_last_interacted = time() - s.highlight_duration

        self.color = s.reset_button_color
        self.hcolor = s.reset_button_hcolor
        self.fill_color = self.color

        self.font = pg.font.Font(s.font, s.font_size)
        self.text_img = self.font.render(s.reset_button_text, True, s.text_color, None)
        self.text_rect = self.text_img.get_rect()
        self.dropshadow_img = self.font.render(s.reset_button_text, True, s.dropshadow_color, None)
        self.dropshadow_rect = self.dropshadow_img.get_rect()

        self.image = pg.Surface((s.reset_button_width, s.reset_button_height))
        self.rect = self.image.get_rect()

        self.rect.center = s.reset_button_center
        self.text_rect.center = s.reset_button_text_center
        self.dropshadow_rect.center = s.reset_button_dropshadow_center

    def set_highlight(self):
        self.time_last_interacted = time()

    def update(self, pos):
        self.fill_color = self.hcolor if self.hover(pos) else self.color
        if self.time_last_interacted + s.highlight_duration > time():
            self.fill_color = s.highlight_color

    def draw(self, window):
        self.image.fill(self.fill_color)
        self.image.blit(self.dropshadow_img, self.dropshadow_rect)
        self.image.blit(self.text_img, self.text_rect)
        window.blit(self.image, self.rect)

    def hover(self, pos):
        x, y = self.rect.x, self.rect.y
        if x < pos[0] < x + s.reset_button_width and y < pos[1] < y + s.reset_button_height:
            return True
        else:
            return False

class Text(pg.sprite.Sprite):
    """All non-interactive text, i.e. the title and play instructions"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.time_last_flash = time()

        # controls explanation
        self.font = pg.font.Font(s.font, s.control_explanation_font_size)
        self.text_image = self.font.render(s.control_explanation_text, True, s.text_color, None)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = s.control_explanation_text_center
        self.controls_dropshadow_image1 = self.font.render(s.control_explanation_text, True, s.dropshadow_color, None)
        self.controls_dropshadow_rect1 = self.controls_dropshadow_image1.get_rect()
        self.controls_dropshadow_rect1.center = s.control_explanation_dropshadow_center

        # title 1: "CONWAY'S"
        self.title_font1 = pg.font.Font(s.font, s.title_text1_size)
        self.title_image1 = self.title_font1.render(s.title_text1, True, s.title_text1_color)
        self.title_image1a, self.title_image1b = self.title_image1, self.title_font1.render(s.title_text1, True, s.white)
        self.title_rect1 = self.title_image1.get_rect()
        self.title_rect1.center = s.title_text1_center
        self.dropshadow_image1 = self.title_font1.render(s.title_text1, True, s.black)
        self.dropshadow_rect1 = self.dropshadow_image1.get_rect()
        self.dropshadow_rect1.center = s.title_dropshadow1_center

        # title 2: "Game of Life"
        self.title_font2 = pg.font.Font(s.font, s.title_text2_size)
        self.title_image2 = self.title_font2.render(s.title_text2, True, s.white)
        self.title_image2a, self.title_image2b = self.title_image2, self.title_font2.render(s.title_text2, True, s.dark_blue)
        self.title_rect2 = self.title_image2.get_rect()
        self.title_rect2.center = s.title_text2_center
        self.dropshadow_image2 = self.title_font2.render(s.title_text2, True, s.black)
        self.dropshadow_rect2 = self.dropshadow_image2.get_rect()
        self.dropshadow_rect2.center = s.title_dropshadow2_center

    def flash(self):
        self.title_image1 = self.title_image1b if self.title_image1 == self.title_image1a else self.title_image1a
        self.title_image2 = self.title_image2b if self.title_image2 == self.title_image2a else self.title_image2a
        self.time_last_flash = time()

    def update(self):
        if self.time_last_flash + s.title_flash_duration < time():
            self.flash()

    def draw(self, window):
        window.blit(self.controls_dropshadow_image1, self.controls_dropshadow_rect1)
        window.blit(self.text_image, self.text_rect)
        window.blit(self.dropshadow_image1, self.dropshadow_rect1)
        window.blit(self.title_image1, self.title_rect1)
        window.blit(self.dropshadow_image2, self.dropshadow_rect2)
        window.blit(self.title_image2, self.title_rect2)
