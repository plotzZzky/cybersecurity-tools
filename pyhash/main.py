from hash import PyHash
import hashlib


class PyHashMenu(PyHash):
    def __init__(self):
        super().__init__()
        print(f"{'_' * 40} PyHash {'_' * 40}")

    # Create a hash file
    def create_hash_file_md5sum(self, filename: str):
        self.generic_create_hash_file(hashlib.md5(), filename)

    def create_hash_file_sha1sum(self, filename: str):
        self.generic_create_hash_file(hashlib.sha1(), filename)

    def create_hash_file_sha256sum(self, filename: str):
        self.generic_create_hash_file(hashlib.sha256(), filename)

    def create_hash_file_sha512sum(self, filename: str):
        self.generic_create_hash_file(hashlib.sha512(), filename)

    def create_hash_file_sha3_256sum(self, filename: str):
        self.generic_create_hash_file(hashlib.sha3_256(), filename)

    # Return and print file
    def return_hash_md5sum(self, filename: str):
        self.generic_return_hash(hashlib.md5(), filename)

    def return_hash_sha1sum(self, filename: str):
        self.generic_return_hash(hashlib.sha1(), filename)

    def return_hash_sha256sum(self, filename: str):
        self.generic_return_hash(hashlib.sha256(), filename)

    def return_hash_sha512sum(self, filename: str):
        self.generic_return_hash(hashlib.sha512(), filename)

    def return_hash_sha3_256sum(self, filename: str):
        self.generic_return_hash(hashlib.sha3_256(), filename)

    # Compare file with hash
    def compare_file_hash_md5sum(self, filename, user_hash):
        self.generic_compare_file_hash(hashlib.md5(), filename, user_hash)

    def compare_file_hash_sha1sum(self, filename, user_hash):
        self.generic_compare_file_hash(hashlib.sha1(), filename, user_hash)

    def compare_file_hash_sha256sum(self, filename, user_hash):
        self.generic_compare_file_hash(hashlib.sha256(), filename, user_hash)

    def compare_file_hash_sha512sum(self, filename, user_hash):
        self.generic_compare_file_hash(hashlib.sha512(), filename, user_hash)

    def compare_file_hash_sha3_256sum(self, filename, user_hash):
        self.generic_compare_file_hash(hashlib.sha3_256(), filename, user_hash)

    # Compare hashes files
    def compare_hashes_files_md5sum(self, filename1, filename2):
        self.generic_compare_hashes(hashlib.md5(), filename1, filename2)

    def compare_hashes_files_sha1sum(self, filename1, filename2):
        self.generic_compare_hashes(hashlib.sha1(), filename1, filename2)

    def compare_hashes_files_sha256sum(self, filename1, filename2):
        self.generic_compare_hashes(hashlib.sha256(), filename1, filename2)

    def compare_hashes_files_sha512sum(self, filename1, filename2):
        self.generic_compare_hashes(hashlib.sha512(), filename1, filename2)

    def compare_hashes_files_sha3_256sum(self, filename1, filename2):
        self.generic_compare_hashes(hashlib.sha3_256(), filename1, filename2)


py_hash = PyHashMenu()

if __name__ == "__main__":
    py_hash.compare_file_hash_sha256sum(
        "PyHash/file.txt",
        "e3b0c44298fc1c149afbf4c8996fx92427ae41e4649b934ca495991b7852b855"
    )
    py_hash.compare_hashes_files_sha256sum(
        "PyHash/file.txt",
        "PyHash/file2.txt"
    )
