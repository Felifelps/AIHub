import os


def is_pdf(file_name):
    return file_name.endswith('.pdf')

def save_file(file, file_path):
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

def delete_file(file_path):
    os.remove(file_path)
