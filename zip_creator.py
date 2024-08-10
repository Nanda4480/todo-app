import zipfile
import pathlib
def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w' ) as archive:
        for filepath in filepaths:
            archive.write(filepath)

if __name__ == '__main__':
    make_archive(filepaths=["list.py", "miles per gallon.py"], dest_dir="zipfolder")

