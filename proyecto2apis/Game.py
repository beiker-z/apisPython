import requests
from requests.exceptions import HTTPError
from PIL import Image
from io import BytesIO

"""
@author: Anthony Vasquez
"""

class Game:

    def __init__(self, client_id: str, client_secret: str):
        self.json = dict()
        self._token = ""
        self._client_id = client_id
        self._client_secret = client_secret

    def get_credentials(self):
        url = "https://id.twitch.tv/oauth2/token?client_id={0}&client_secret={1}&grant_type=client_credentials".format(
            self._client_id, self._client_secret)
        response = requests.post(url=url)
        response.raise_for_status()
        json = response.json()
        self._token = json["access_token"]

    def get_info_game(self, name: str):
        url = "https://api.igdb.com/v4/games"
        headers = {"Client-ID": self._client_id,
                   "Authorization": "Bearer {0}".format(self._token), "Accept": "application/json"}
        data = 'fields name, genres, platforms, total_rating, release_dates, screenshots; search "{0}";'.format(
            name)
        response = requests.post(url=url, data=data, headers=headers)
        response.raise_for_status()
        self.json = response.json()

    def get_image(self, id: int):
        url = "https://api.igdb.com/v4/screenshots"
        headers = {"Client-ID": self._client_id,
                   "Authorization": "Bearer {0}".format(self._token), "Accept": "application/json"}
        data = 'fields url;where id = {0};'.format(id)
        response = requests.post(url=url, data=data, headers=headers)
        response.raise_for_status()
        url_img = "https:{0}".format(response.json()[0]["url"])
        response_image = requests.get(url=url_img)
        response_image.raise_for_status()
        return BytesIO(response_image.content)


game = Game(client_id="c8lqxkwl3d0aq4myzjcemt1s8xgfsd",
            client_secret="foagtapyb4xmlgmimo9zrn7np2b7kg")
try:
    game.get_credentials()
    game.get_info_game("Contra: The War of the Worlds")
    print("Game Info:", game.json)
    id = game.json[0]["screenshots"][0]
    image = game.get_image(id)
    img = Image.open(image)
    img.show()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
