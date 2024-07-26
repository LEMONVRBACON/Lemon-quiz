import colorama
import os
import time
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
correct = 0
os.system("title Lemon quiz")
print(Fore.RED + """
.__                                                                             .__        
|  |   ____   _____   ____   ____      _________    _____   ____     ________ __|__|_______
|  | _/ __ \ /     \ /  _ \ /    \    / ___\__  \  /     \_/ __ \   / ____/  |  \  \___   /
|  |_\  ___/|  Y Y  (  <_> )   |  \  / /_/  > __ \|  Y Y  \  ___/  < <_|  |  |  /  |/    / 
|____/\___  >__|_|  /\____/|___|  /  \___  (____  /__|_|  /\___  >  \__   |____/|__/_____ \
          \/      \/            \/  /_____/     \/      \/     \/      |__|              \/
""")
# print(Fore.CYAN + "lemon cool")
# print(Back.RED + "lemon as at fortnigt")
# print(Style.BRIGHT + "LEMON NIGHT")

answer = input(Fore.CYAN + "what is lemon's favorte food? ").strip()
if answer == "bacon":
   print("correct")
   time.sleep(3)
   correct = +1
   os.system("title Lemon quiz ^| points: " + str(correct))
else:
   print("wrong")
   time.sleep(3)
   correct = -1
   os.system("title  Lemon quiz ^| points: " + str(correct))
os.system("cls")
answer = input(Fore.CYAN + "what was lemon old pfp a space monke or a dog? ").strip()
if answer == "space monke":
   print("correct")
   time.sleep(3)
   correct = +1
   os.system("title Lemon quiz ^| points: " + str(correct))
else:
   print("wrong")
   time.sleep(3)
   correct = -1
   os.system("title Lemon quiz ^| points: " + str(correct))
   os.system("cls")
answer = input(Fore.CYAN + "what is my least favorit Fruit").strip()
if answer == "lime":
   print("correct")
   time.sleep(3)
   correct = +1
   os.system("title Lemon quiz ^| points: " + str(correct))
else:
   print("wrong")
   time.sleep(3)
   correct = -1
   os.system("title Lemon quiz ^| points: " + str(correct))
os.system("cls")
answer = input(Fore.CYAN + "what is my least tiktoker").strip()
if answer == "lime vr":
   print("correct")
   time.sleep(3)
   correct = +1
   os.system("title Lemon quiz ^| points: " + str(correct))
else:
   print("wrong")
   time.sleep(3)
   correct = -1
   os.system("title Lemon quiz ^| points: " + str(correct))
print("You scored " + correct + " Good job!")
time.sleep(15)