import pygame

class Ship:
	def __init__(self, screen):
		"""Initialize the ship and set its starting position."""

		# Load the ship image and get its rect.
		self.screen  	 = screen
		self.image   	 = pygame.image.load('images/ship.bmp')
		self.rect    	 = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom

	def blitme(self):
		"""Draw the ship at its current location."""

		self.screen.blit(self.image, self.rect)
