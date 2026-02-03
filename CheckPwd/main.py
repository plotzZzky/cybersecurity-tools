# Thanks to https://github.com/brannondorsey for making the rockyou.txt file available.
import os
from pathlib import Path
from urllib3 import request
import sys


class CheckPwd:
    """ Ferramenta que verifica se a sua senha está em bancos de senhas públicos """
    cli_desc: str = "Ferramenta para verificar se sua senha está no rockyou.txt"

    db_link: str = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
    db_path: Path = Path("Db/rockyou.txt")

    pwd: str = ""

    pwd_msg: str = (
        "\nA senha {} já consta no nosso banco de dados.\n"
        "Não recomendamos o uso de senha que ja foram vazadas."
    )
    not_found_pwd: str = "\nA senha {} não está no nossa banco de dados."

    def __init__(self):
        self.menu_options = [
            {"name": "Baixar o db", "func": self.check_if_db_exist},
            {"name": "Verificar senha", "func": self.receive_pwd},
            {"name": "Sair", "func": self.exit_cli},
        ]

    def welcome(self):
        print(f"{'_' * 25} CheckPwd {'_' * 25}")
        print(self.cli_desc)
        self.show_menu_options()

    def show_menu_options(self):
        print(f"\n{'.' * 20} Menu {'.' * 20}")

        for index, option in enumerate(self.menu_options, 1):
            print(f"{index}- {option['name']}")

        self.check_menu_option()

    def check_menu_option(self):
        try:
            option: str = input("\nDigite uma opção: ")

            self.menu_options[int(option) - 1]["func"]()

        except (IndexError, ValueError):
            print("\nOpção invalida!")
            self.check_menu_option()

        except KeyboardInterrupt:
            self.exit_cli()

    def check_if_db_exist(self):
        if not self.db_path.exists():
            self.download_db_from_web()

        else:
            print("\nDb já existe!")

        self.show_menu_options()

    def download_db_from_web(self):
        """ Salva o banco de dados(rockyou.txt) """
        print("\nBaixando o db...")

        Path("Db").mkdir(parents=True, exist_ok=True)
        result = request(url=self.db_link, method='GET')

        with open(self.db_path, 'w') as file:
            file.write(result.data.decode(errors='replace'))

        print("\nConcluido!")

    def receive_pwd(self):
        self.pwd: str = input("\nInsira sua senha: ") or 'welcome'
        self.open_pwd_dict()

    def open_pwd_dict(self):
        """
            - Tenta abrir o rockyou.txt
            - Se não achar o arquivo chama a função que baixa o
        """
        try:

            with open(self.db_path, "r", errors='replace') as file:
                self.check_all_pwd(file)

        except FileNotFoundError:
            self.download_db_from_web()
            self.open_pwd_dict()

    def check_all_pwd(self, file):
        """ Verifica cada senha no db para ver se é igual a digita pelo usuaário """
        for line in file.readlines():
            if line.strip() == self.pwd:
                print(self.pwd_msg.format(self.pwd))
                self.exit_menu() # Necessário para evitar que exiba as duas mensagens

        print(self.not_found_pwd.format(self.pwd))
        self.exit_menu()

    def exit_menu(self):
        option: str = input("\nTestar nova senha(Y/n):")

        if option.lower() == 'y':
            self.show_menu_options()

        else:
            self.exit_cli()

    @staticmethod
    def exit_cli():
        """ Separada da função exit_menu para não exibir o exit_menu ao selecionar sair no menu inicial """
        print("\nBye!")
        sys.exit()

app = CheckPwd()

if __name__ == "__main__":
    app.welcome()
