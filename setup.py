# Github : https://github.com/Jays-C0D3
#
# This file will move the winalysis file to your startup folder when you run it.
#You can also do this manually if you would like of course.

import subprocess as a
import os as b

def main():
    puzzle = b.getcwd()
    usrlist = []
    try: 
        b.chdir(puzzle[0:3]+'Users')
        for usr in b.listdir():
            if usr.lower() in ['all users','default user', 'desktop.ini','public']:
                pass
            else:
                usrlist.append(usr)
    except:
        next
    if len(usrlist)>1:
        menu = {}
        for usr in range(len(usrlist)):
            menu[usr] = usrlist[usr]
        print("Which user would you like to set WinAlysis for?")
        for opt,val in menu.items():
            print(str(opt) + '). ' + val )
        usr = str(input("Select number and press enter: "))
        print("Setting WinAlysis in start up for {0} . . .".format(usrlist[int(usr)]))
        a.run(['powershell','mv','winalysis.py',puzzle[0:3]+usrlist[int(usr)]])

    else:
        print("Setting WinAlysis in start up for {0} . . .".format(usrlist[0]))
        a.run(['powershell','mv','winalysis.py',puzzle[0:3]+usrlist[0]]+)
main()
