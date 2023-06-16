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
        print("Şifreleme hatası:", str(e))

def decrypt_message(fernet, encrypted_message):
    try:
        return fernet.decrypt(encrypted_message)
    except Exception as e:
        print("Şifre çözme hatası:", str(e))

def main():
    key = generate_key()
    fernet = Fernet(key)

    while True:
        print("Seçenekler:")
        print("1. Mesajı Şifrele")
        print("2. Şifreli Mesajı Çöz")
        print("3. Anahtar Yönetimi")
        print("4. Çıkış")

        choice = input("Seçiminizi girin: ")

        if choice == "1":
            message = input("Mesajı girin: ").encode("utf-8")
            encrypted_message = encrypt_message(fernet, message)
            if encrypted_message:
                print("Şifrelenmiş Mesaj:", encrypted_message)
        elif choice == "2":
            encrypted_message = input("Şifreli mesajı girin: ")
            decrypted_message = decrypt_message(fernet, encrypted_message.encode("utf-8"))
            if decrypted_message:
                print("Çözülmüş Mesaj:", decrypted_message.decode("utf-8"))
        elif choice == "3":
            print("Anahtar yönetimi seçildi.")
            key_action = input("1. Anahtarı Görüntüle\n2. Yeni Anahtar Oluştur\n3. Anahtarı Sil\nSeçiminizi girin: ")

            if key_action == "1":
                print("Anahtar:", key.decode("utf-8"))
            elif key_action == "2":
                confirmation = input("Yeni bir anahtar oluşturulacak. Devam etmek istiyor musunuz? (E/H): ")

                if confirmation.lower() == "e":
                    key = generate_key()
                    fernet = Fernet(key)
                    print("Yeni anahtar oluşturuldu.")
            elif key_action == "3":
                confirmation = input("Anahtar silinecek. Devam etmek istiyor musunuz? (E/H): ")

                if confirmation.lower() == "e":
                    if os.path.exists(KEY_FILE):
                        os.remove(KEY_FILE)
                        print("Anahtar silindi.")
                    else:
                        print("Anahtar bulunamadı.")
            else:
                print("Geçersiz seçenek.")
        elif choice == "4":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
