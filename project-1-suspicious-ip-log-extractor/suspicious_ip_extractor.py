
import re
from collections import Counter

# Open and read the log file
with open("sample_log.txt", "r") as file:
    logs = file.readlines()

# Regular expression to find IP addresses
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Extract all IP addresses
ip_addresses = []

for line in logs:
    found_ips = re.findall(ip_pattern, line)
    ip_addresses.extend(found_ips)

# Count frequency of each IP
ip_count = Counter(ip_addresses)

# Define suspicious threshold
threshold = 3

print("=== Suspicious IP Analysis Report ===\n")

report_lines = []
report_lines.append("=== Suspicious IP Analysis Report ===\n")

for ip, count in ip_count.items():
    if count >= threshold:
        message = f"[ALERT] Suspicious IP Detected: {ip} appeared {count} times."
        print(message)
        report_lines.append(message)

print("\n=== All IP Frequency Count ===\n")
report_lines.append("\n=== All IP Frequency Count ===\n")

for ip, count in ip_count.items():
    message = f"{ip} --> {count} occurrences"
    print(message)
    report_lines.append(message)

# Save report to file
with open("report.txt", "w") as report:
    for line in report_lines:
        report.write(line + "\n")

print("\nReport has been saved to report.txt")
