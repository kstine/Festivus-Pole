# import pyglet
# import os
# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'Festivus-Pole/Festivus/Feats/airgrieve.ogg')


# song = pyglet.media.load(filename)
# song = pyglet.media.load('/Users/kelbystine/Documents/GitHub/Festivus-Pole/Festivus/Feats/airgrieve.ogg', streaming=False)
# song.play()
# pyglet.app.run()

import pygame

def main():
    pygame.init()
    song = pygame.mixer.Sound(
        '/Users/kelbystine/Documents/GitHub/Festivus-Pole/Festivus/Feats/airgrieve.ogg')
    # clock = pygame.time.Clock()
    song.play()
    # while True:
    #     clock.tick(60)
    # pygame.display.quit()
    # pygame.quit()

if __name__ == "__main__":
    main()