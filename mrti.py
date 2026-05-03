import os
import sys
import socket
import requests
import time

# الشعار الاحترافي (M.R. TI)
LOGO = """
 \033[1;32m     ___           ___           ___           ___     
     /__/\         /  /\         /__/\         /  /\    
    |  |::\       /  /::\        \  \:\       /  /:/_   
    |  |:|:\     /  /:/\:\        \  \:\     /  /:/ /\  
  __|__|:|\:\   /  /:/~/:/    _____\__\:\   /  /:/ /:/  
 /__/::::| \:\ /__/:/ /:/    /__/::::::::\ /__/:/ /:/   
 \  \:\~~\__\/ \  \:\/:/     \  \:\~~\__\/ \  \:\/:/    
  \  \:\        \  \::/       \  \:\        \  \::/     
   \  \:\        \  \:\        \  \:\        \  \:\     
    \  \:\        \  \:\        \  \:\        \  \:\     
     \__\/         \__\/         \__\/         \__\/     
\033[1;37m       [ M . R . T I  -  V 1 . 0  S Y S T E M ]
       [ منظومة مستر تي لجمع المعلومات وصيد الثغرات ]
\033[0m"""

def ghost_mode(enable=True):
    if enable:
        print("\033[1;34m[*] تفعيل وضع الشبح (Tor SOCKS5)... \033[0m")
        proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        return proxies
    return None

def telegram_push(msg):
    token = "TOKEN_هنا"
    chat_id = "ID_هنا"
    if token != "TOKEN_هنا":
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
        requests.get(url)

def scanner(target):
    print(f"\033[1;33m[*] جاري فحص الهدف: {target}\033[0m")
    try:
        ip = socket.gethostbyname(target)
        header_check = requests.get(f"http://{target}", timeout=5).headers
        
        report = f"--- M.R. TI REPORT ---\nTarget: {target}\nIP: {ip}\n"
        
        if 'Server' in header_check:
            report += f"Server: {header_check['Server']}\n"
        if 'X-Frame-Options' not in header_check:
            report += "Vuln: Clickjacking (Missing X-Frame-Options)\n"
            
        print(f"\033[1;32m[+] تم اكتمال الفحص بنجاح!\033[0m")
        print(report)
        telegram_push(report)
    except Exception as e:
        print(f"\033[1;31m[-] خطأ: {e}\033[0m")

def main():
    os.system('clear')
    print(LOGO)
    print("\033[1;36m1. فحص هدف جديد (Gathering & Vuln Scan)")
    print("2. تفعيل وضع التخفي (Ghost Mode)")
    print("3. المساعدة (Help)")
    print("4. خروج\033[0m")
    
    choice = input("\nM.R. TI > ")
    
    if choice == '1':
        target = input("أدخل رابط الموقع (بدون http): ")
        scanner(target)
    elif choice == '2':
        ghost_mode()
    else:
        sys.exit()

if __name__ == "__main__":
    main()
