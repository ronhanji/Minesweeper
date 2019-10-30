import pygame
import random
import cell

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


WIDTH = 600
HEIGHT = 800
FPS = 30
BGCOLOR = BLACK

w=12
h=16
wi=WIDTH//w
he=HEIGHT//h
while True:
    try:
        num_bombs = int(input("Enter the number of bombs:"))
        break
    except:
        print("Not a Valid integer")
        continue

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
clock = pygame.time.Clock()

cells=[]
for y in range(h):
    t=[]
    for x in range(w):
        t.append(cell.Cell((0,255,0),[x,y,wi,he],(0,0),0))
    cells.append(t)

for i in range(num_bombs):
    x,y=random.randrange(w),random.randrange(h)
    while cells[y][x].bomb:
        x,y=random.randrange(w),random.randrange(h)
    cells[y][x].bomb=True

def num_checker(cells):
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            for y in range(i-1,i+2):
                for x in range(j-1,j+2):
                    if 0<=y<h and 0<=x<w:
                        if cells[y][x].bomb:
                            cells[i][j].number+=1
num_checker(cells)

def zero_checker(j,i):
    for y in range(i-1,i+2):
        for x in range(j-1,j+2):
            if 0<=y<h and 0<=x<w:
                if cells[y][x].bomb==False and cells[y][x].clicked==False:
                    cells[y][x].clicked=True
                    if cells[y][x].number==0:
                        zero_checker(x,y)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mp=pygame.mouse.get_pos()
            cell=cells[mp[1]//he][mp[0]//wi]
            if event.button==3 and cell.clicked==False:
                if cell.marked:
                    cell.marked=False
                    num_bombs+=1
                else:
                    cell.marked=True
                    num_bombs-=1

            elif cell.number==0 and not cell.marked:
                cell.marked=False
                num_bombs+=1
                zero_checker(mp[0]//wi,mp[1]//he)
            else:
                if not cell.marked:
                    cell.clicked=True
                    if cell.bomb:
                        print('Bomb Hit')
                        for i in cells:
                            for j in i:
                                j.clicked = True
            if num_bombs==0:
                print("Win")
                pgame.quit()
    screen.fill(BGCOLOR)
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j].draw(screen)
    pygame.display.flip()

pygame.quit()
