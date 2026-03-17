import requests

class TruenumbersArtifactApi:
    """
    TruenumbersArtifactApi class for interacting with the Truenumbers Artifact API.
    """
    base_url: str = ""
    shared_headers: dict = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    def __init__(self, **kwargs):
        """
        Initializes the TruenumbersArtifactApi.
        :param base_url: str (required) - The base URL of the Truenumbers Artifact API.
        :param shared_headers: dict (optional) - The shared headers to be used for all requests.
        """
        base_url = kwargs.get("base_url")
        if not base_url:
            raise ValueError("base_url is required")
        self.base_url = base_url
        shared_headers = kwargs.get("shared_headers")
        if shared_headers:
            self.shared_headers.update(shared_headers)
