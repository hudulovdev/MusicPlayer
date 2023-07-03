import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

# Provide the path to the music file
file_path = "path_to_music_file.mp3"

# Play the music
play_music(file_path)
