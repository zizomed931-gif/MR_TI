import os
from modules.engine import run_scan
from modules.database import save_result

LOGO = """
\033[1;35m
    ███╗   ███╗██████╗     ████████╗██╗
    ████╗ ████║██╔══██╗    ╚══██╔══╝██║
    ██╔████╔██║██████╔╝       ██║   ██║
    ██║╚██╔╝██║██╔══██╗       ██║   ██║
    ██║ ╚═╝ ██║██║  ██║       ██║   ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝       ╚═╝   ╚═╝
    [ M . R . T I  -  G I T L A B  E D I T I O N ]
\033[0m"""

def main():
    os.system('clear')
    print(LOGO)
    print("1. Start Scan (فحص جديد)")
    print("2. Launch Dashboard (تشغيل لوحة الويب)")
    choice = input("\nM.R. TI > ")
    
    if choice == '1':
        target = input("Enter Target: ")
        result = run_scan(target)
        if result:
            save_result(result)
            print(f"\033[1;32m[+] Saved: {result['ip']}\033[0m")
    elif choice == '2':
        print("[*] Dashboard running at http://127.0.0.1:5000")
        os.system("python app.py")

if __name__ == "__main__":
    main()
