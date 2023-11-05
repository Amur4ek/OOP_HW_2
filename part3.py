# Имена исходных файлов
file1_name = "1.txt"
file2_name = "2.txt"

# Открывает исходные файлы и считывает их содержимое
with open(file1_name, "r", encoding="utf-8") as file1, open(file2_name, "r", encoding="utf-8") as file2:
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

# Определяет количество строк в каждом файле
file1_lines_count = len(file1_lines)
file2_lines_count = len(file2_lines)

# Создает список кортежей, содержащих имя файла и количество строк
files_info = [(file1_name, file1_lines_count), (file2_name, file2_lines_count)]

# Сортирует список кортежей по количеству строк
sorted_files_info = sorted(files_info, key=lambda x: x[1])

# Открывает результирующий файл
with open("result.txt", "w") as result_file:
    # Перебирает отсортированные файлы
    for file_info in sorted_files_info:
        file_name, lines_count = file_info
        # Записывает служебную информацию в результирующий файл
        result_file.write(file_name + "\n")
        result_file.write(str(lines_count) + "\n")
        # Записывает содержимое файла в результирующий файл
        if file_name == file1_name:
            result_file.writelines(file1_lines)
        else:
            result_file.writelines(file2_lines)
        result_file.write("\n")
