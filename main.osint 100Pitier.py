import webbrowser
import os
import colorama
from colorama import Fore, Back, Style
colorama.init
reel_interface = """

  $$\   $$$$$$\   $$$$$$\  $$$$$$$\  $$\   $$\     $$\                     
$$$$ | $$$ __$$\ $$$ __$$\ $$  __$$\ \__|  $$ |    \__|                    
\_$$ | $$$$\ $$ |$$$$\ $$ |$$ |  $$ |$$\ $$$$$$\   $$\  $$$$$$\   $$$$$$\  
  $$ | $$\$$\$$ |$$\$$\$$ |$$$$$$$  |$$ |\_$$  _|  $$ |$$  __$$\ $$  __$$\ 
  $$ | $$ \$$$$ |$$ \$$$$ |$$  ____/ $$ |  $$ |    $$ |$$$$$$$$ |$$ |  \__|
  $$ | $$ |\$$$ |$$ |\$$$ |$$ |      $$ |  $$ |$$\ $$ |$$   ____|$$ |      
$$$$$$\\$$$$$$  /\$$$$$$  /$$ |      $$ |  \$$$$  |$$ |\$$$$$$$\ $$ |      
\______|\______/  \______/ \__|      \__|   \____/ \__| \_______|\__|      

 $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |\__$$  __|
$$ /  $$ |$$ /  \__|  $$ |  $$$$\ $$ |   $$ |   
$$ |  $$ |\$$$$$$\    $$ |  $$ $$\$$ |   $$ |   
$$ |  $$ | \____$$\   $$ |  $$ \$$$$ |   $$ |   
$$ |  $$ |$$\   $$ |  $$ |  $$ |\$$$ |   $$ |   
 $$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |   $$ |   
 \______/  \______/ \______|\__|  \__|   \__|             """
print(reel_interface)
print("")
osint = """

            [1] recherche-email  | [4] recherche-nom
            [2] recherche-IP     | [5] ip
            [3] recherche-numéro            
            
    Séléctionne une option : """
question_search = input(osint)
e_mail = """
            [1] Epios   | [5] Spokeo
            [2] Lusha   | [6] thatsthem
            [3] Hunter  | [7] emailsherlock
            [4] Osint   |
            
Séléctionne une option : """

if question_search == "1":
    face_email = input(e_mail)
    if face_email == "1":
        webbrowser.open("https://epieos.com/")
    if face_email == "2":
        webbrowser.open("https://www.lusha.com/")
    if face_email == "3":
        webbrowser.open("https://hunter.io/email-finder")
    if face_email == "4":
        webbrowser.open("https://osint.industries/")
    if face_email == "5":
        webbrowser.open("https://www.spokeo.com/")
    if face_email == "6":
        webbrowser.open("https://thatsthem.com/reverse-email-lookup")
    if face_email == "7":
        webbrowser.open("https://www.emailsherlock.com/email-reverse-search")

ipgros = """

            [1] infobyip          | [4] iplocation     | [7] IP looking
            [2] whatismyipaddress | [5] nordvpn-lookup | [8] Key CDN
            [3] tool-IP-lookup    | [6] IP loca        | [x] PRO LOOKUP
                                
séléctionne une option ou "exit" : """
if question_search == "2":
    search_ip = input(ipgros)
    if search_ip == "1":
        webbrowser.open("https://www.infobyip.com/")
    if search_ip == "2":
        webbrowser.open("https://whatismyipaddress.com/ip-lookup")
    if search_ip == "3":
        webbrowser.open("https://cdn.discordapp.com/attachments/1180669099555160174/1203077511215448064/iplookup.exe?ex=65cfc83e&is=65bd533e&hm=b8acc203446cd388a6f5d70dae5deeb2c1c3fa04ef05057a2185a984abe81183&")
    if search_ip == "4":
        webbrowser.open("https://www.iplocation.net/ip-lookup")
    if search_ip == "5":
        webbrowser.open("https://nordvpn.com/fr/ip-lookup/") 
    if search_ip == "6":
        webbrowser.open("https://iplocation.io/") 
    if search_ip == "7":
        webbrowser.open("https://www.ip-lookup.org/location/") 
    if search_ip == "8":
        webbrowser.open("https://tools.keycdn.com/geo") 
    if search_ip == "x":
        webbrowser.open("https://www.ip-tracker.org/lookup.php")
num = """

            [1] Celltrack
            [2] Epios
            [3] Osint.industries
            [4] Email looker
            
Séléctionne une option ou "exit" : """
if question_search == "3":
    ques_num = input(num)
    if ques_num == "1":
        webbrowser.open("https://www.celltrack.co.uk/")
    if ques_num == "2":
        webbrowser.open("https://epios.com/")
    if ques_num == "3":
        webbrowser.open("https://osint.industries/")
    if ques_num == "4":
        webbrowser.open("https://numlooker.com/reverse-email-lookup")
nom_t = """

            [1] Webmii     
            [2] Info-perso
            [3] Infofinder
            [4] Enaos
            [5] Webmii
            
séléctionne une option ou "exit" : """
if question_search == "4":
    ques_nom = input(nom_t)
    if ques_nom == "1":
        webbrowser.open("https://webmii.com//")
    if ques_nom == "2":
        webbrowser.open("https://info-perso.com/fr/")
    if ques_nom == "3":
        webbrowser.open("https://infofinder.io/")
    if ques_nom == "4":
        webbrowser.open("https://www.enaos.be/")
    if ques_nom == "5":
        webbrowser.open("https://webmii.com/")
search_ip = """

            [1] Ipinfo/io
            [2] Beta.snusbase
            [3] Iplocation.net
            [4] Ip.fr localiser

séléctionne une option ou "exit" : """
if question_search == "5" :
    ques_nom = input(search_ip)
    if ques_nom == "1":
        webbrowser.open("https://ipinfo.io/")
    if ques_nom == "2":
        webbrowser.open("https://beta.snusbase.com//")
    if ques_nom == "3":
        webbrowser.open("https://www.iplocation.net/ip-lookup/")
    if ques_nom == "4":
        webbrowser.open("https://mon-adresse-ip.fr/localiser-une-adresse-ip/")