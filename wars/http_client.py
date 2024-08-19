import requests
import time


class HTTPClient:
    def __init__(self, base_url):
        self.base_url = base_url
        
    def get(self, endpoint):
        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error during GET request: {e}")
            return None
        
        
class Repository:
    def __init__(self,http_client):
        self.http_client = http_client
        
    def fetch_characters(self, count):
        characters = []
        next_url = '/people/'
        
        while len(characters) < count and next_url is not None:
            data = self.http_client.get(next_url)
            if data and 'results' in data:
                characters.extend(data['results'])
                next_url = data.get('next')
            else:
                break
        return characters[:count]