import os

class FileFunctions:
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def create_file(self):
        
        file_format = input("Введите формат файла (например, .txt): ")
        if not file_format.startswith('.'):
            print("Неверный формат файла.")
            return
        file_name = f"file{file_format}"
        content = input("Введите текст, который хотите записать в файл: ")
        with open(os.path.join(self.directory, file_name), 'w') as f:
            f.write(content)
        print("Файл успешно создан.")

    def read_file(self):
        file_name = input("Введите имя файла, который хотите прочитать: ")
        if not os.path.isfile(os.path.join(self.directory, file_name)):
            print("Файл не найден.")
            return
        with open(os.path.join(self.directory, file_name), 'r') as f:
            content = f.read()
        print("Содержимое файла:")
        print(content)

    def update_file(self):
        file_name = input("Введите имя файла, который хотите обновить: ")
        if not os.path.isfile(os.path.join(self.directory, file_name)):
            print("Файл не найден.")
            return
        new_content = input("Введите новый текст для записи: ")
        with open(os.path.join(self.directory, file_name), 'w') as f:
            f.write(new_content)
        print("Файл успешно обновлен.")

    def delete_file(self):
        file_name = input("Введите имя файла, который хотите удалить: ")
        if not os.path.isfile(os.path.join(self.directory, file_name)):
            print("Файл не найден.")
            return
        os.remove(os.path.join(self.directory, file_name))
        print("Файл успешно удален.")

class App:
    def __init__(self, directory):
        self.file_manager = FileFunctions(directory)

    def run(self):
        while True:
            print("\nВыберите действие:")
            print("1 - Создать файл")
            print("2 - Прочитать файл")
            print("3 - Обновить файл")
            print("4 - Удалить файл")
            print("0 - Выход")
            choice = input("Ваш выбор: ")

            if choice == '1':
                self.file_manager.create_file()
            elif choice == '2':
                self.file_manager.read_file()
            elif choice == '3':
                self.file_manager.update_file()
            elif choice == '4':
                self.file_manager.delete_file()
            elif choice == '0':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    app = App("files")
    app.run()