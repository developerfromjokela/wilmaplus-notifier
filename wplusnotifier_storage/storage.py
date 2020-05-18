#  Copyright (c) 2020 wilmaplus-notifier, developed by Developer From Jokela, for Wilma Plus mobile app


import hashlib
from pathlib import Path
from .encryption import AESCipher

from django.conf import settings
import os


def get_saved_data(enc_key, filename, random_token, user_id):
    token_hash = hashlib.sha512(random_token.encode('UTF-8'))
    filename = filename + "_" + token_hash.digest().hex() + "."+hashlib.sha256(user_id.encode('UTF-8')).digest().hex()+".wplus_storage"
    savePathCheck(settings.STORAGE_DIR)
    file_path = Path(os.path.join(settings.STORAGE_DIR, filename))
    if file_path.is_file():
        f_content = open(file_path, 'r')
        content = f_content.read()
        decrypted_content = AESCipher(content, enc_key).decrypt()
        return decrypted_content
    return None


def save_data(content, enc_key, filename, random_token, user_id):
    token_hash = hashlib.sha512(random_token.encode('UTF-8'))
    filename = filename + "_" + token_hash.digest().hex() + "."+hashlib.sha256(user_id.encode('UTF-8')).digest().hex()+".wplus_storage"
    savePathCheck(settings.STORAGE_DIR)
    file_path = Path(os.path.join(settings.STORAGE_DIR, filename))
    if file_path.is_file():
        file_path.unlink()
    encrypted_content = AESCipher(content, enc_key).encrypt()
    f = open(file_path, "x")
    f.write(encrypted_content)
    f.close()


def savePathCheck(path):
    my_file = Path(path)
    if not my_file.is_dir():
        my_file.mkdir()
