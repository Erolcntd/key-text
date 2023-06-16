from cryptography.fernet import Fernet
import getpass
import os

KEY_FILE = "encryption.key"

def generate_key():
    if os.path.exists(KEY_FILE):
        return load_key()
    else:
        key = Fernet.generate_key()
        save_key(key)
        return key

def save_key(key):
    with open(KEY_FILE, "wb") as file:
        file.write(key)

def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()

def encrypt_message(fernet, message):
    try:
        return fernet.encrypt(message)
    except Exception as e:
        print("Encryption error:", str(e))

def decrypt_message(fernet, encrypted_message):
    try:
        return fernet.decrypt(encrypted_message)
    except Exception as e:
        print("Decryption error:", str(e))

def main():
    key = generate_key()
    fernet = Fernet(key)

    while True:
        print("Options:")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Key Management")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            message = input("Enter the message: ").encode("utf-8")
            encrypted_message = encrypt_message(fernet, message)
            if encrypted_message:
                print("Encrypted Message:", encrypted_message)
        elif choice == "2":
            encrypted_message = input("Enter the encrypted message: ")
            decrypted_message = decrypt_message(fernet, encrypted_message.encode("utf-8"))
            if decrypted_message:
                print("Decrypted Message:", decrypted_message.decode("utf-8"))
        elif choice == "3":
            print("Key management selected.")
            key_action = input("1. View Key\n2. Generate New Key\n3. Delete Key\nEnter your choice: ")

            if key_action == "1":
                print("Key:", key.decode("utf-8"))
            elif key_action == "2":
                confirmation = input("A new key will be generated. Do you want to proceed? (Y/N): ")

                if confirmation.lower() == "y":
                    key = generate_key()
                    fernet = Fernet(key)
                    print("New key generated.")
            elif key_action == "3":
                confirmation = input("The key will be deleted. Do you want to proceed? (Y/N): ")

                if confirmation.lower() == "y":
                    if os.path.exists(KEY_FILE):
                        os.remove(KEY_FILE)
                        print("Key deleted.")
                    else:
                        print("Key not found.")
            else:
                print("Invalid option.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
