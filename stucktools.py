import os

def display_banner():
    print("\033[92m")  # Set text to green
    print(r"""
███████╗████████╗██╗   ██╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝╚══██╔══╝╚██╗ ██╔╝██║ ██╔╝╚══██╔══╝██╔═══██╗██╔════╝ ██║     ██╔════╝
███████╗   ██║    ╚████╔╝ █████╔╝    ██║   ██║   ██║██║  ███╗██║     █████╗  
╚════██║   ██║     ╚██╔╝  ██╔═██╗    ██║   ██║   ██║██║   ██║██║     ██╔══╝  
███████║   ██║      ██║   ██║  ██╗   ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
╚══════╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
""")
    print("github.com/relld2iscord/styktogle")
    print("Multi-Tool")
    print("\033[0m")  # Reset text color

def display_menu():
    print("\033[92m")  # Set text to green
    print("[Menu n°1]")
    print("[01] -> IP Pinger")
    print("[02] -> IP Port Scanner")
    print("[03] -> SQL Vulnerability")
    print("[04] -> Phishing Attack")
    print("[05] -> Quitter")
    print("\033[0m")  # Reset text color

def execute_program(program_name):
    os.system(f"./programs/{program_name}")

def main():
    display_banner()
    while True:
        display_menu()
        choice = input("\033[92mSélectionnez une option (1-5): \033[0m")
        
        if choice == '1':
            execute_program("ip-pinger.py")
        elif choice == '2':
            execute_program("ip-port_scanner.py")
        elif choice == '3':
            execute_program("sql_vulnerability.py")
        elif choice == '4':
            execute_program("phishing_attack.py")
        elif choice == '5':
            print("\033[92mQuitter...\033[0m")
            break
        else:
            print("\033[91mOption invalide, veuillez réessayer.\033[0m")

        input("\033[92m\nAppuyez sur Entrée pour continuer...\033[0m")

if __name__ == "__main__":
    main()


