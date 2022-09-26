#!/usr/bin/env python3

#=====# #=====#
import os
import sys
from time import sleep


#=====# #=====#
'''
if there is no argument, print usage and exit
'''

if len(sys.argv) < 2:
    print("# Usage: sudo autopac.py [arg1] [arg2] ... #".center(60, '-'))
    sys.exit()

args = []
for arg in sys.argv[1:]:
    args.append(arg)


#=====# #=====#    
'''
create search.txt file for storing search result
'''

os.system("clear")
ascii_art = '''
 ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ██▓███   ▄▄▄       ▄████▄  
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▒████▄    ▒██▀ ▀█  
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ 
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░▒ ░       ▒   ▒▒ ░  ░  ▒   
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░░         ░   ▒   ░        
      ░  ░   ░                  ░ ░                 ░  ░░ ░      
                                                        ░        
'''
print(ascii_art)
print("# Creating search.txt #".center(60, '-'))
sleep(1)
try:
    os.system("touch search.txt")
except Exception as ex:
    print("Could not create file!\n" + ex)
    sys,exit()

#=====# #=====#
'''
search for query and store them in search.txt
'''

print("\n")
print(f"# Searching for {' '.join(args)} #".center(60, '-'))
print("\n")
print("# Getting results #".center(60, '-'))
sleep(1)

if len(args) == 1:
    query = args[0]
    os.system(f"pacman -Ss {query} > search.txt")
else:
    os.system(f"pacman -Ss {' '.join(args)} > search.txt")

#=====# #=====#
'''
open search.txt for editing in 'read' mode
'''

with open("search.txt", "r") as file:
    search = file.readlines()


#=====# #=====#
'''
create 'even' list and append even lines to it
'''

even = []
for index, line in enumerate(search):
    if index % 2 == 0:
        even.append(line)


#=====# #=====#
'''
create 'names' list and append names to it
'''

names = []
for item in even:
    names.append(item.split("/")[1])


#=====# #=====#
'''
create 'results' list and append final results to it
'''
    
results = []
for name in names:
    var = name.split()[0]
    results.append(var) 


#=====# #=====#
'''
ask user to confirm installation 
and create 'error.txt' for error log
'''

print("\n")
print(f"# Done! Found {len(results)} #".center(60, '-'))
print("\n")
ok = input("*** Continue installing? (y/n) ")
print("\n")
os.system("echo '#====# Error Log #====#' > error.txt")


#=====# #=====#
'''
if user confirmed installation, then install all tools
and when all tools installd delete seearch.txt and exit
'''

if "y" in ok:
    for index, item in enumerate(results):
        try:
            os.system("clear")
            print(f"# {str(index).rjust(3)} / {str(len(results)).rjust(3)} #".center(60, '-'))
            os.system(f"sudo pacman -S {item} --noconfirm")
        except Exception as ex:
            print(f"# Can't install {item} -> Error code in error.txt #".center(60, '-'))
            os.system(f"echo {ex} >> error.txt")
            
    print("# Deleting search.txt file #".center(60, '-'))
    os.system("rm search.txt")    










