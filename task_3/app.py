import asyncio
from database import Database
from logger import log_action

class App:
    def __init__(self):
        self.db = Database()

    async def start(self):
        await self.db.connect()
        await self.run()
        await self.db.close()

    @log_action
    async def create_record(self):
        content = input("Введите данные для новой записи: ")
        record_id = await self.db.create_record(content)
        print(f"Запись с ID {record_id} успешно создана.")

    @log_action
    async def read_record(self):
        record_id = input("Введите идентификатор записи: ")
        record = await self.db.read_record(record_id)
        if record:
            print(f"Содержимое записи: {record['content']}")
        else:
            print("Запись не найдена.")

    @log_action
    async def update_record(self):
        record_id = input("Введите идентификатор записи: ")
        if await self.db.read_record(record_id):
            new_content = input("Введите новые данные: ")
            await self.db.update_record(record_id, new_content)
            print("Запись успешно обновлена.")
        else:
            print("Запись не найдена.")

    @log_action
    async def delete_record(self):
        record_id = input("Введите идентификатор записи: ")
        if await self.db.read_record(record_id):
            await self.db.delete_record(record_id)
            print("Запись успешно удалена.")
        else:
            print("Запись не найдена.")

    async def run(self):
        while True:
            print("\nВыберите действие:")
            print("1 - Создать запись")
            print("2 - Прочитать запись")
            print("3 - Обновить запись")
            print("4 - Удалить запись")
            print("5 - Выход")

            choice = input("Ваш выбор: ")
            if choice == '1':
                await self.create_record()
            elif choice == '2':
                await self.read_record()
            elif choice == '3':
                await self.update_record()
            elif choice == '4':
                await self.delete_record()
            elif choice == '5':
                break
            else:
                print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    app = App()

    # Запуск основного цикла асинхронного приложения
    asyncio.run(app.start())