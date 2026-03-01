from datetime import datetime, timezone
import re


class PyHash:
    def generic_create_hash_file(self, algorithm, filename: str):
        result_hash = self.generic_return_hash(algorithm, filename)
        self.create_hash_file(algorithm, filename, result_hash)

    def generic_compare_file_hash(self, algorithm, filename, user_hash):
        file_hash = self.generic_return_hash(algorithm, filename)

        if user_hash == file_hash:
            print("O arquivo não foi alterado\n")

        else:
            print("O arquivos foi alterado\n")

    def generic_compare_hashes(self, algorithm, filename1, filename2):
        hash1 = self.generic_return_hash(algorithm, filename1)
        hash2 = self.generic_return_hash(algorithm, filename2)

        if hash1 == hash2:
            print("Arquivos são iguais\n")

        else:
            print("Arquivos diferentes\n")

    # Utils
    @staticmethod
    def create_hash(algorithm, filename: str) -> bytes:
        """
            Cria a hash do arquivo

            Args:
                algorithm (func) - Algoritimo usado para criar a hash (md5, sha1, sha256...)
                filename (str) - Nome do arquivo para se gerar a hash

            Return:
                Retorna a hash gerada fo arquivo (filename)
        """
        with open(filename, "rb") as file:
            data: bytes = file.read()
            algorithm.update(data)

        return algorithm.hexdigest()

    def create_hash_file(self, algorithm, filename: str, result_hash: bytes):
        """
            Cria o txt com os dados do arquivo

            Args:
                algorithm () - Algoritmo usado para criar a hash
                filename (str) - Nome do arquivo que foi heshado
                result_hash (bytes) - Hash do arquivo
        """
        timestamp = self.return_timestamp()
        hash_file_name: str = self.return_new_hash_file_name(algorithm, filename, timestamp)

        with open(hash_file_name, "w") as hash_file:
            hash_file.write(
                f"filename={filename}\n"
                f"timestamp={timestamp}\n"
                f"hash={result_hash}\n"
            )

    def generic_return_hash(self, algorithm, filename: str) -> bytes:
        """ Retorna a hash criada """
        result_hash: bytes = self.create_hash(algorithm, filename)

        print(
            f'filename="{filename}"\n'
            f'hash_{algorithm.name}="{result_hash}"\n'
        )
        return result_hash

    def return_new_hash_file_name(self, algorithm, filename: str, timestamp: str) -> str:
        """ Retorna o nome do arquivo com a hash """
        clean_name: str = self.return_clean_name(filename)
        return f"{algorithm.name}_{clean_name}_{timestamp}.txt"

    @staticmethod
    def return_clean_name(raw_name: str) -> str:
        """ Retorna o nome sem extensão e chars especiais """
        no_ext: str = raw_name.split(".")[0]
        clean_name: str = re.sub(r'[^A-Za-z0-9]', '_', no_ext)
        return clean_name

    @staticmethod
    def return_timestamp() -> str:
        """ Cria e retorna o timestamp """
        now: datetime = datetime.now(timezone.utc)
        timestamp: str = now.strftime("%Y%m%dT%H%M%S.%f") + "Z"
        return timestamp
