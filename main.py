import os.path
from zipfile import ZipFile
import io

files_list = 'Files List.txt'
directory_to_extract_to = 'extract here'
file_path = 'Extract me.zip'


def get_zip_files(ref):
    zip_files = []
    for zip_file in ref.infolist():
        if zip_file.filename.endswith('.zip'):
            zip_files.append(zip_file.filename)
    return zip_files


def find_file():
    print(os.path.isfile(file_path))


def dig(archive_path, depth=0):
    with ZipFile(archive_path, 'r') as zip_ref:
        print(f'{zip_ref.infolist()[0].filename}')
        inner_zip_files = get_zip_files(zip_ref)
        if depth < 400 and len(inner_zip_files) != 0:
            for i, zip_file in enumerate(inner_zip_files):
                if i > 9:
                    break
                next_file = io.BytesIO(zip_ref.read(zip_file))
                dig(next_file, depth + 1)
        else:
            if not os.path.isdir(directory_to_extract_to):
                os.makedirs(directory_to_extract_to)
            with open(directory_to_extract_to + '\\' + files_list, 'w') as output_file:
                print(zip_ref.infolist()[0].filename)
                for file in zip_ref.infolist():
                    output_file.write(file.filename + '\n')
                if len(zip_ref.infolist()) < 50:
                    zip_ref.extractall(directory_to_extract_to)


if __name__ == '__main__':
    # find_file()
    with io.open(file_path, mode='r+b') as content:
        print(type(content))
        dig(content)
