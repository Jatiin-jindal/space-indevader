import pygame , random , math
pygame.init()

def isCollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt(math.pow(enemyx-bulletx,2) + math.pow(enemyy-bullety,2))
    if distance < 37:
        return True
    else:
        return False

    
over_font = pygame.font.Font(None,54)
def game_over():
    render = over_font.render(f"Game Over And Score Is {score}",True,(0,255,0))
    window.blit(render,(90,300))
# SCORE FUNCTION
def show_score():
    render = font.render(f"SCORE IS {score}",True,(255,0,0))
    window.blit(render,(50,50))
    
# SHOWING TEXT ON WINDOW
font = pygame.font.Font(None,34)

score = 0
    
window = pygame.display.set_mode((800 , 600))
shipx = 350
shipy = 500
bullety = 450
bullet_fire = False
background = pygame.image.load("space_indevader1/background.png")
space_ship = pygame.image.load("space_indevader1/player.png")
   
enemy = []
enemyx = []
enemyy = []
enemyMovement = []
number = 5
for i in range(number):
    enemy.append(pygame.image.load("space_indevader1/enemy (2).png"))
    enemyx.append(random.randint(10 , 490))
    enemyy.append(random.randint(10 , 150))
    enemyMovement.append( 5)

bulletx = shipx
bullet = pygame.image.load("space_indevader1/bullet.png")
playerMovement = 0
while True:
    window.blit(background,(0 , 0)) 
    show_score()
    for event in pygame.event.get():
        if event.type == pygame.quit:
            window.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerMovement -=5
            if event.key == pygame.K_SPACE:
                bullet_fire = True
            if event.key == pygame.K_RIGHT:
                playerMovement +=5
        if event.type == pygame.KEYUP:
            playerMovement = 0
    shipx += playerMovement
    if shipx <= 0: 
        shipx = 0
    if shipx >= 736:
        shipx = 736
    for i in range(number):
        if enemyy[i] >= 436:
            for j in range(number):
                enemyy[j] = 2000
            game_over()
            break
        if enemyx[i] <= 0:
            enemyMovement[i] = 7
            enemyy[i] += 10
        if enemyx[i] >= 736:
            enemyMovement[i] = -7
            enemyy[i] += 10
        enemyx[i] += enemyMovement[i]
        collided = isCollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collided:
            score += 100
            enemyx[i] = random.randint(10,490)
        window.blit(enemy[i],(enemyx[i] , enemyy[i]))
    if bullet_fire:
        bullety -= 15
        if bullety <= 0:
            bulletx = shipx
            bullet_fire = False
        window.blit(bullet,(bulletx , bullety))
    window.blit(space_ship,(shipx , shipy))
    
    if not bullet_fire:
        bullety = 500
        bulletx = shipx
    pygame.display.update()
    


