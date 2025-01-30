import os
import tempfile


def is_pdf(file_name):
    return file_name.endswith('.pdf')


def save_as_temp_file(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tf:
        tf.write(file.read())
        return tf


def delete_file(file_path):
    os.remove(file_path)
