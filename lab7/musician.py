import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption("Player")
bg = pygame.image.load('imagess/chill.png').convert_alpha()

song_files = ['songs/song1.mp3', 'songs/song2.mp3', 'songs/song3.mp3', 'songs/song4.mp3']

songs_q = [pygame.mixer.Sound(song) for song in song_files]
q = 0
current_song = songs_q[q]

playing = False

def play():
    global playing
    current_song.play()
    playing = True

def pause():
    global playing
    pygame.mixer.stop()
    playing = False

def next_song():
    global q, current_song
    pygame.mixer.stop()
    q = (q + 1) % len(songs_q)
    current_song = songs_q[q]
    play()

def prev_song():
    global q, current_song
    pygame.mixer.stop()
    q = (q - 1) % len(songs_q)
    current_song = songs_q[q]
    play()

running = True
while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if playing:
            pause()
        else:
            play()
    elif keys[pygame.K_RIGHT]:
        next_song()
    elif keys[pygame.K_LEFT]:
        prev_song()

    pygame.display.update()

pygame.quit()
