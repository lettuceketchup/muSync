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
		self.timeElapsed = -1

	def play(self):
		self.status['playing'] = True
		self.status['paused'] = False
		self.status['stopped'] = False
		self.status['ended'] = False
		pygame.mixer.music.play()
		self.timeElapsed = self.currentPos()
		pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
		print('played')

	def pause(self):
		self.status['playing'] = False
		self.status['paused'] = True
		pygame.mixer.music.pause()
		self.timeElapsed = self.currentPos()
		print('paused')

	def resume(self):
		self.status['playing'] = True
		self.status['paused']= False
		pygame.mixer.music.unpause()
		self.timeElapsed = self.currentPos()
		print('resumed')

	def stop(self):
		self.status['playing'] = False
		self.status['stopped'] = True
		pygame.mixer.music.stop()
		self.timeElapsed = self.currentPos()
		print('stopped')
		
	def seekInitialize(self, millisec):
		pygame.mixer.music.rewind()
		pygame.mixer.music.set_pos(millisec/1000)
		self.timeElapsed = self.currentPos()
		print('seeked!')

	def seek(self, millisec):
		pygame.mixer.music.set_pos(millisec/1000)
		self.timeElapsed = self.currentPos()

	def currentPos(self):
		return pygame.mixer.music.get_pos()

		

