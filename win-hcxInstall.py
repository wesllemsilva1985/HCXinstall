#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Code by: IgorMatsunaga - NSW
#Site: https://nsworld.com.br
#Github: https://github.com.br/igorMatsunaga

#Edited by: Wellem
#Modified source code for terminal windows
#Github: https://github.com/wesllemsilva1985 and https://github.com/Wescomp-Dev

import os
os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607
    
    
logo = '\033[1;34m'+'''

██╗  ██╗ ██████╗██╗  ██╗██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
██║  ██║██╔════╝╚██╗██╔╝██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
███████║██║      ╚███╔╝ ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
██╔══██║██║      ██╔██╗ ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
██║  ██║╚██████╗██╔╝ ██╗██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝                                                                                  
-----------------------------------coded by igorMatsunaga----------------------------------------
-----------------------------------------nsworld-------------------------------------------------
'''+'\033[39m'
print(logo)

menu = '\033[1;33m'+'''
Escolha o número da opção que deseja utilizar:

(1)  Instalar Hcxdumptool
(2)  Instalar hxctools
(3)  Instalar Hcxdumptool e hxctools
'''+'\033[39m'
print(menu)

def dumptool():
    os.system("git clone https://github.com/ZerBea/hcxdumptool.git")
    os.system("cd hcxdumptool && make && make install")
    print("Instalação completa")

def tools():
    os.system("git clone https://github.com/ZerBea/hcxtools.git")
    os.system("apt-get update && apt-get install zlib1g-dev && apt-get install libpcap0.8-dev && apt-get install libcurl4-openssl-dev")
    os.system("cd hcxtools && make && make install")

escolha = input('\033[1;32m'+'''Digite a opção: '''+'\033[0;0m')


if(escolha == "1"):
    print('\033[1;33m'+'''Instalando Hcxdumptool '''+'\033[0;0m')
    dumptool()
elif(escolha == "2"):
    print('\033[1;33m'+'''Instalando hxctools'''+'\033[0;0m')
    tools()
elif(escolha == "3"):
    print('\033[1;33m'+'''As ferramentas estão sendo instaladas'''+'\033[0;0m')
    dumptool()
    tools()    
else:
    exit()


