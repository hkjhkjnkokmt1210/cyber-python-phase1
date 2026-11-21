import hashlib
class PasswordAuditor :
    def __init__(self, min_length=8):
        self.min_length = min_length

    def check_strength(self, password):
        score = 0;
        if len(password) >= self.min_length:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in r"!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for c in password):
            score += 1

        if score == 4 :
            return "STRONG"
        elif score < 2:
            return "WEAK"
        else:
            return "MEDIUM"

    def hash_sha256(self, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return hashed

if __name__ == "__main__":
    auditor = PasswordAuditor(min_length=8)
    mk = ["123456", "Admin123", "Cyber@2026"]
    for password in mk:
        mucdo = auditor.check_strength(password)
        hashed_password = auditor.hash_sha256(password)
        print(f"Password: {password}, Strength: {mucdo}, Hashed: {hashed_password}")
