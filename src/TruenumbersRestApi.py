import requests

class TruenumbersRestApi:
    """ 
    TruenumbersRestApi class for interacting with the Truenumbers REST API.
    """
    base_url: str = ""
    shared_headers: dict = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, **kwargs):
        """
        Args:
            base_url: str
            shared_headers: dict - Headers to send in all requests made within this class.
        Returns:
            None
        """
        base_url = kwargs.get("base_url")
        if not base_url:
            raise ValueError("base_url is required")
        self.base_url = base_url
        shared_headers = kwargs.get("shared_headers")
        if shared_headers:
            self.shared_headers.update(shared_headers)
    
    def tnql(self, **kwargs):
        """
        Executes a TNQL query.
        :param numberspace: str (required) - The numberspace to execute the TNQL query on.
        :param tnql: str (required) - The TNQL query to execute.
        :param limit: int (optional) - The number of results to return. default is 100.
        :param offset: int (optional) - The offset of the results to return. default is 0.
        Returns:
            dict - The result of the TNQL query.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        tnql = kwargs.get("tnql")
        if not tnql:
            raise ValueError("tnql is required")
        params = {
            "limit": kwargs.get("limit", 100),
            "offset": kwargs.get("offset", 0)
        }
        url = f"{self.base_url}/v2/numberflow/tnql"
        json_payload = { "tnql": tnql }
        response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace, **params})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def tnql_group_by(self, **kwargs):
        """
        Executes a TNQL group by query.
        :param numberspace: str (required) - The numberspace to execute the TNQL group by query on.
        :param tnql: str (required) - The TNQL query to execute.
        :param limit: int (optional) - The number of results to return. default is 100.
        :param offset: int (optional) - The offset of the results to return. default is 0.
        Returns:
            dict - The result of the TNQL group by query.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        tnql = kwargs.get("tnql")
        if not tnql:
            raise ValueError("tnql is required")
        params = {
            "limit": kwargs.get("limit", 100),
            "offset": kwargs.get("offset", 0)
        }
        url = f"{self.base_url}/v2/numberflow/tnql/group-by"
        json_payload = { "tnql": tnql }
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

    def create_truenumbers_from_statement(self, **kwargs):
        """
        Creates truenumbers from a true statement.
        :param numberspace: str (required) - The numberspace to create the truenumbers in.
        :param true_statement: str (required) - The true statement to create the truenumbers from.
        :param noReturn: bool (optional) - Whether to return the truenumbers. default is False.
        :param skipStore: bool (optional) - Whether to skip storing the truenumbers. default is False.
        :param tags: list (optional) - The tags to add to the truenumbers. default is [].
        Returns:
            dict - The result of the truenumbers creation.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        true_statement = kwargs.get("true_statement")
        if not true_statement:
            raise ValueError("true_statement is required")
        params = {
            "noReturn": kwargs.get("noReturn", False),
            "skipStore": kwargs.get("skipStore", False),
            "tags": kwargs.get("tags", [])
        }
        url = f"{self.base_url}/v2/numberflow/numbers"
        json_payload = { "trueStatement": true_statement, **params}
        response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

        def create_truenumbers_from_json(self, **kwargs):
            """
            Creates truenumbers from a JSON payload.
            :param numberspace: str (required) - The numberspace to create the truenumbers in.
            :param truenumbers_json: str (required) - The JSON payload to create the truenumbers from.
            :param noReturn: bool (optional) - Whether to return the truenumbers. default is False.
            :param skipStore: bool (optional) - Whether to skip storing the truenumbers. default is False.
            :param tags: list (optional) - The tags to add to the truenumbers. default is [].
            Returns:
                dict - The result of the truenumbers creation.
            """
            numberspace = kwargs.get("numberspace")
            if not numberspace:
                raise ValueError("numberspace is required")
            truenumbers_json = kwargs.get("truenumbers_json")
            if not truenumbers_json:
                raise ValueError("truenumbers_json is required")
            params = {
                "noReturn": kwargs.get("noReturn", False),
                "skipStore": kwargs.get("skipStore", False),
                "tags": kwargs.get("tags", [])
            }   
            url = f"{self.base_url}/v2/numberflow/numbers"
            json_payload = { "truenumbers": truenumbers_json, **params}
            response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
            if response.status_code >= 400:
                raise Exception(f"Error: {response.status_code} {response.text}")
            return response.json()

    def delete_truenumbers(self, **kwargs):
        """
        Deletes truenumbers from a numberspace.
        :param numberspace: str (required) - The numberspace to delete the truenumbers from.
        :param tnql: str (required) - The TNQL query to delete the truenumbers from.
        Returns:
            dict - The result of the truenumbers deletion.
        """
        url = f"{self.base_url}/v2/numberflow/numbers"
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        tnql = kwargs.get("tnql")
        if not tnql:
            raise ValueError("tnql is required")
        json_payload = { "tnql": tnql}
        response = requests.delete(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def delete_truenumbers_by_id(self, **kwargs):
        """
        Deletes truenumbers from a numberspace by ID.
        :param numberspace: str (required) - The numberspace to delete the truenumbers from.
        :param id: str (required) - The ID of the truenumbers to delete.
        Returns:
            dict - The result of the truenumbers deletion.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        url = f"{self.base_url}/v2/numberflow/numbers/{id}"
        response = requests.delete(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def tag_truenumbers(self, **kwargs):
        """
        Tags truenumbers.
        :param numberspace: str (required) - The numberspace to tag the truenumbers in.
        :param tnql: str (required) - The TNQL query to tag the truenumbers with.
        :param tags: list[str] (required) - The tags to add to the truenumbers.
        Returns:
            dict - The result of the truenumbers tagging.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        tnql = kwargs.get("tnql")
        if not tnql:
            raise ValueError("tnql is required")
        tags = kwargs.get("tags")
        if not tags:
            raise ValueError("tags is required")
        url = f"{self.base_url}/v2/numberflow/numbers/tags"
        json_payload = { "tnql": tnql, "addTags": tags}
        response = requests.patch(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def remove_tags_from_truenumbers(self, **kwargs):
        """
        Removes tags from truenumbers.
        :param numberspace: str (required) - The numberspace to remove the tags from.
        :param tnql: str (required) - The TNQL query to remove the tags from.
        :param tags: list[str] (required) - The tags to remove from the truenumbers.
        Returns:
            dict - The result of the truenumbers tagging.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        tnql = kwargs.get("tnql")
        if not tnql:
            raise ValueError("tnql is required")
        tags = kwargs.get("tags")
        if not tags:
            raise ValueError("tags is required")
        url = f"{self.base_url}/v2/numberflow/numbers/tags"
        json_payload = { "tnql": tnql, "removeTags": tags}
        response = requests.patch(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def get_truenumber_by_id(self, **kwargs):
        """
        Gets a truenumber by ID.
        :param numberspace: str (required) - The numberspace to get the truenumber from.
        :param id: str (required) - The ID of the truenumber to get.
        Returns:
            dict - The result of the truenumber retrieval.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        url = f"{self.base_url}/v2/numberflow/numbers/{id}"
        response = requests.get(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def tag_truenumber_by_id(self, **kwargs):
        """
        Tags a truenumber by ID.
        :param numberspace: str (required) - The numberspace to tag the truenumber in.
        :param id: str (required) - The ID of the truenumber to tag.
        :param tags: list[str] (required) - The tags to add to the truenumber.
        Returns:
            dict - The result of the truenumber tagging.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        tags = kwargs.get("tags")
        if not tags:
            raise ValueError("tags is required")
        url = f"{self.base_url}/v2/numberflow/numbers/{id}/tags"
        json_payload = { "addTags": tags}
        response = requests.patch(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def remove_tags_from_truenumber_by_id(self, **kwargs):
        """
        Removes tags from a truenumber by ID.
        :param numberspace: str (required) - The numberspace to remove the tags from.
        :param id: str (required) - The ID of the truenumber to remove the tags from.
        :param tags: list[str] (required) - The tags to remove from the truenumber.
        Returns:
            dict - The result of the truenumber tagging.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        tags = kwargs.get("tags")
        if not tags:
            raise ValueError("tags is required")
        url = f"{self.base_url}/v2/numberflow/numbers/{id}/tags"
        json_payload = { "removeTags": tags}
        response = requests.patch(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def update_truenumber_values_by_statement(self, **kwargs):
        """
        Updates the values of truenumbers by statement.
        :param numberspace: str (required) - The numberspace to update the truenumbers in.
        :param true_statement: str (required) - The true statement to update the truenumbers with.
        :param tags: list[str] (required) - The tags to update the truenumbers with.
        Returns:
            dict - The result of the truenumber values update.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        true_statement = kwargs.get("true_statement")
        if not true_statement:
            raise ValueError("true_statement is required")
        tags = kwargs.get("tags")
        if not tags:
            raise ValueError("tags is required")
        url = f"{self.base_url}/v2/numberflow/numbers/value"
        json_payload = { "trueStatement": true_statement, "tags": tags}
        response = requests.put(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def update_truenumber_values_by_json(self, **kwargs):
        """
        Updates the values of truenumbers by JSON.
        :param numberspace: str (required) - The numberspace to update the truenumbers in.
        :param truenumbers_json: str (required) - The JSON payload to update the truenumbers with.
        :param tags: list[str] (required) - The tags to update the truenumbers with.
        Returns:
            dict - The result of the truenumber values update.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        truenumbers_json = kwargs.get("truenumbers_json")
        if not truenumbers_json:
            raise ValueError("truenumbers_json is required")
        tags = kwargs.get("tags")
        if not tags:
            raise ValueError("tags is required")
        url = f"{self.base_url}/v2/numberflow/numbers/value"
        json_payload = { "truenumbers": truenumbers_json, "tags": tags}
        response = requests.put(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def batched_truenumber_operations(self, **kwargs):
        """
        Batches truenumber operations.
        :param numberspace: str (required) - The numberspace to batch the truenumber operations in.
        :param operations: list[dict] (required) - The operations to batch.
        Returns:
            dict - The result of the truenumber operations batching.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        operations = kwargs.get("operations")
        if not operations:
            raise ValueError("operations is required")
        url = f"{self.base_url}/v2/numberflow/batch"
        json_payload = { "operations": operations}
        response = requests.post(url, headers=self.shared_headers, json=json_payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def get_saved_queries(self, numberspace: str):
        """
        Gets saved queries.
        :param numberspace: str (required) - The numberspace to get the saved queries from.
        Returns:
            dict - The result of the saved queries retrieval.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        url = f"{self.base_url}/v2/numberflow/queries"
        response = requests.get(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def create_saved_query(self, **kwargs):
        """
        Creates a saved query.
        :param numberspace: str (required) - The numberspace to create the saved query in.
        :param name: str (required) - The name of the saved query.
        :param tnql: str (required) - The TNQL query to create the saved query with.
        Returns:
            dict - The result of the saved query creation.
        """
        numberspace = kwargs.get("numberspace")
        url = f"{self.base_url}/v2/numberflow/queries"
        name = kwargs.get("name")
        if not name:
            raise ValueError("name is required")
        tnql = kwargs.get("tnql")
        if not tnql:
            raise ValueError("tnql is required")
        payload = { "name": name, "tnql": tnql}
        response = requests.post(url, headers=self.shared_headers, json=payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def update_saved_query(self, **kwargs):
        """
        Updates a saved query.
        :param numberspace: str (required) - The numberspace to update the saved query in.
        :param id: str (required) - The ID of the saved query to update.
        :param name: str (required) - The name of the saved query.
        :param tnql: str (required) - The TNQL query to update the saved query with.
        Returns:
            dict - The result of the saved query update.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        url = f"{self.base_url}/v2/numberflow/queries/{id}"
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        name = kwargs.get("name")
        if not name:
            raise ValueError("name is required")
        tnql = kwargs.get("tnql")
        if not tnql:
            raise ValueError("tnql is required")
        payload = { "name": name, "tnql": tnql}
        response = requests.put(url, headers=self.shared_headers, json=payload, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def delete_saved_query(self, **kwargs):
        """
        Deletes a saved query.
        :param numberspace: str (required) - The numberspace to delete the saved query from.
        :param id: str (required) - The ID of the saved query to delete.
        Returns:
            dict - The result of the saved query deletion.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        url = f"{self.base_url}/v2/numberflow/queries/{id}"
        response = requests.delete(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def execute_saved_query_by_id(self, **kwargs):
        """
        Executes a saved query by ID.
        :param numberspace: str (required) - The numberspace to execute the saved query in.
        :param id: str (required) - The ID of the saved query to execute.
        Returns:
            dict - The result of the saved query execution.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        url = f"{self.base_url}/v2/numberflow/queries/{id}/results"
        response = requests.get(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def login_user(self, **kwargs):
        """
        Logs in a user.
        :param email: str (required) - The email of the user to login.
        :param password: str (required) - The password of the user to login.
        :param organization: str (required) - The organization of the user to login.
        Returns:
            dict - The result of the user login.
        """
        email = kwargs.get("email")
        if not email:
            raise ValueError("email is required")
        password = kwargs.get("password")
        if not password:
            raise ValueError("password is required")
        organization = kwargs.get("organization")
        if not organization:
            raise ValueError("organization is required")
        url = f"{self.base_url}/v2/users/login"
        json_payload = { "email": email, "password": password, "productCode": organization}
        response = requests.post(url, headers=self.shared_headers, json=json_payload)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def register_user(self, **kwargs):
        """
        Registers a user.
        :param email: str (required) - The email of the user to register.
        :param password: str (required) - The password of the user to register.
        :param organization: str (required) - The organization of the user to register.
        Returns:
            dict - The result of the user registration.
        """
        email = kwargs.get("email")
        if not email:
            raise ValueError("email is required")
        password = kwargs.get("password")
        if not password:
            raise ValueError("password is required")
        organization = kwargs.get("organization")
        if not organization:
            raise ValueError("organization is required")
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
    