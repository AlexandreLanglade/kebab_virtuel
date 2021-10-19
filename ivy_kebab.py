#!/usr/bin/env/python
# Mon agent ivy en python
from ivy.ivy import IvyServer
import pygame, sys
from pygame.locals import *
    
class KebabAgent(IvyServer):
	def __init__(self, name):
		IvyServer.__init__(self,'KebabAgent')
		self.name = name
		self.start('127.255.255.255:2010')
		self.bind_msg(self.handle_kebab, '^sra5 Parsed=action=(.*) Confidence=(.*) NP=(.*)')
        
	def handle_kebab(self, *arg):
		print('[Agent %s] got an item from %r'%(self.name, arg[0]))
		print(" ----> ",arg[1], ":", arg[2])
		
		if(float(arg[2][2:])>7800000):
			if("viande" in arg[1]):
				self.send_msg('ppilot5 Say= ok viande chef')
				screen.blit(v, (400,100))
			elif("salade" in arg[1]):
				self.send_msg('ppilot5 Say= ok salade chef')
				screen.blit(s, (400,100))
			elif("tomate" in arg[1]):
				self.send_msg('ppilot5 Say= ok tomate chef')
				screen.blit(t, (400,100))
			elif("oignon" in arg[1]):
				self.send_msg('ppilot5 Say= ok oignon chef')
				screen.blit(o, (400,100))
			elif("sauce" in arg[1]):
				self.send_msg('ppilot5 Say= ok sauce chef')
		else:
			self.send_msg('ppilot5 Say= je te met quoi chef')
     


a=KebabAgent('Kababiste')
pygame.init()
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((900,600))

#data

bg=pygame.image.load("data/bgoff.jpg")
v=pygame.image.load("data/viande.png")
s=pygame.image.load("data/salade.png")
t=pygame.image.load("data/tomate.png")
o=pygame.image.load("data/oignon.png")
	
screen.blit(bg, (0,0))
while(True):
	for event in pygame.event.get():
		if(event.type == QUIT):
			# quit() is the opposite of init()
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fps_clock.tick(30)