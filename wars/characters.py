from http_client import HTTPClient, Repository
import time

def timing_decorator(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        return result
    return wrapper


class StarWarsCharacters:
    def __init__(self, base_url, number_of_characters):
        self.http_client = HTTPClient(base_url)
        self.repository = Repository(self.http_client)
        self.number_of_characters = number_of_characters

    @timing_decorator
    def get_characters(self):
        raw_characters = self.repository.fetch_characters(self.number_of_characters)
        result = []
        for char in raw_characters:
            result.append({
                "name": char['name'],
                "height": char['height'],
                "mass": char['mass'],
                "birth_year": char['birth_year'],
                "gender": char['gender'],
                "homeworld": char['homeworld'],
                "films": char['films'],
            })
        return result
    
    
    
    
if __name__ == "__main__":
    star_wars_api = StarWarsCharacters("https://swapi.dev/api/", 5)
    characters = star_wars_api.get_characters()
    for character in characters:
        print(character)