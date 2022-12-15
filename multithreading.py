'''
Thread: a thread is a sequence of instructions that the computer performs. 
It is executed independently.
Multithreading: 
executing multiple parts of the program at a time using the threading module. 
We can import this module by writing the below statement.

import threading
'''

import threading
import time

class CPUPainter:
    
    def paintWall(self):
        time.sleep(2)
        print('wall painted')
        
    def __init__(self):
        # we're creating a new thread that's targeting paintwall function
        # and we are going to start a thread by t.start(). it means instead of
        # calling CPUPainter and going originally calling the painwall function
        # waiting two seconds printing wall painted and then moving on.
        t = threading.Thread(target=self.paintWall)
        t.start()
        
CPUPainter()
CPUPainter()
CPUPainter()
CPUPainter()