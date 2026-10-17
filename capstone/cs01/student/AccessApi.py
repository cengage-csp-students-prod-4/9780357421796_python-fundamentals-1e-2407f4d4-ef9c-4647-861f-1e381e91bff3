import requests


class AccessApi:
    """
    Class AccessApi is used to abstract lower level access to course required API

    Attributes
    ----------
    url : str
        A valid website used to hold the course's json files

    Methods
    -------
    url_active()
        returns True if the url is currently responding without errors, and False if not.

    get_end_point(end_point)
        returns the json output of the GET request

    get_status_code(end_point)
        returns the HTTP status code of the GET request

    get_elapsed_time(end_point)
        returns the elapsed time of the GET request in seconds
    """

    TIMEOUT: int = 30  # seconds; never let a request hang forever

    def __init__(self, url: str):
        """
        Parameters
        ----------
        url: str
           a valid website for example: http://google.com
        """
        self.url = url  # routed through the setter below

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        self._url = url

    def _get(self, end_point: str = "") -> requests.Response:
        """Send a GET request to base url + end_point and return the Response."""
        return requests.get(self._url + end_point, timeout=self.TIMEOUT)

    def url_active(self) -> bool:
        try:
            return self._get().ok
        except requests.exceptions.RequestException:
            return False

    def get_end_point(self, end_point: str) -> list:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        return self._get(end_point).json()

    def get_status_code(self, end_point: str) -> int:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        return self._get(end_point).status_code

    def get_elapsed_time(self, end_point: str) -> float:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        return self._get(end_point).elapsed.total_seconds()