import pygame

def main():
    #1.创建窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #2.创建一个和窗口一样大小的图片,用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()
    #3.创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")
    """把背景图片放到窗口中显示"""
    while True:
        screen.blit(background,(0,0))
        screen.blit(hero,(210,700))
        pygame.display.update()


if __name__ == "__main__":
    main()
