import requests  #импортируем встроенный модуль пайтон с его методами для получения api по ссылке 

class APIClient:  # создаем класс 
    def __init__(self, base_url):  #конструктор 
        self.base_url = base_url #создаем атрибут класса 
    @staticmethod
    def get(url,results=1):
        try:
            response = requests.get(url, params={'results': results}) #вы полняют get запрос 
            response.raise_for_status()  # вызывает ошибку если запрос завершился ошибкой 404 или 500
            return response.json() #преобразовает ответ в формат json() и возвращает его 
        except requests.RequestException as e: # переъватывает ошибки 
           print(f"Error during API request: {e}") #выводит в ответ если находит ошбку
        return None 

