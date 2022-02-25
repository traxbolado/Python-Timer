import time

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('[Lunar Temporizador] O tempo chegou ao fim! \n')
  
print(".___________..______           ___      ___   ___ ")
print("|           ||   _  \         /   \     \  \ /  / ")
print("`---|  |----`|  |_)  |       /  ^  \     \  V  /  ")
print("    |  |     |      /       /  /_\  \     >   <   ")
print("    |  |     |  |\  \----. /  _____  \   /  .  \  ")
print("    |__|     | _| `._____|/__/     \__\ /__/ \__\ ")
print("\n\n")

t = input("[Lunar Temporizador] Insira o tempo em segundos: \nR: ")
  
countdown(int(t))
