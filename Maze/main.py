import pygame as pg

def maze():

    pg.init()
    size = (500,400)
    window = pg.display.set_mode(size,pg.RESIZABLE)
    pg.display.update()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    running = False


if __name__ == '__main__':
    maze()