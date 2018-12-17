import time
import pygame
import random
import os

base_path = './Festivus/Feats/ogg_files/'
audiofiles = ['airgrieve.ogg',
              'featsostr.ogg',
              'festmiracl.ogg',
              'festrestus.ogg']


def setup_pygame():
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.music.set_volume(1)


def load_audiofiles():
        clip_list = []
        for audiofile in audiofiles:
                clip_list.append(pygame.mixer.Sound(base_path + audiofile))
        return clip_list


def quit_pygame():
        print('\nClosing app.')
        pygame.quit()


def generate_random_clip(clip_list, last_clip_list):
        current_clip = random.randint(0, len(clip_list)-1)
        while current_clip in last_clip_list:
                        current_clip += 1
                        if (current_clip > len(clip_list)-1):
                                current_clip = 0
        return current_clip


def update_last_clip_list(last_clip_list):
        if (len(last_clip_list) > 2):
                del last_clip_list[0]


def prevent_overlap():
        if (pygame.mixer.get_busy()):
                pygame.mixer.stop()


def main():
        last_clips = []
        setup_pygame()
        clips = load_audiofiles()

        while True:
                key_stroke = input(
                    'Press any key to play a sound clip, otherwise press e.\n')

                if (key_stroke == 'e'):
                        break
                else:
                        prevent_overlap()
                        chosen_clip = generate_random_clip(clips, last_clips)
                        clips[chosen_clip]. play()
                        last_clips.append(chosen_clip)
                update_last_clip_list(last_clips)

        quit_pygame()


if __name__ == "__main__":
        main()
