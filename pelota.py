import pygame, sys,  random

class pelota:
    def __init__(self, ventana, x, y):
        self.ventana = ventana
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pygame.draw.circle(self.ventana, (r, g, b), (self.x, self.y), 10, 0)
        
    def mover(self):
        self.x += self.vx
        self.y += self.vy


def refrescar(ventana):
    ventana.fill((0, 0, 0))
    bola.dibujar()
    text = font.render(str(golpes), True, ((255, 255, 255)))
    
    text_rect = text.get_rect()
    text_rect.centerx = 100
    ventana.blit(text, text_rect)

def main():
    global bola, golpes, font, r, g, b
    ventana = pygame.display.set_mode((600, 400))
    ventana.fill((0, 0, 0))
    bola = pelota(ventana, 50, 100)
    bola.vx = 0.5
    bola.vy = 0.2
    golpes = 0
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pygame.font.init()
    font = pygame.font.SysFont("Courier", 30)
    pygame.display.set_caption("Pelota")
    jugar = True
    while jugar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugar = False
        pygame.time.delay(2)
        bola.mover()
        if bola.x >= 590:
            bola.vx *= -1
            bola.x = 590
            golpes += 1
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
        if bola.x <= 0:
            bola.vx *= -1
            bola.x = 0
            golpes += 1
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
        if bola.y >= 390:
            bola.vy *= -1
            bola.y = 390
            golpes += 1
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
        if bola.y <= 0:
            bola.vy *= -1
            bola.y = 0
            golpes += 1
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
        refrescar(ventana)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
