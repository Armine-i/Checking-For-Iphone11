from subprocess import Popen
import sys

filename = "ebayScript.py"
# run and relaunch my script if there's an exception
while True:
    print("\nStarted " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()
