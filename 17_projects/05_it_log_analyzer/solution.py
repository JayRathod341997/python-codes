# ─────────────────────────────────────────────────────────────────
# Project 05 — IT — DevOps Log Analyzer
# Concepts  : string methods, tuples, sets, dicts, sorted+lambda
# Difficulty: Intermediate
# ─────────────────────────────────────────────────────────────────

# ── Section 1: Hardcoded Log Data ──────────────────────────────────
logs = [
    "2024-01-15 10:23:45 ERROR 192.168.1.101 Database connection failed",
    "2024-01-15 10:25:12 INFO 192.168.1.102 User login successful",
    "2024-01-15 10:26:33 ERROR 192.168.1.101 Database timeout after 30s",
    "2024-01-15 10:27:01 WARNING 192.168.1.103 High memory usage detected",
    "2024-01-15 10:28:15 ERROR 192.168.1.104 API endpoint /users returned 500",
    "2024-01-15 10:29:42 INFO 192.168.1.105 Cache cleared successfully",
    "2024-01-15 10:30:11 ERROR 192.168.1.101 Database connection failed",
    "2024-01-15 10:31:22 WARNING 192.168.1.103 Disk space low (85%)",
    "2024-01-15 10:32:50 ERROR 192.168.1.106 API endpoint /products returned 500",
    "2024-01-15 10:33:15 INFO 192.168.1.102 Backup completed",
    "2024-01-15 10:34:41 ERROR 192.168.1.101 Database connection failed",
    "2024-01-15 10:35:30 WARNING 192.168.1.107 Slow query detected (5.2s)",
    "2024-01-15 10:36:12 ERROR 192.168.1.108 API endpoint /orders returned 500",
    "2024-01-15 10:37:55 INFO 192.168.1.109 Deployment completed successfully",
    "2024-01-15 10:38:20 ERROR 192.168.1.101 Database connection failed",
    "2024-01-15 10:39:10 WARNING 192.168.1.103 CPU usage high (90%)",
    "2024-01-15 10:40:30 ERROR 192.168.1.110 API endpoint /users returned 500",
    "2024-01-15 10:41:45 INFO 192.168.1.111 Service health check passed",
    "2024-01-15 10:42:15 ERROR 192.168.1.104 Database connection failed",
    "2024-01-15 10:43:50 WARNING 192.168.1.103 Replication lag detected (10s)",
]

print("\n" + "="*80)
print("DEVOPS LOG ANALYZER")
print("="*80)

# ── Section 2: Log Parser Function ─────────────────────────────────
# ── CONCEPT: String Methods (split, startswith, in) ────────────────
# We parse each log line by splitting on spaces.

def parse_log_line(line):
    """Parse a log line and extract timestamp, level, IP, and message."""
    parts = line.split()
    if len(parts) < 5:
        return None
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    ip = parts[3]
    message = " ".join(parts[4:])
    return (timestamp, level, ip, message)

# ── Section 3: Count Log Levels ────────────────────────────────────
# ── CONCEPT: Dict as frequency counter ────────────────────────────

level_count = {}
for log_line in logs:
    parsed = parse_log_line(log_line)
    if parsed:
        level = parsed[1]
        level_count[level] = level_count.get(level, 0) + 1

print("\nLOG LEVEL SUMMARY:")
print("─" * 80)
for level in sorted(level_count.keys()):
    print(f"  {level:<10}: {level_count[level]:>3} occurrences")

# ── Section 4: Top Error Messages ──────────────────────────────────
# ── CONCEPT: Dicts, sorted(), lambda ──────────────────────────────

error_messages = {}
for log_line in logs:
    parsed = parse_log_line(log_line)
    if parsed and parsed[1] == "ERROR":
        msg = parsed[3]
        error_messages[msg] = error_messages.get(msg, 0) + 1

print("\nTOP ERROR MESSAGES:")
print("─" * 80)
sorted_errors = sorted(error_messages.items(), key=lambda x: x[1], reverse=True)
for i, (msg, count) in enumerate(sorted_errors[:5], start=1):
    print(f"  {i}. {msg} ({count} times)")

# ── Section 5: Suspicious IPs (Many Errors) ────────────────────────
# ── CONCEPT: Sets for unique tracking, dicts for grouping ─────────

ip_errors = {}
suspicious_ips = set()

for log_line in logs:
    parsed = parse_log_line(log_line)
    if parsed and parsed[1] == "ERROR":
        ip = parsed[2]
        ip_errors[ip] = ip_errors.get(ip, 0) + 1
        if ip_errors[ip] >= 3:
            suspicious_ips.add(ip)

print("\nSUSPICIOUS IPS (3+ errors):")
print("─" * 80)
for ip in sorted(suspicious_ips):
    print(f"  {ip}: {ip_errors[ip]} errors")

# ── Section 6: All Unique IPs ──────────────────────────────────────
# ── CONCEPT: Set operations ────────────────────────────────────────

all_ips = set()
for log_line in logs:
    parsed = parse_log_line(log_line)
    if parsed:
        all_ips.add(parsed[2])

print("\nUNIQUE IPS IN LOGS:")
print("─" * 80)
print(f"  Total unique IPs: {len(all_ips)}")
for ip in sorted(all_ips):
    print(f"    {ip}")

print("\n" + "="*80 + "\n")
print("NOTE: We'll replace these loops in Project 10 using comprehensions.")
print("="*80 + "\n")
