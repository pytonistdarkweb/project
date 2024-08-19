from api_client import APIClient #импортируем из модуля (api_client) класс (APIClient) который запрашивает данные API

class UserData: # СОЗДАЕМ КЛАСС
    def __init__(self, url, count):  # УКАЗЫВАЕМ ПАРАМЕТРЫ 
        self.url = url  #Сохраняет URL
        self.count = count  #Сохраняет требуемое количество пользователей
        self.api_client = APIClient(self.url) # СОЗДАЕТ ЭКЗЕМПЛЯР КЛАССА (APIClient) ДЛЯ РАБОТЫ С НИМ 

    def fetch_users(self):
        users = []  #СОЗДАЕМ ПУСТОЙ СПИСОК ДЛЯ ДАЛЬНЕЙШЕЙ РАБОТЫ С НИМ
        while len(users) < self.count:  #СОЗДАЕМ ЦИКЛ КОТОРЫЙ БУДЕТ РАБОТАТЬ ДО ТОГО ПОКА ДЛИНА СПИСКА НЕ ДОСТИГНЕТ ЗНАЧЕНИЯ (COUNT)
            result = self.api_client.get("https://randomuser.me/api/", results=self.count - len(users))  #ЗАПРАШИВАЕТ У API КОЛЛИЧЕСТВО ОСТАВШИХСЯ ПОЛЬЗОВАТЕЛЕЙ 
            if result:  #ПРОВЕРЯЕТ ЯВЛЯЕТСЯ ЛИ ПУСТОЙ ПЕРЕМЕННАЯ 
                for user in result.get('results', []):#Извлекает список пользователей из result с помощью метода get, который возвращает значение по ключу 'results'. Если ключ не найден, возвращается пустой список []. Цикл проходит по каждому элементу (пользователю) этого списка.
                    user_info = {  #Создает словарь user_info, в который помещает информацию о поле,
                        "gender": user.get("gender"),
                        "name": user.get("name"),
                        "email": user.get("email"),
                        "location": user.get("location"),
                        "dob": user.get("dob"),
                        "phone": user.get("phone")
                    }
                    users.append(user_info)  #Добавляет словарь user_info в список users, который накапливает информацию о всех пользователях, полученных из API.
            if len(users) >= self.count:  #Проверяет, достигнуто ли желаемое количество пользователей (значение self.count).
                break
        return users  # ВОЗВРАЩАЕТ СПИСОК ПОЛЬЗОВАТЕЛЕЙ 

if __name__ == '__main__':
    api_url = "https://randomuser.me/api/"
    num_users = 5  # количество пользователей для получения
    
    user_data = UserData(api_url, num_users)
    users = user_data.fetch_users()
    print(users)
  
   
