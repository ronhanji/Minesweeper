import pygame


def draw_text(surf, text, size, x, y, font, color=(255, 255, 255)):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    surf.blit(text_surface, text_rect)

class Cell():
    def __init__(self,color,rect,offset,number,bomb=False):
        self.x=rect[0]
        self.y=rect[1]
        self.width=rect[2]
        self.height=rect[3]
        self.offset=offset
        self.posx=self.x*self.width+self.offset[0]
        self.posy=self.y*self.height+self.offset[1]
        self.rect=[self.posx,self.posy,self.width,self.height]
        self.number=number
        self.color=color
        self.bomb=bomb
        self.font=pygame.font.match_font("Arial")
        self.clicked=False
        self.marked=False

    def draw(self,screen):
        if self.marked:
            pygame.draw.rect(screen,(125,125,125),self.rect)
        if self.clicked:
            if self.bomb:
                pygame.draw.rect(screen,self.color,self.rect)
            elif self.number==0:
                pygame.draw.rect(screen,(0,0,255),self.rect)
            else:
                draw_text(screen,str(self.number),30,self.posx+self.width/2,self.posy+self.height/2,self.font)

        pygame.draw.rect(screen,(255,0,0),self.rect,1)
