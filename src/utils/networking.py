import requests

def create_session() -> requests.Session:
    return requests.Session()

def get(url: str, session: requests.Session) -> requests.Response:
    return session.get(url)
