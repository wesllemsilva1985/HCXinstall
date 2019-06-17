#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Code by: IgorMatsunaga - NSW
#Site: https://nsworld.com.br
#Github: https://github.com.br/igorMatsunaga

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
print('\033[34m' + logo + '\033[0m')
menu = '''
Escolha o número da opção que deseja utilizar:

(1)  Instalar Hcxdumptool
(2)  Instalar hxctools
(3)  Instalar Hcxdumptool e hxctools
'''
print('\033[33m' + menu)

def dumptool():
    os.system("git clone https://github.com/ZerBea/hcxdumptool.git")
    os.system("cd hcxdumptool && make && make install")
    print("Instalação completa")

def tools():
    os.system("git clone https://github.com/ZerBea/hcxtools.git")
    os.system("apt-get update && apt-get install zlib1g-dev && apt-get install libpcap0.8-dev && apt-get install libcurl4-openssl-dev")
    os.system("cd hcxtools && make && make install")

escolha = raw_input('\033[5m' + "Digite a opção: " + '\033[0m')


if(escolha == "1"):
    print('\033[33m' + "Instalando Hcxdumptool ")
    dumptool()
elif(escolha == "2"):
    print('\033[33m' + "Instalando hxctools" + '\033[0m')
    tools()
elif(escolha == "3"):
    print('\033[33m' + "As ferramentas estão sendo instaladas" + '\033[0m')
    dumptool()
    tools()    
else:
    exit()


