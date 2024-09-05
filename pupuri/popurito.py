import os
import requests
from user_data import users



class FileFunctions:
    def __init__(self, directory):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    def create_file(self):
        file_name = input("Введите имя файла: ")
        file_format = input("Выберите формат файла (например, .txt): ")
        if not file_format.startswith('.'):
            print("Неверный формат файла.")
            return
        # content = users 
        result_string = ""
        for dictionary in users:
            result_string += str(dictionary) + "\n"
        with open(os.path.join(self.directory, file_name), 'w', encoding='utf-8') as f:
            f.write(result_string)
        print("Файл успешно создан.")
    
    def read_file(self):
        file_name = input("Введите имя файла, который хотите прочитать: ")
        if not os.path.isfile(os.path.join(self.directory, file_name1)): 
            print("Файл не найден.")
            return  
        with open(os.path.join(self.directory, file_name), 'r') as f:
            content = f.read()
        print("Содержимое файла: ")
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


class CommandInterface:
    def __init__(self,directory):
        self.file_manager = FileFunctions(directory)
    
    
    def run(self):
        while True:
            print(f"1 - Создать файл")
            print(f"2 - Прочитать файл")
            print(f"3 - Обновить файл")
            print(f"4 - Удалить файл")
            print(f"0 - Выход")
            human_choice = input("Введите цифру: ")
        
            if human_choice == "1":
                self.file_manager.create_file()
            elif human_choice == "2":
                self.file_manager.read_file()
            elif human_choice == "3":
                self.file_manager.update_file()
            elif human_choice == "4":
                self.file_manager.delete_file()
            elif human_choice == "0":
                print("Вы вышли из программы!")
                break
            else:
                ("Вы ввели не то число, введите еще раз!!!")
                
if __name__ == "__main__":
    app = CommandInterface("files")
    app.run()



            
            
        