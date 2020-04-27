import threading
import time

def sleeper(n , name):
   print('Hi i am ', name, ' going to sleep')
   time.sleep(n)
   print(name , ' woken up ')


t= threading.Thread(target= sleeper, name='THread 1', args=(5, 'THREAD1'))

t.start()

print('hello')