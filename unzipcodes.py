import zipfile

def extract_zip(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as zip:
        zip.extractall(dest_dir)


if __name__ == '__main__':
    extract_zip("compressed.zip", r"C:\Users\PLNAPC\PycharmProjects\python_Project\todo-app\files")
