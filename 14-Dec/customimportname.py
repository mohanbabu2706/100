#game.py
#import the draw module
if visual_mode:
    #in visual mode we draw using graphics
    import draw_visual as draw
else:
    #in extual mode,we print out text
    import draw_textual as draw

def main():
    result = play_game()
    #this can eiter visual or textual depending on visual_mode
    draw,draw_game(result)
