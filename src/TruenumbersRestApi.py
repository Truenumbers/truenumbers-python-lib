import requests

class TruenumbersRestApi:
    base_url: str = ""
    shared_headers: dict = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, params: dict):
        if not params['base_url']:
            raise ValueError("base_url is required")
        self.base_url = params['base_url']
        if params['shared_headers']:
            self.shared_headers.update(params['shared_headers'])

    def tnql(self, numberspace: str, tnql: str, params: dict = {"limit": 100, "offset": 0}):
        url = f"{self.base_url}/v2/numberflow/tnql"
        json_payload = { "tnql": tnql}
        response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace, **params})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def tnql_group_by(self, numberspace: str, tnql: str, params: dict = {"limit": 100, "offset": 0}):
        url = f"{self.base_url}/v2/numberflow/tnql/group-by"
        json_payload = { "tnql": tnql}
        response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace, **params})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def create_numberspace(self, numberspace: str):
        url = f"{self.base_url}/v2/numberflow/numberspace"
        json_payload = { "numberspace": numberspace}
        response = requests.post(url, headers=self.shared_headers, json=json_payload)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def get_numberspaces(self):
        url = f"{self.base_url}/v2/numberflow/numberspace"
        response = requests.get(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def delete_numberspace(self, numberspace: str):
        url = f"{self.base_url}/v2/numberflow/numberspace"
        response = requests.delete(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def get_numberspace(self, numberspace: str):
        url = f"{self.base_url}/v2/numberflow/numberspace"
        response = requests.get(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def create_truenumbers_from_statement(self, numberspace: str, true_statement: str, params: dict = {"noReturn": False, "skipStore": False, "tags": []}):
        url = f"{self.base_url}/v2/numberflow/numbers"
        json_payload = { "trueStatement": true_statement, **params}
        response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def create_truenumbers_from_json(self, numberspace: str, truenumbers_json: str, params: dict = {"noReturn": False, "skipStore": False, "tags": []}):
        url = f"{self.base_url}/v2/numberflow/numbers"
        json_payload = { "truenumbers": truenumbers_json, **params}
        response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def delete_truenumbers(self, numberspace: str, tnql: str):
        url = f"{self.base_url}/v2/numberflow/numbers"
        json_payload = { "tnql": tnql}
        response = requests.delete(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def delete_truenumbers_by_id(self, numberspace: str, id: str):
        url = f"{self.base_url}/v2/numberflow/numbers/{id}"
        response = requests.delete(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def tag_truenumbers(self, numberspace: str, tnql: str, tags: list):
        url = f"{self.base_url}/v2/numberflow/numbers/tags"
        json_payload = { "tnql": tnql, "addTags": tags}
        response = requests.patch(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def remove_tags_from_truenumbers(self, numberspace: str, tnql: str, tags: list):
        url = f"{self.base_url}/v2/numberflow/numbers/tags"
        json_payload = { "tnql": tnql, "removeTags": tags}
        response = requests.patch(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def get_truenumber_by_id(self, numberspace: str, id: str):
        url = f"{self.base_url}/v2/numberflow/numbers/{id}"
        response = requests.get(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def tag_truenumber_by_id(self, numberspace: str, id: str, tags: list):
        url = f"{self.base_url}/v2/numberflow/numbers/{id}/tags"
        json_payload = { "addTags": tags}
        response = requests.patch(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def remove_tags_from_truenumber_by_id(self, numberspace: str, id: str, tags: list):
        url = f"{self.base_url}/v2/numberflow/numbers/{id}/tags"
        json_payload = { "removeTags": tags}
        response = requests.patch(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def update_truenumber_values_by_statement(self, numberspace: str, true_statement: str, tags: list[str]):
        url = f"{self.base_url}/v2/numberflow/numbers/value"
        json_payload = { "trueStatement": true_statement, "tags": tags}
        response = requests.put(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def update_truenumber_values_by_json(self, numberspace: str, truenumbers_json: str, tags: list[str]):
        url = f"{self.base_url}/v2/numberflow/numbers/value"
        json_payload = { "truenumbers": truenumbers_json, "tags": tags}
        response = requests.put(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def batched_truenumber_operations(self, numberspace: str, operations: list[dict]):
        url = f"{self.base_url}/v2/numberflow/batch"
        json_payload = { "operations": operations}
        response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def get_saved_queries(self, numberspace: str):
        url = f"{self.base_url}/v2/numberflow/queries"
        response = requests.get(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def create_saved_query(self, numberspace: str, payload: dict):
        url = f"{self.base_url}/v2/numberflow/queries"
        response = requests.post(url, headers=self.shared_headers, json=payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def update_saved_query(self, numberspace: str, id: str, payload: dict):
        url = f"{self.base_url}/v2/numberflow/queries/{id}"
        response = requests.put(url, headers=self.shared_headers, json=payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def delete_saved_query(self, numberspace: str, id: str):
        url = f"{self.base_url}/v2/numberflow/queries/{id}"
        response = requests.delete(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def execute_saved_query_by_id(self, numberspace: str, id: str):
        url = f"{self.base_url}/v2/numberflow/queries/{id}/results"
        response = requests.get(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def login_user(self, email: str, password: str, organization: str):
        url = f"{self.base_url}/v2/users/login"
        json_payload = { "email": email, "password": password, "productCode": organization}
        response = requests.post(url, headers=self.shared_headers, json=json_payload)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def register_user(self, email: str, password: str, organization: str):
        url = f"{self.base_url}/v2/users/register"
        json_payload = { "email": email, "password": password, "productCode": organization}
        response = requests.post(url, headers=self.shared_headers, json=json_payload)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def verify_user(self):
        url = f"{self.base_url}/v2/users/verify"
        response = requests.get(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    