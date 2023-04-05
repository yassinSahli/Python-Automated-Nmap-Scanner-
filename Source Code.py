#!/usr/bin/python3
import nmap
import emoji
Scanner = nmap.PortScanner()
print("[!] Welcome to S.Builder's Scanner, simplified, automoate tool [!]")
print(emoji.emojize("[!] Made with :red_heart: [!]", variant="emoji_type"))
print("<--------------------------------------------------------------->")
print("<--------------------------------------------------------------->")
ip_addr = input("Enter your the IP address to scan : ")
print("The IP your entered is :  ", ip_addr)
type(ip_addr)
print("<--------------------------------------------------------------->")
type_scan = input("\nPlease enter the type of scan you want to run \n 1)SYN-ACK Scan\n 2)UDP Scan\n 3)Comprehensive Detailed Scan\n")
print("Type Selected : ",  type_scan)

if type_scan == '1':
    print("Nmap Version : ", Scanner.nmap_version())  # Display nmap's version
    print("<--------------------------------------------------------------->")
    print("You chose : SYN-ACK Scan, Starting Scan...")
    print("<--------------------------------------------------------------->")
    Scanner.scan(ip_addr, '1-1024', '-v -sS')  # nmap ip_addr port_number -v(verbose = human redable) -sS for s: scan and S : SYN-ACK
    print("<--------------------------------------------------------------->")
    print(Scanner.scaninfo())  # Display the result of scan (Scan infos)
    print("<--------------------------------------------------------------->")
    print("IP Status : ", Scanner[ip_addr].state())  # Shows if the IP address is UP or down == User online or offline
    print("<--------------------------------------------------------------->")
    print(Scanner[ip_addr].all_protocols())  # Protocol used for scan
    print("<--------------------------------------------------------------->")
    print("OPEN PORTS : ", Scanner[ip_addr].keys())  # Displays ALL OPEN dangerous ports
    print("<--------------------------------------------------------------->")
    print("<--------------------------------------------------------------->")
    print("[!]Report Ends.[!]")
elif type_scan == '2':
    print("Nmap Version : ", Scanner.nmap_version())  # Display nmap's version
    print("<--------------------------------------------------------------->")
    print("You chose : UDP Scan, Starting Scan...")
    print("<--------------------------------------------------------------->")
    Scanner.scan(ip_addr, '1-1024', '-v -sU')  # nmap ip_addr port_number -v(verbose = human redable) -sU for s : scan & U : UDP
    print("<--------------------------------------------------------------->")
    print(Scanner.scaninfo())  # Display the result of scan (Scan infos)
    print("<--------------------------------------------------------------->")
    print("IP Status : ", Scanner[ip_addr].state())  # Shows if the IP address is UP or down == User online or offline
    print("<--------------------------------------------------------------->")
    print(Scanner[ip_addr].all_protocols())  # Protocol used for scan
    print("<--------------------------------------------------------------->")
    print("OPEN PORTS : ", Scanner[ip_addr].keys())  # Displays ALL OPEN dangerous ports
    print("<--------------------------------------------------------------->")
    print("<--------------------------------------------------------------->")
    print("[!]Report Ends.[!]")
elif type_scan == '3':
    print("Nmap Version : ", Scanner.nmap_version())  # Display nmap's version
    print("<--------------------------------------------------------------->")
    print("You chose : Comprehensive Detailed Scan, Starting Scan...")
    print("<--------------------------------------------------------------->")
    Scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')  # nmap ip_addr port_number -v(verbose = human redable) -sU for s : scan & U : UDP & sV : service fingerprinting/Ennumeration & sC : scan for default scripts &  A : Agressive Scan & O : Operating System detection
    print("<--------------------------------------------------------------->")
    print(Scanner.scaninfo())  # Display the result of scan (Scan infos)
    print("<--------------------------------------------------------------->")
    print("[!]Report Ends.[!]")
else :
    print(f"{Fore.YELLOW} [!] [WARNING] [!] {Fore.RESET} ")
    print("Input Error ! Please enter a valid options.")
    print(f"{Fore.YELLOW} [!]Report Ends.[!] {Fore.RESET} ")


