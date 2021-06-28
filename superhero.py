import requests


class SuperHero:
    url = 'https://superheroapi.com/api/2619421814940190/search'


    def __init__(self, name):
        self.name = name
        response = requests.get(f'{SuperHero.url}/{self.name}')
        if response.status_code != 200:
            raise RuntimeError(f'Ошибка: {response.status_code}')
        self.info = response.json()['results'][0]


    def powerstats(self, name_stat):
        powerstats = self.info['powerstats']
        return powerstats[name_stat]


    def __str__(self):
        return self.name


Hulk = SuperHero('Hulk')
Captain = SuperHero('Captain America')
Thanos = SuperHero('Thanos')
heroes = [Hulk, Captain, Thanos]


most_intelligence = sorted(heroes, key=lambda hero: hero.powerstats('intelligence'))[0]
print(most_intelligence)

