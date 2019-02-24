import requests


class Habitica(object):

    BASE_HABITICA_URL = 'https://habitica.com/api/v3/'

    def __init__(self, user_id, api_key):
        self.user_id = user_id
        self.api_key = api_key
        self.auth_headers = {'x-api-user': user_id, 'x-api-key': api_key}

    def status(self):
        """
        Get Habitica's API status
        https://habitica.com/apidoc/#api-Status-GetStatus
        """
        url = self.BASE_HABITICA_URL + 'status'
        resp = requests.get(url, headers=self.auth_headers).json()['data']
        return resp


if __name__ == "__main__":
    habitica = Habitica("64df109a-d760-49ec-99a2-ab46f6682ffc", "e2c0f281-8edf-42e1-825e-3166e818b26f")

    print(habitica.status())

