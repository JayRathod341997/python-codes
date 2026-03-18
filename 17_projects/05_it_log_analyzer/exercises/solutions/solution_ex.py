# ───────────────────────────────────────────────────────────────
# Solutions — Project 05: IT Log Analyzer
# ───────────────────────────────────────────────────────────────

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

def parse_log_line(line):
    parts = line.split()
    if len(parts) < 5:
        return None
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    ip = parts[3]
    message = " ".join(parts[4:])
    return (timestamp, level, ip, message)

print("\n" + "="*80)
print("EXERCISE 1 SOLUTION: First 5 ERROR Logs")
print("="*80 + "\n")

error_logs = []
for log_line in logs:
    parsed = parse_log_line(log_line)
    if parsed and parsed[1] == "ERROR":
        error_logs.append(parsed)

print(f"Total ERROR logs: {len(error_logs)}\n")
print("First 5 errors:")
for i, (ts, level, ip, msg) in enumerate(error_logs[:5], start=1):
    print(f"  {i}. {ts} {ip} — {msg}")

print("\n" + "="*80)
print("EXERCISE 2 SOLUTION: Errors by IP Address")
print("="*80 + "\n")

ip_error_count = {}
for log_line in logs:
    parsed = parse_log_line(log_line)
    if parsed and parsed[1] == "ERROR":
        ip = parsed[2]
        ip_error_count[ip] = ip_error_count.get(ip, 0) + 1

print("Error count by IP (top 5):")
sorted_ips = sorted(ip_error_count.items(), key=lambda x: x[1], reverse=True)
for rank, (ip, count) in enumerate(sorted_ips[:5], start=1):
    print(f"  {rank}. {ip}: {count} errors")

print("\n" + "="*80)
print("EXERCISE 3 SOLUTION: Warning Message Analysis")
print("="*80 + "\n")

warning_messages = {}
for log_line in logs:
    parsed = parse_log_line(log_line)
    if parsed and parsed[1] == "WARNING":
        msg = parsed[3]
        warning_messages[msg] = warning_messages.get(msg, 0) + 1

print("All warning messages:")
for msg, count in sorted(warning_messages.items(), key=lambda x: x[1], reverse=True):
    print(f"  "{msg}": {count} occurrence(s)")

if warning_messages:
    most_common = max(warning_messages.items(), key=lambda x: x[1])
    print(f"\nMost common warning:")
    print(f"  Message: "{most_common[0]}"")
    print(f"  Count: {most_common[1]}")

print("\n" + "="*80 + "\n")
