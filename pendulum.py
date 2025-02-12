import pygame
import math
import time
import random
import os
from ctypes import POINTER, WINFUNCTYPE, windll
from ctypes.wintypes import BOOL, HWND, RECT
pygame.init()

window = pygame.display.set_mode((1200,600),pygame.RESIZABLE)
window = pygame.display.set_mode((1200,600),pygame.RESIZABLE)

hwnd = pygame.display.get_wm_info()["window"]
prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
paramflags = (1, "hwnd"), (2, "lprect")

GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)
rect = GetWindowRect(hwnd)
print("top, left, bottom, right: ", rect.top, rect.left, rect.bottom, rect.right)

x = rect.left
y = rect.top
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


stampsx = []
stampsy = []
stampspx = []
stampspy = []
r1 = 200
r2 = 200
m1 = 40
m2 = 40
#a1 = math.pi / 2
a1 = random.uniform(0, math.pi * 2)
#a2 = math.pi / 3
a2 = random.uniform(0, math.pi * 2)
a1_v = 0
a2_v = 0
a1_a = 0
a2_a = 0
g = 1
t = 0
px = r2 * math.sin(a2) + (r1 * math.sin(a1) + 600)
py = r2 * math.cos(a2) + (r1 * math.cos(a1) + 50)

mode = 'un'

font = pygame.font.Font('info\\upperercase.ttf', 150)
title1 = font.render('PENDULUM', True, pygame.Color("BLACK"))
mode1 = font.render('Set Mode', True, pygame.Color("BLACK"))
font = pygame.font.Font('info\\upperercase.ttf', 90)
title2 = font.render('SIMULATOR', True, pygame.Color("BLACK"))
font = pygame.font.Font('info\\upperercase.ttf', 30)
title3 = font.render('Press Space To Start', True, pygame.Color("BLACK"))
font = pygame.font.Font('info\\upperercase.ttf', 15)
title4 = font.render('Font By TOM7 or SUCKERPUNCH', True, pygame.Color("BLACK"))
font = pygame.font.Font('info\\upperercase.ttf', 55)
time1 = font.render('TIME:', True, pygame.Color("BLACK"))
time2 = font.render(str(t), True, pygame.Color("BLACK"))

pygame.display.set_caption("Pendulum Simulator")
programIcon = pygame.image.load("info\\icon.png")
OffButton = pygame.image.load("info\\ButtonOff.bmp")
LineButton = pygame.image.load("info\\ButtonLine.bmp")
DottedButton = pygame.image.load("info\\ButtonDotted.bmp")
pygame.display.set_icon(programIcon)

title = True
run = True

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print("hi")
        
        window.blit(self.image, (self.rect.x, self.rect.y))

        return action

while title & run:
    w = pygame.display.get_surface().get_width()
    h = pygame.display.get_surface().get_height()

    if w < 1200:
        window = pygame.display.set_mode((1200,h),pygame.RESIZABLE)
    if h < 600:
        window = pygame.display.set_mode((w,600),pygame.RESIZABLE)
    
    window.fill(pygame.Color("WHITE"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                title = False
    window.blit(title1, pygame.Rect((w/2-title1.get_width()/2), (h/2-title1.get_height()/2)-180, 564, 350))
    window.blit(title2, pygame.Rect((w/2-title2.get_width()/2), (h/2-title2.get_height()/2)-110, 564, 350))
    window.blit(title3, pygame.Rect((w/2-title3.get_width()/2), (h/2-title3.get_height()/2)+150, 564, 350))
    window.blit(title4, pygame.Rect((w/2-title4.get_width()/2), (h/2-title4.get_height()/2)+172, 564, 350))
    pygame.display.update()
while mode == 'un' and run:
    w = pygame.display.get_surface().get_width()
    h = pygame.display.get_surface().get_height()

    if w < 1200:
        window = pygame.display.set_mode((1200,h),pygame.RESIZABLE)
    if h < 600:
        window = pygame.display.set_mode((w,600),pygame.RESIZABLE)
    
    window.fill(pygame.Color("WHITE"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(mode1, pygame.Rect((w/2-mode1.get_width()/2), (h/2-mode1.get_height()/2)-100, 564, 350))
    
    if Button((w/2-DottedButton.get_width()/2)-450, (h/2-DottedButton.get_height()/2)+100, OffButton).draw():
        mode = 'off'
    if Button((w/2-DottedButton.get_width()/2), (h/2-DottedButton.get_height()/2)+100, DottedButton).draw():
        mode = 'dotted'
    if Button((w/2-DottedButton.get_width()/2)+450, (h/2-DottedButton.get_height()/2)+100, LineButton).draw():
        mode = 'line'
    pygame.display.update()

m = 0

while run:
    m += 1
    w = pygame.display.get_surface().get_width()
    h = pygame.display.get_surface().get_height()

    if w < 1200:
        window = pygame.display.set_mode((1200,h),pygame.RESIZABLE)
    if h < 600:
        window = pygame.display.set_mode((w,600),pygame.RESIZABLE)
    
    t += 1
    time2 = font.render(str(t), True, pygame.Color("BLACK"))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if m <= 2147483647:
        window.fill(pygame.Color("WHITE"))
    
    num1a = -g * (2 * m1 + m2) * math.sin(a1)
    num2a = -m2 * g * math.sin(a1-2*a2)
    num3a = -2*math.sin(a1-a2)*m2
    num4a = a2_v*a2_v*r2+a1_v*a1_v*r1*math.cos(a1-a2)
    dena = r1 * (2*m1+m2-m2*math.cos(2*a1-2*a2))

    num1b = 2 * math.sin(a1-a2)
    num2b = (a1_v*a1_v*r1*(m1+m2))
    num3b = g * (m1 + m2) * math.cos(a1)
    num4b = a2_v*a2_v*r2*m2*math.cos(a1-a2)
    denb = r2 * (2*m1+m2-m2*math.cos(2*a1-2*a2))
    
    a1_a = (num1a + num2a + num3a*num4a) / dena
    a2_a = num1b*(num2b+num3b+num4b) / denb
    
    x1 = r1 * math.sin(a1) + (w/2)
    y1 = r1 * math.cos(a1) + 50
    
    x2 = r2 * math.sin(a2) + x1
    y2 = r2 * math.cos(a2) + y1
    
    pygame.draw.line(window, pygame.Color("BLACK"), ((w/2),50), (x1, y1), 2)
    pygame.draw.circle(window, pygame.Color("BLACK"), (x1, y1), m1/2)

    if not mode == 'off':
        stampsx.append(x2)
        stampsy.append(y2)
        if mode == 'line':
            stampspx.append(px)
            stampspy.append(py)
            for i in range(0, len(stampsx)):
                pygame.draw.line(window, pygame.Color("BLACK"), (stampspx[i],stampspy[i]), (stampsx[i],stampsy[i]), 2)
        else:
            for i in range(0, len(stampsx)):
                pygame.draw.circle(window, pygame.Color("BLACK"), (stampsx[i],stampsy[i]), 2)
    pygame.draw.line(window, pygame.Color("BLACK"), (x1,y1), (x2, y2), 2)    
    pygame.draw.circle(window, pygame.Color("BLACK"), (x2, y2), m1/2)

    if not mode == 'off':
        if t > 200:
            stampsx.pop(0)
            stampsy.pop(0)
            if mode == 'line':
                stampspx.pop(0)
                stampspy.pop(0)
    
    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

    a1_v *= 1.0001 #0.9995
    a2_v *= 1.0001 #0.9995
    
    px = x2
    py = y2

    window.blit(time1, pygame.Rect(0, 0, 264, 50))
    window.blit(time2, pygame.Rect(110, 0, 67, 80))

    pygame.display.update()
    time.sleep(0.02)
pygame.quit()
