import pygame


# Just the drawing function, exported to another file because this file used to have a lot of handlers
# But for the editor you really only need one
def drawScreen(screen, background, levelSlice, textureNames, textures, cursor_coord, selected, screenInfo):
    # Draw the background first
    screen.blit(background, (0, 0))
    for h in range(0, screenInfo[2]):
        for w in range(0, screenInfo[1]):
            if levelSlice[h][w] != 0 and not (w == cursor_coord[0] and h == cursor_coord[1]):
                x_pos = w * screenInfo[0] * screenInfo[3]
                y_pos = h * screenInfo[0] * screenInfo[3]
                screen.blit(textures[textureNames[levelSlice[h][w]]], (x_pos, y_pos))

    # Draw the cursor
    cursor_x = cursor_coord[0] * screenInfo[0] * screenInfo[3]
    cursor_y = cursor_coord[1] * screenInfo[0] * screenInfo[3]
    # Draw what you have selected
    screen.blit(textures[textureNames[selected]], (cursor_x, cursor_y))
    # And draw the cursor
    screen.blit(textures['SelectBox'], (cursor_x, cursor_y))
