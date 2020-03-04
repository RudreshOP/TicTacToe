import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))

def disp():
    screen.fill((255,255,255))
    pygame.draw.line(screen, (0,0,0), (210,30),(210,570),5)
    pygame.draw.line(screen, (0,0,0), (390,30),(390,570),5)
    pygame.draw.line(screen, (0,0,0), (30,210),(570,210),5)
    pygame.draw.line(screen, (0,0,0), (30,390),(570,390),5)
    for j in range(9):
        if grid[j] == "X":
            draw_X(points[j])
        elif grid[j] == "O":
            draw_O(points[j])
    for i in range(2):
        text = val[i].upper() + " : " + str(scores_x_y[i])
        dispt = font.render(text, False, colors[i])
        screen.blit(dispt, [610, 210 + 120*i])
    pygame.display.flip()

def draw_X(crds):
    pygame.draw.line(screen,(255,0,0),(crds[0]+20,crds[1]+20),(crds[0]+160,crds[1]+160),5)
    pygame.draw.line(screen,(255,0,0),(crds[0]+20,crds[1]+160),(crds[0]+160,crds[1]+20),5)

def draw_O(crds):
    pygame.draw.circle(screen,(0,255,0),(crds[0]+90,crds[1]+90),70,5)

def check(lst):
    status = False
    for each in possibilities:
        crct = 0
        for i in range(3):
            if each[i] in lst:
                crct += 1
        if crct == 3:
            status = True
            break
    return status
                
pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.SysFont("comicsans",100)
possibilities = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
points = [(30,30),(210,30),(390,30),(30,210),(210,210),(390,210),(30,390),(210,390),(390,390)]
scores_x_y = [0,0,0]
val = ["x","o"]
colors = [(255,0,0),(0,255,0)]
main = True

while main:
    running = True
    chances = 0
    grid = ["","","","","","","","",""]
    x = []
    o = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for i in range(9):
                        crd = points[i]
                        if pos[0] in range(crd[0],crd[0]+181) and pos[1] in range(crd[1],crd[1]+181):
                            if grid[i] == "":
                                if chances%2 == 0:
                                    grid[i] = "X"
                                    x.append(i)
                                else:
                                    grid[i] = "O"
                                    o.append(i)
                                chances += 1

        for i in range(2):
            stat = check(eval(val[i]))
            if stat:
                winner = i
                running = False
        if running and chances == 9:
            winner = 2
            running = False
        disp()

    scores_x_y[winner] += 1
    disp()
    if scores_x_y[winner] == 3 and winner != 2:
        main = False
        
pygame.time.delay(3000)