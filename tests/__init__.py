import time
delay=0.0001

def memory_stress_test():
    memory_bank = []
    print("Starting memory stress test\n")
    while True:
        memory_bank.append("dfdsfsdfdsfdsf"*525)
        time.sleep(delay)

def disk_stress_test():
    print("Does disk stress test")

def network_stress_test():
    print("Does network stress test")

def cpu_stress_test():
    print("Does cpu stress test")

def mysql_stress_test():
    print("Does MySQL stress test")
