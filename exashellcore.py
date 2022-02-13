from platform import platform
import time
import os
import requests
import platform
import subprocess
import psutil

from pystyle import Write, Colors

VERSION = "1.1"

lastestVersion = requests.get("https://api.github.com/repos/xYanis/ExaShell/releases/latest").json["tag_url"]

if VERSION != lastestVersion:
    print(f"[] You are not on the latest version (v{lastestVersion}) !")

Write.Print("[] Loading ExaShell ...", Colors.red_to_purple, interval=0.040)
time.sleep(2)
os.system('cls')
Write.Print("[] Enter help to see all commands of ExaShell ! \n", Colors.yellow_to_red, interval=0.040)

while True:
    base = Write.Input("[] root@ExaShell -> ", Colors.yellow_to_red, interval=0.040)
    if base == "help":
        Write.Print('╭───────>Help<──────╮\n', Colors.purple_to_red, interval=0.040)
        Write.Print('[->] help (show this menu)\n', Colors.purple_to_red, interval=0.040)
        Write.Print('[->] exainfo (show informations about this computer)\n', Colors.purple_to_red, interval=0.040)
        Write.Print('[->] exaspeed (launch tool for speed test) | SOON\n', Colors.purple_to_red, interval=0.040)
        Write.Print('[->] exanetconfig (show informations about network) | SOON\n', Colors.purple_to_red, interval=0.040)
        Write.Print('[->] exapart (launch tool for partitioning) | SOON\n', Colors.purple_to_red, interval=0.040)
        Write.Print('╰──────────><──────────╯\n', Colors.purple_to_red, interval=0.040)

    if base == "exainfo":
        uname = platform.uname()
        Write.Print('╭───────>ExaInfo<──────╮\n', Colors.purple_to_red, interval=0.040)
        Write.Print(f'[->] OS : {uname.system}\n', Colors.purple_to_red, interval=0.040)
        Write.Print(f'[->] Computer Name : {uname.node}\n', Colors.purple_to_red, interval=0.040)
        Write.Print(f'[->] OS Version : {uname.version}\n', Colors.purple_to_red, interval=0.040)
        Write.Print(f'[->] CPU : {uname.processor}\n', Colors.purple_to_red, interval=0.040)
        Write.Print(f'[->] CPU Architecture : {uname.machine}\n', Colors.purple_to_red, interval=0.040)
        Write.Print('╰──────────><──────────╯\n', Colors.purple_to_red, interval=0.040)
    
    if base == "exaspeed":
        Write.Print('╭───────>ExaSpeed<──────╮\n', Colors.purple_to_red, interval=0.040)
        Write.Print('COMING SOON\n', Colors.purple_to_red, interval=0.040)

    if base == "exanetconfig":
        Write.Print('╭───────>ExaNetconfig<──────╮\n', Colors.purple_to_red, interval=0.040)
        Write.Print('COMING SOON\n', Colors.purple_to_red, interval=0.040)

    if base == "exapart":
        Write.Print('╭───────>ExaPart<──────╮\n', Colors.purple_to_red, interval=0.040)
        Write.Print('COMING SOON\n', Colors.purple_to_red, interval=0.040)

