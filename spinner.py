import time
import sys

def spin(chars):
	for c in chars: 
		sys.stdout.write(chr(27) + '[1D' + c)
		sys.stdout.flush()
		time.sleep(1.0)
while True:
	spin("|/-\\")
