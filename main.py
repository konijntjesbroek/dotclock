import time
from asciimatics.screen import Screen

def demo(screen):
    while(True):
        secs, mins, hours =[int (i) for i in time.strftime("%S %M %H", time.localtime()).split()]
        marker=(' ', '.',':', '\'', '*', '#')
        hmark =(' ', ':', '#')
        line_1 = (secs % 12 *  marker[(secs // 12 + 1)] + (12 - (secs % 12)) * marker[secs // 12])
        line_2 = (mins % 12 *  marker[(mins // 12 + 1)] + (12 - (mins % 12)) * marker[mins // 12]) 
        line_3 = (hours % 12 * hmark[(hours // 12 + 1)] + (12 - (hours % 12)) * hmark[hours // 12]) 
        clock_show = line_1 + '\n\r' + line_2 + '\n\r' + line_3
        
        screen.print_at(clock_show, 0, 0)
        screen.refresh()
        time.sleep(1)
        
Screen.wrapper(demo)
