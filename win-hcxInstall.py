#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Code by: IgorMatsunaga - NSW
#Site: https://nsworld.com.br
#Github: https://github.com.br/igorMatsunaga

#Edited by Wellem
#code adapted for console windows
#Github https://github.com/wesllemsilva1985 and https://github.com/Wescomp-Dev

import os

    
    
logo = '''

██╗  ██╗ ██████╗██╗  ██╗██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
██║  ██║██╔════╝╚██╗██╔╝██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
███████║██║      ╚███╔╝ ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
██╔══██║██║      ██╔██╗ ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
██║  ██║╚██████╗██╔╝ ██╗██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝                                                                                  
-----------------------------------coded by igorMatsunaga----------------------------------------
-----------------------------------------nsworld-------------------------------------------------
'''
print(logo)
menu = '''
Escolha o número da opção que deseja utilizar:

(1)  Instalar Hcxdumptool
(2)  Instalar hxctools
(3)  Instalar Hcxdumptool e hxctools
'''
print(menu)

def dumptool():
    os.system("git clone https://github.com/ZerBea/hcxdumptool.git")
    os.system("cd hcxdumptool && make && make install")
    print("Instalação completa")

def tools():
    os.system("git clone https://github.com/ZerBea/hcxtools.git")
    os.system("apt-get update && apt-get install zlib1g-dev && apt-get install libpcap0.8-dev && apt-get install libcurl4-openssl-dev")
    os.system("cd hcxtools && make && make install")

escolha = input("Digite a opção: ")


if(escolha == "1"):
    print("Instalando Hcxdumptool ")
    dumptool()
elif(escolha == "2"):
    print("Instalando hxctools")
    tools()
elif(escolha == "3"):
    print("As ferramentas estão sendo instaladas")
    dumptool()
    tools()    
else:
    exit()


