import json


class SSHLogAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.failed_counts = {}  # Lưu kết quả đếm dùng chung cho toàn bộ class

    def parse_logs(self):
        self.failed_counts = {}  # Reset lại mỗi lần gọi hàm để tránh cộng dồn sai
        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                # Kiểm tra trực tiếp trên cả dòng (không dùng vòng lặp for word nữa)
                if "Failed password" in line:
                    ip = line.split("from", 1)[1].split()[0]
                    if ip in self.failed_counts:
                        self.failed_counts[ip] += 1
                    else:
                        self.failed_counts[ip] = 1

        return self.failed_counts

    def get_suspicious_ips(self, threshold=3):
        suspicious_list = []
        for ip, count in self.failed_counts.items():
            if count >= threshold:
                # Kiểm tra điều kiện lớn nhất (>= 5) trước
                severity = "HIGH" if count >= 5 else "MEDIUM"
                suspicious_list.append({
                    "ip_address": ip,
                    "failed_attempts": count,
                    "severity": severity
                })
        return suspicious_list

    def export_json(self, output_file="report.json", threshold=3):
        alerts = self.get_suspicious_ips(threshold=threshold)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(alerts, f, indent=4)


if __name__ == "__main__":
    analyzer = SSHLogAnalyzer("sample_auth.log")
    counts = analyzer.parse_logs()
    print("Tong hop so lan dang nhap sai:", counts)

    suspicious = analyzer.get_suspicious_ips(threshold=3)
    print("Danh sach IP dang ngo:", suspicious)

    analyzer.export_json("report.json", threshold=3)
    print("Da xuat bao cao thanh cong ra file report.json!")