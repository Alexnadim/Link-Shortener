import sys
import time
import pyshorteners
red="\033[1;91m"
green="\033[1;92m"
yellow="\033[1;93m"
blue="\033[1;94m"
purple="\033[1;95m"
cyan="\033[1;96m"
white="\033[1;97m"


def slowprint(s):
	for c in s+'\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(30/4000)
slowprint(red+"============================================================")
slowprint(red+"============================================================")

		
aschi_code=green+"""
   _____ _    _  ____  _____ _______ ______ _____  
  / ____| |  | |/ __ \|  __ \__   __|  ____|  __ \ 
 | (___ | |__| | |  | | |__) | | |  | |__  | |__) |
  \___ \|  __  | |  | |  _  /  | |  |  __| |  _  / 
  ____) | |  | | |__| | | \ \  | |  | |____| | \ \ 
 |_____/|_|  |_|\____/|_|  \_\ |_|  |______|_|  \_\
"""

slowprint(aschi_code)
slowprint(yellow+"\n============================================================")
slowprint(yellow+"============================================================")


time.sleep(1)

link=str(input(yellow+"\n\n [ENTER YOUR LINK HERE] = "))


s=pyshorteners.Shortener()
final_link=(s.tinyurl.short(link))
time.sleep(2)
print(green+"\n [YOUR-SHORT-LINK-IS] = ",final_link)

