import logging
import threading
import time

def printing_name():
    na = "Alex"
    print("Name: ", na)

def printing_age():
    age = 20
    print("Age: ", age)

if __name__ == '__main__':
   x = threading.Thread(target=printing_name)
   x.start()
   
   time.sleep(4)

   y = threading.Thread(target=printing_age)
   y.start()
