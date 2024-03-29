import os
import sys

def search_file(filename):
    # Получаем текущую директорию, в которой находится файл программы
    current_dir = os.getcwd()
    
    # Рекурсивно ищем файл в текущей и всех поддиректориях
    for root, dirs, files in os.walk(current_dir):
        if filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'r') as file:
                # Выводим первые 5 строк файла
                for _ in range(5):
                    line = file.readline()
                    if not line:
                        break
                    print(line, end='')
            return
    
    # Если файл не найден, выводим сообщение
    print(f"File {filename} not found.")

search_file('test.txt')