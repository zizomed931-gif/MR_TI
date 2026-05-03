import os, sys, socket
from modules.utils import scan_sql, scrape_info
from modules.database import save_data

PASSWORD = "3295X"
LOGO = """\033[1;35m
    ███╗   ███╗██████╗ 
    ████╗ ████║██╔══██╗
    ██╔████╔██║██████╔╝
    ██║╚██╔╝██║██╔══██╗
    ██║ ╚═╝ ██║██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝ [ M.R. TI - النسخة النهائية ]
\033[0m"""

def login():
    os.system('clear')
    print("\033[1;31m[!] الدخول مقيد\033[0m")
    val = input("[*] أدخل رمز الأمان: ")
    return val == PASSWORD

def main():
    if not login(): 
        print("❌ رمز خاطئ!"); sys.exit()
    
    while True:
        os.system('clear')
        print(LOGO)
        print("1. فحص شامل (SQL + Scrape)")
        print("2. تشغيل لوحة الويب")
        print("3. خروج")
        
        cmd = input("\nM.R. TI > ")
        if cmd == '1':
            target = input("أدخل رابط الموقع: ")
            ip = socket.gethostbyname(target)
            sql_res = scan_sql(target)
            emails = scrape_info(target)
            save_data(target, ip, f"{sql_res} | Emails: {len(emails)}")
            print(f"\033[1;32m[+] تم الحفظ! IP: {ip}\033[0m")
            input("اضغط Enter للعودة...");
        elif cmd == '2':
            print("[*] السيرفر يعمل على http://127.0.0.1:5000")
            os.system("python app.py")
        elif cmd == '3': break

if __name__ == "__main__":
    main()
