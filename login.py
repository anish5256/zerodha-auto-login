import requests
import pyotp

class KiteAuthenticator:
    """
    This class is used to authenticate a user with Kite API.
    """
    BASE_URL = 'https://kite.zerodha.com/api'
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "x-kite-version": "2.9.3"
    }

    def __init__(self, user_id, password, pin):
        """
        Initialize the KiteAuthenticator class.

        Parameters:
        user_id (str): The user id
        password (str): The user password
        pin (str): The user pin
        """
        self.user_id = user_id
        self.password = password
        self.pin = pin

    def _get_session(self):
        """
        Get the session key.

        Returns:
        str: The session key
        """
        data = {"user_id": self.user_id, "password": self.password}
        url = f"{self.BASE_URL}/login"
        response = requests.post(url, data=data, headers=self.HEADERS)
        return response.cookies.get_dict()['kf_session']

    def _get_request_id(self, kf_session):
        """
        Get the request id.

        Parameters:
        kf_session (str): The session key

        Returns:
        dict: The cookies dictionary with session key
        """
        headers = {**self.HEADERS, "cookie": 'kf_session=' + kf_session, "x-kite-userid": self.user_id}
        url = f"{self.BASE_URL}/twofa"
        if len(str(self.pin)) > 6:
            self.pin = pyotp.TOTP(self.pin).now()
        data = {"user_id": self.user_id, "twofa_value": self.pin}
        response = requests.post(url, data=data, headers=headers)
        return response.cookies.get_dict()

    def authenticate(self):
        """
        Authenticate the user.

        Returns:
        dict: The cookies dictionary with session key
        """
        kf_session = self._get_session()
        cookies = self._get_request_id(kf_session)
        cookies['kf_session'] = kf_session
        return cookies
