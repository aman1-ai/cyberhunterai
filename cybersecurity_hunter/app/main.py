from scanner import scan_device
from defense import activate_defense
from report import generate_report

def main():
    print("Starting Cybersecurity Hunter App")
    threats = scan_device()
    if threats:
        print("Threats Detected!")
        activate_defense(threats)
        generate_report(threats)
    else:
        print("No threats detected.")

if __name__ == "__main__":
    main()
