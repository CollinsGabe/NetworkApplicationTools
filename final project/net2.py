import subprocess
import socket
import os

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # (Google's public DNS server)
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
    print("1. Summarized scan - List live IP addresses on the network")
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
        result_file = "1.txt"
    elif option == 2:
        command = f"sudo nmap -A 192.168.1.0/24"
        result_file = "2.txt"
    elif option == 3:
        command = f"sudo nmap -sA 192.168.1.0/24"
        result_file = "3.txt"
    elif option == 4:
        command = f"sudo nmap -oG - 192.168.1.0/24"
        result_file = "4.txt"
    elif option == 5:
        command = f"sudo nmap -v 192.168.1.0/24"
        result_file = "5.txt"
    elif option == 6:
        command = f"sudo nload"
        result_file = "6.txt"
    elif option == 7:
        command = f"sudo nmap -sn -PE 192.168.1.0/24"
        result_file = "7.txt"
    elif option == 8:
        command = f"sudo nmap -sV 192.168.1.0/24"
        result_file = "8.txt"
    elif option == 9:
        command = f"systemctl stop NetworkManager"
        result_file = "9.txt"
    elif option == 10:
        command = f"systemctl start NetworkManager"
        result_file = "10.txt"
    else:
        print("Invalid option. Exiting.")
        return

    try:
        # Run the command and capture the output
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        # Check if the command was successful
        if process.returncode == 0:
            # Append result to the corresponding text file
            with open(result_file, "a") as file:
                file.write(f"Option {option} result:\n")
                file.write(stdout)
                file.write("\n\n")
            print(f"Option {option} executed successfully.")
        else:
            print(f"Error executing option {option}. stderr: {stderr}")
    except Exception as e:
        print(f"Error: {e}")

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

