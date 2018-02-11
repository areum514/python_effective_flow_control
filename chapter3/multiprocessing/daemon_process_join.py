###################################
# File Name : daemon_multiprocessing_join.py
###################################
#!/usr/bin/python3

import time
import multiprocessing


def daemon():
    print ("Start")
    time.sleep(5)
    print ("Exit")

if __name__ == "__main__":
    d = multiprocessing.Process(name="daemon", target=daemon)
    d.daemon = True

    d.start()
    d.join()