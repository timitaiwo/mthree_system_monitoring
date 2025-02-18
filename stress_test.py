from tests import *
import signal
import sys

prompt = """
1. Press 1 for Memory Stress Testing
2. Press 2 for Disk Stress Testing
3. Press 3 for Network Stress Testing
4. Press 4 for CPU Stress Testing
5. Press 5 for MySQL Stress Testing

Press Ctrl/Super + C to cancel
"""

def main():
    
    print("\nWelcome to stress test. Select the below option to stress test your device", end="")

    while True:
        print(prompt)

        user_selection = input("Which stress test do you want to carry out? ")

        print()

        if not user_selection.isdigit():
            print("Please pass in an number greater than zero")
            continue

        user_selection = int(user_selection)
        lower_bound = 1
        upper_bound = 5
        if user_selection < lower_bound or  user_selection > upper_bound:
            print(f"Invalid number selected. Please select one between {lower_bound} and {upper_bound}")
            continue

        match user_selection:
            case 1:
                memory_stress_test()
            case 2:
                disk_stress_test()
            case 3:
                network_stress_test()
            case 4:
                cpu_stress_test()
            case 5:
                mysql_stress_test()

        next_round = input("\nFinished stress test. Another round? yes/no ")
        if next_round=="y" or next_round=="yes":
            continue

        if next_round == "n" or next_round=="no":
            print("n/no detected. Terminating program")
            break

        print("\ny/yes not detected. Program terminating")
        break


def sig_int(sig_number, framei):
    print("\nProgram Terminated")
    sys.exit(0)

if __name__=="__main__":
    signal.signal(signal.SIGINT, sig_int)
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram Terminated")
