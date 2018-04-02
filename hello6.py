import pygame

class Ball(pygame.sprite.Sprite):
	def_init_(self, x, y, xdir, ydir, speed):
		pygame.sprite.Sprite._init_(self)
		self.image = pygame.Surface([20,20])
		self.image.fill(pygame.Color(255,255,255))
		pygame.draw.circle(self.image, pygame.Color(255,0,0),(10,10), 10, 0)
		self.rect = self.image.get_rect()
		self.x, self.y = x,y
		self.xdir, self.ydir = xdir, ydir
		self.speed = speed
	def update(self):
		self.x = self.x + (self.xdir * self.speed)
		self.y = self.y + (self.ydir * self.speed)
		if(self.x<10) | (self.x > 490):
			self.xdir = self.xdir * -1
		if(self.y<10 | (self.y > 490):
			self.ydir = self.ydir * -1

		self.rect.center = (self.x,self.y)
		pygame.init()
		fps=pygame.time.Clock()
		window=pygame.display.set_mode((500,500))
		ball1=Ball(100,250,1,1,5)
		ball2=Ball(400,10,-1,-1,8)

		While True:
			ball1.update()
			ball2.update()
			window.fill(pygame.Color(255,255,255))
			window.blit(ball1,image,ball1,rect)
			window.blit(ball2,image,ball2,rect)
			pygame.display.update()
			fps.tick(30)

