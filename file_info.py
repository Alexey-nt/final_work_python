import os
import logging
from collections import namedtuple

logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(message)s', encoding='utf-8')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_file_info(file_path):
    try:
        files_info = []

        for i in os.listdir(file_path):
            full_path = os.path.join(file_path, i)

            if os.path.isdir(full_path):
                name, extension = os.path.splitext(i)
                files_info.append(
                    FileInfo(name=name,
                             extension='',
                             is_directory=True,
                             parent_directory=file_path))
            else:
                name, extension = os.path.splitext(i)
                files_info.append(FileInfo(name=name,
                                           extension=extension,
                                           is_directory=False,
                                           parent_directory=file_path))

        return files_info
    except Exception as e:
        logging.error(f'Ошибка в получении информации о файле: {e}', exc_info=True)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Команда для запуска: python file_info.py <directory_path>')
        sys.exit(1)

    directory_path = sys.argv[1]

    files_info = get_file_info(directory_path)

    if files_info:
        for file_info in files_info:
            logging.info(f'\n Имя файла: {file_info.name}\n Расширение файла: {file_info.extension}'
                         f'\n Это директория?: {file_info.is_directory}\n Родительская директория: {file_info.parent_directory}')
    else:
        logging.warning('Пустая директория.')
