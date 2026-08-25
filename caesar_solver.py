def brute_force_caesar(ciphertext):
    print(f"\n[+] Analyzing Ciphertext: {ciphertext}\n" + "-"*40)
    for shift in range(1, 26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                decrypted += chr((ord(char) - base - shift) % 26 + base)
            else:
                decrypted += char
        print(f"Shift -{shift:02d}: {decrypted}")

if __name__ == "__main__":
    target = input("Enter ciphertext (or text inside braces): ")
    brute_force_caesar(target)
