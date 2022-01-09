from pynput.keyboard import Key, Listener
import winsound
position=1
import pygame

pygame.mixer.init()  # initialise `init()` for mixer of pygame. 
masterSound =[]
print("""
   _     _     _     _     _     _     _     _       _       _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \     / \     / \   / \   / \   / \ 
 ( K ) ( e ) ( y ) ( b ) ( o ) ( a ) ( r ) ( d )   ( A )   ( L ) ( i ) ( v ) ( e )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/     \_/     \_/   \_/   \_/   \_/ 
""")
print("adding sound track")
for i in range(1, 206):
    masterSound.append(pygame.mixer.Sound("Nyan cat ({}).wav".format(i)))
print("sound track added")

def on_press(key):
    global position
    masterSound[position].play()
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