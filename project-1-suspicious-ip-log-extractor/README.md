# Project 1 — Suspicious IP Log Extractor

## Overview

This Python security automation project was developed to simulate a lightweight SOC-style log investigation process by automatically extracting IP addresses from connection logs, counting repeated occurrences, and flagging suspicious repeated activity.

The purpose of this project is to demonstrate how Python can be used to automate repetitive log review tasks that would otherwise require manual inspection by a security analyst.

---

## Project Files

- `sample_log.txt` → simulated network and SSH login activity logs
- `suspicious_ip_extractor.py` → Python script for IP extraction and suspicious activity detection
- `report.txt` → generated suspicious IP frequency report

---

## Detection Logic

The script performs the following operations:

1. Reads the raw log file line by line
2. Uses Regular Expressions (Regex) to extract all IPv4 addresses
3. Counts how many times each IP appears
4. Flags any IP appearing 3 or more times as suspicious
5. Generates a final investigation report

---

## Example Detection Result

The script successfully identified:

- `185.220.101.45`

as the most suspicious IP address after appearing 6 times in repeated failed SSH login attempts, indicating likely brute-force probing behavior.

---

## Skills Demonstrated

- Python file handling
- Regular Expressions (Regex)
- Security log parsing
- IOC extraction
- Frequency-based anomaly detection
- Automated report generation

---

This project forms the first artifact in the Python Security Automation Lab portfolio series.
