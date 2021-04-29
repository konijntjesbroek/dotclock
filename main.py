import time
from asciimatics.screen import Screen

def demo(screen):
    while(True):
        secs, mins, hours =[int (i) for i in time.strftime("%S %M %H", time.localtime()).split()]
        mark = '#'
        shades = (0, 22, 28, 34, 40) 
        line_1 = (secs // 5) * mark
        line_2 = (mins // 5) * mark
        line_3 = (hours % 12) * mark
        am_line = (12 - (hours % 12)) * mark

        screen.clear_buffer(255, 0, 0) 
        screen.print_at(line_1, 0, 0, 46)
        screen.print_at(mark, (secs // 5), 0, shades[secs % 5])
        screen.print_at(line_2, 0, 1, 46)
        screen.print_at(mark, (mins // 5), 1, shades[mins % 5])
        if ( hours < 12):
            screen.print_at(line_3, 0, 2, shades[2])
        else:
            screen.print_at(line_3, 0, 2, 46)
            screen.print_at(am_line, hours % 12, 2, shades[2])
        
        screen.refresh()
        time.sleep(1)
        
Screen.wrapper(demo)
