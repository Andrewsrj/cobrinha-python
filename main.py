import pygame
import time

pygame.init()
# Tamanho da tela
dis_width = 400
dis_height = 300
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption("Jogo da Cobrinha por Andrews Costa")

# Cor da cobrinha
blue=(0, 0, 255)

# Cor do alimento
red=(255, 0, 0)

# Cor de fundo
black=(40, 40, 40)

# Definição do fim do jogo
game_over=False

# Posição inicial da cobrinha
x1 = dis_width/2
y1 = dis_height/2

snake_block=10

x1_change = 0
y1_change = 0

snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width/2)-100, dis_height/2])

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
    
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(black)
    pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])

    pygame.display.update()

    clock.tick(snake_speed)

message("Fim de jogo!",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()