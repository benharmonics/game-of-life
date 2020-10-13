"""settings.py - settings for game of life"""

# colors
black = (0, 0, 0)
white = (255, 255, 255)
smoke = (230, 230, 230)
mustard = (150, 150, 0)
yellow = (220, 220, 0)
turquoise = (41, 217, 230)
dark_blue = (0, 48, 78)
red = (255, 0, 0)
ue_red = (191, 0, 0)
lime_green = (50, 205, 50)
north_texas_green = (5, 144, 51)

# window settings
screen_title = "Conway's Game of Life"
screen_height = 600
screen_width = int(screen_height*16/9)
background_color = turquoise
fps = 60

# cell settings
cell_sidelength = int(screen_height / 54)
cell_color = black
cell_hcolor = ue_red
cell_separation = 1
cell_x0 = 10
cell_y0 = int(screen_height / 58)
cells_per_side = 48
game_board_x_max = int(cell_x0 + cells_per_side * (cell_sidelength + cell_separation) + 1)

# sidebar
sidebar_x0 = game_board_x_max + cell_x0
sidebar_width = screen_width - sidebar_x0

# button and text settings
text_color = white
dropshadow_color = black
highlight_duration = .25
highlight_color = lime_green
title_flash_duration = 3.14
font_size = 30
font = 'freesansbold.ttf'
dropshadow_buffer = 2

clear_button_text = "Clear"
clear_button_color = ue_red
clear_button_hcolor = red
clear_button_height = int(screen_height / 12)
clear_button_width = sidebar_width * 2/5
clear_button_center = [sidebar_x0 + sidebar_width/2, screen_height*.75]
clear_button_text_center = [clear_button_width/2, clear_button_height/2]
clear_button_dropshadow_center = [clear_button_text_center[0] + dropshadow_buffer,
                                  clear_button_text_center[1] + dropshadow_buffer]

save_button_text = "Save"
save_button_color = mustard
save_button_hcolor = yellow
save_button_height = clear_button_height
save_button_width = sidebar_width * .25
save_button_center = [sidebar_x0 + sidebar_width/3, screen_height*.6]
save_button_text_center = [save_button_width/2, save_button_height/2]
save_button_dropshadow_center = [save_button_text_center[0] + dropshadow_buffer,
                                 save_button_text_center[1] + dropshadow_buffer]

reset_button_text = "Reset"
reset_button_color = mustard
reset_button_hcolor = yellow
reset_button_height = clear_button_height
reset_button_width = save_button_width
reset_button_center = [sidebar_x0 + sidebar_width * 2/3, screen_height*.6]
reset_button_text_center = [reset_button_width/2, reset_button_height/2]
reset_button_dropshadow_center = [reset_button_text_center[0] + dropshadow_buffer,
                                  reset_button_text_center[1] + dropshadow_buffer]

control_explanation_font_size = 26
control_explanation_text = 'Hold SPACE to advance'
control_explanation_text_center = [sidebar_x0 + sidebar_width/2, screen_height*.9]
control_explanation_dropshadow_center = [control_explanation_text_center[0] + dropshadow_buffer,
                                         control_explanation_text_center[1] + dropshadow_buffer]

title_text1 = "CONWAY'S"
title_text2 = 'Game of Life'
title_text1_color = dark_blue
title_text1_size = 30
title_text2_size = 60
title_text1_center = [sidebar_x0 + sidebar_width/2 - 60, screen_height*.23]
title_dropshadow1_center = [title_text1_center[0] + dropshadow_buffer,
                            title_text1_center[1] + dropshadow_buffer]
title_text2_center = [sidebar_x0 + sidebar_width/2, screen_height*.3]
title_dropshadow2_center = [title_text2_center[0] + dropshadow_buffer,
                            title_text2_center[1] + dropshadow_buffer]
