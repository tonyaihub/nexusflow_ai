import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

class SecretManager:
    def __init__(self):
        # Генерируем ключ шифрования, если его нет
        self.key = os.getenv("ENCRYPTION_KEY", Fernet.generate_key())
        self.cipher = Fernet(self.key)

    def encrypt_key(self, api_key: str):
        return self.cipher.encrypt(api_key.encode()).decode()

    def decrypt_key(self, encrypted_key: str):
        return self.cipher.decrypt(encrypted_key.encode()).decode()

# Инициализация для использования в модулях
secrets = SecretManager()
