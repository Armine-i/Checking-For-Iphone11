from subprocess import Popen
import sys

filename = "ebayScript.py"
while True:
    print("\nStarted " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()
