import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load("./music/bensound-sunny.mp3")

class Player():
	def __init__(self):
		pygame.mixer.init()
		self.status = {
			'playing' : False,
			'paused' : False,
			'stopped' : False,
			'ended' : False,
			'quited' : False
		}

	def play(self):
		self.status['playing'] = True
		self.status['paused'] = False
		self.status['stopped'] = False
		self.status['ended'] = False
		pygame.mixer.music.play()
		pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
		print('played')

	def pause(self):
		self.status['playing'] = False
		self.status['paused'] = True
		pygame.mixer.music.pause()
		print('paused')

	def resume(self):
		self.status['playing'] = True
		self.status['paused']= False
		pygame.mixer.music.unpause()
		print('resumed')

	def stop(self):
		self.status['playing'] = False
		self.status['stopped'] = True
		pygame.mixer.music.stop()
		print('stopped')
		
	def seekInitialize(self, millisec):
		# pygame.mixer.music.rewind()
		pygame.mixer.music.set_pos(millisec/1000)
		print('seeked!')

	def seek(self, millisec):
		pygame.mixer.music.set_pos(millisec/1000)

	def currentPos(self):
		return pygame.mixer.music.get_pos()

		

