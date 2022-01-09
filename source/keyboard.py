from pynput.keyboard import Key, Listener
import winsound
position=1
import pygame

pygame.mixer.init()  # initialise `init()` for mixer of pygame. 
masterSound =[]
for i in range(1, 206):
    masterSound.append(pygame.mixer.Sound("Nyan cat ({}).wav".format(i)))
print("sound imported")

def on_press(key):
    global position
    print('a')
    masterSound[position].play()
    #winsound.PlaySound("Nyan Cat ({}).wav".format(position), winsound.SND_ASYNC)
    position += 1
    if(position >206):
        position=0

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()