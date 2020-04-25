# import os
# os.add_dll_directory('C:\Program Files (x86)\VideoLAN\VLC')

# import vlc
# p = vlc.MediaPlayer("file:///E:/Study/PESU/Semester 6/CN/Project/bensound-sunny.mp3")
# p.play()

# from playsound import playsound
# playsound('bensound-sunny.mp3')
import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load("../bensound-sunny.mp3")
pygame.mixer.music.play()

print(time.time());
# while pygame.mixer.music.get_busy() == True:
#     continue
time.sleep(10)
pygame.mixer.music.pause()
print(time.time());