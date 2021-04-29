import time
from asciimatics.screen import Screen

def demo(screen):
    secs, mins, hours =time.strftime("%S %M %H", time.localtime()).split()
    screen.print_at('*' * int(secs), 0, 0)
    screen.print_at('*' * int(mins), 0, 1)
    screen.print_at('*' * int(hours), 0, 2)
    screen.refresh()
    time.sleep(1)
    
while(True):    
    Screen.wrapper(demo)