import requests


class TruenumbersArtifactApi:
    """
    Client for the Truenumbers Artifact API.

    This class wraps HTTP endpoints for artifact operations. Methods raise
    ``ValueError`` when required arguments are missing and ``Exception`` when
    the underlying HTTP request returns a status code >= 400.

    Example::

        api = TruenumbersArtifactApi(
            base_url="https://api.example.com/truenumbers-artifact-api",
            shared_headers={"Authorization": "Bearer <token>"},
        )
    """
    base_url = ""
    shared_headers = {
        # "Content-Type": "application/json",
        # "Accept": "application/json"
    }

    def __init__(self, *, base_url, shared_headers=None):
        """
        Initialize a new Truenumbers Artifact API client.

        Args:
            base_url (str): Base URL of the Artifact API. Required.
            shared_headers (dict, optional): Extra HTTP headers to send with every
                request (for example authentication headers). Supplied keys
                merge with the default ``shared_headers``.

        Raises:
            ValueError: If ``base_url`` is not provided.

        Example::

            api = TruenumbersArtifactApi(
                base_url="https://api.example.com/truenumbers-artifact-api",
            )
            api_auth = TruenumbersArtifactApi(
                base_url="https://api.example.com/truenumbers-artifact-api",
                shared_headers={"Authorization": "Bearer <token>"},
            )
        """
        if not base_url:
            raise ValueError("base_url is required")
        self.base_url = base_url
        if shared_headers:
            self.shared_headers.update(shared_headers)

    def get_artifact_by_id(self, *, id):
        """
        Get an artifact by ID.
        """
        url = f"{self.base_url}/v1/artifact/{id}"
        response = requests.get(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response
    
    def delete_artifact_by_id(self, *, id):
        """
        Delete an artifact by ID.
        """
        url = f"{self.base_url}/v1/artifact/{id}"
        response = requests.delete(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response

    def create_artifact(self, *, file_path):
        """
        Create an artifact.
        """
        url = f"{self.base_url}/v1/artifact"
        response = requests.post(url, headers=self.shared_headers, files={'file': open(file_path, 'rb')})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()