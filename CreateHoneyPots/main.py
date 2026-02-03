from  cryptography.fernet import Fernet
import random
import shutil
import os


class CreateHoneyPot:
    """
        Esta ferramenta gera honeypots para proteger os arquivos reais de um servidor
        * HoneysPots são arquivos falsos colocados nos locais onde os arquivos originais deveriam estar para confundir
         ou atrasar atacantes

        Objective:
        - Esse script deve ser executado em uma rotina com cron para gerar copias "falsas" dos arquvos originais 

        Steps:
        - Copia todos os arquivos da pasta real_files_path
        - Salva os na pasta honey_pot
        - Preenche os arquivos com ruido e depois os criptografa
        - Altera a extensão do arquivo para parecer que foi criptografado com gpg
        - A chave usada não é salva no sistema!!!
    """

     # Paths (test/ é um path ficticio para representar a raiz do sistema)
    honeypot_path: str = "test/home"
    real_files_path: str = "test/files"

    key = Fernet.generate_key()
    fernet = Fernet(key)

    def copy_real_files_to_honeypot_path(self):
        for root, dirs, files in os.walk(self.real_files_path):
            for filename in files:
                self.copy_file_to_new_path(root, filename)

        self.encrypt_all_files()

    def encrypt_all_files(self):
        for root, dirs, files in os.walk(self.honeypot_path):
            for filename in files:
                filepath = os.path.join(root, filename) # gera o path para os arquivos
                self.generate_noise_and_encrypt_file(filepath)

    def generate_noise_and_encrypt_file(self, filepath):
        with open(filepath, "rb") as f:
            data = bytearray(f.read())

        self.generate_noise_to_file(data)
        encrypted_data = self.fernet.encrypt(bytes(data))

        with open(filepath, "wb") as f:
            f.write(encrypted_data)

    @staticmethod
    def copy_file_to_new_path(root, filename):
         filepath = os.path.join(root, filename)  # gera o path para os arquivos
         new_path = root.replace("usr/files", "home")

         os.makedirs(new_path, exist_ok=True)
         # copia o arquivo e adiciona a extensão .gpp para parecer que foi criptografado com o gpg
         shutil.copy(str(filepath), f"{new_path}/{filename}.gpg")

    @staticmethod
    def generate_noise_to_file(data, size=70):
        # Quanto maior o size mais desfigurado o conteudo fica
         for _ in range(size):
             pos = random.randint(0, len(data) - 1)
             data[pos] = random.randint(0, 255)
         return data


app = CreateHoneyPot()

if __name__ == "__main__":
    app.copy_real_files_to_honeypot_path()
