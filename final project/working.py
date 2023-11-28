import subprocess
import socket
import os

def get_local_ip():
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  #(Google's public DNS server)
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_options():
    print("Welcome to the Network Monitoring Tool")
    print("--------------------------------------\n")
    print("Choose an option:")
    print("1. Summarized scan - List live IP addresses on network")
    print("2. Aggressive scan - Get detailed information about devices on the network")
    print("3. ACK scan - Differentiate between stateful and stateless firewalls")
    print("4. Grep output - Generate a grepable output for easy searching")
    print("5. Verbose scan - Produce output with higher verbosity")
    print("6. Data usage - Displays the networks data usage")
    print("7. Ping sweep - Discover live hosts using ICMP ping")
    print("8. Service version scan - Detect service versions on open ports")
    print("9. Stop network - Emergency stop all network services")
    print("10. Start network - Start all network services backup")
    print("11. Quit")

def execute_option(option, target):
    if option == 1:
        command = f"sudo nmap -sn 192.168.1.0/24"
    elif option == 2:
        command = f"sudo nmap -A 192.168.1.0/24"
    elif option == 3:
        command = f"sudo nmap -sA 192.168.1.0/24"
    elif option == 4:
        command = f"sudo nmap -oG - 192.168.1.0/24"
    elif option == 5:
        command = f"sudo nmap -v 192.168.1.0/24"
    elif option == 6:
        command = f"sudo nload"
    elif option == 7:
        command = f"sudo nmap -sn -PE 192.168.1.0/24"
    elif option == 8:
        command = f"sudo nmap -sV 192.168.1.0/24"
    elif option == 9:
    	command = f"systemctl stop NetworkManager"
    elif option == 10:
    	command = f"systemctl start NetworkManager"
    else:
        print("Invalid option. Exiting.")
        return

    subprocess.run(command, shell=True)

def main():
    target = get_local_ip()

    while True:
        display_options()
        user_choice = input("\nEnter your choice (1-11): ")

        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 1 <= user_choice <= 11:
            if user_choice == 11:
                print("Exiting. Goodbye!")
                break
            else:
                execute_option(user_choice, target)
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
