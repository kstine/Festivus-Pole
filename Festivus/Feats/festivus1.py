import time
import pygame
import random
import os





# List all of the audio files 
# These can be talking, song clips or music
audiofiles = ['airgrieve.ogg', 'featsostr.ogg', 'festmiracl.ogg', 'festrestus.ogg']

def main():
        # setup music player
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.music.set_volume(1)

        clip = []

        # load audio files
        for i in range (0, len(audiofiles)):
                clip.append(pygame.mixer.Sound(audiofiles[i]))
 
        keyStroke = ""

        while keyStroke != 'e':
                keyStroke = raw_input('Press any key to play a sound clip, otherwise press e.\n')

                clip[random.randint(0, len(clip)-1)]. play()

        print('what?\n')

        input('\n\npress enter key to exit')         

if __name__ == "__main__":
        main()
