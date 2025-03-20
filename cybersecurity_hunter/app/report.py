def generate_report(threats):
    with open("report.txt", "w") as f:
        f.write("Cybersecurity Report\n")
        f.write("Detected Threats:\n")
        for threat in threats:
            f.write(f"- {threat}\n")
    print("Report generated: report.txt")
