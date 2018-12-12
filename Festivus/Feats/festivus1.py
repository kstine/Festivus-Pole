import time
import pygame
import random
import os


# List all of the audio files 
# These can be talking, song clips or music
audiofiles = ['./Festivus/Feats/ogg_files/airgrieve.ogg',
              './Festivus/Feats/ogg_files/featsostr.ogg',
              './Festivus/Feats/ogg_files/festmiracl.ogg',
              './Festivus/Feats/ogg_files/festrestus.ogg']

def main():
        # setup music player
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.music.set_volume(1)

        clips = []
        last_clips = []

        # load audio files
        for audiofile in audiofiles:
                clips.append(pygame.mixer.Sound(audiofile))

        number_of_clips = len(clips)-1

        def generate_random_clip():
                return random.randint(0, number_of_clips)

        while True:
                key_stroke = input(
                    'Press any key to play a sound clip, otherwise press e.\n')

                if (key_stroke == 'e'):
                        break
                else:
                        chosen_clip = generate_random_clip()
                        while chosen_clip in last_clips:
                                print(chosen_clip)
                                chosen_clip += 1
                                if (chosen_clip > number_of_clips):
                                        print(chosen_clip)
                                        chosen_clip = 0

                        print(chosen_clip)
                        clips[chosen_clip]. play()
                        last_clips.append(chosen_clip)
                        print(last_clips)
                if (len(last_clips)>2):
                        del last_clips[0]
                        print(last_clips)


        pygame.quit()

        input('\nClosing app.\n')         

if __name__ == "__main__":
        main()
