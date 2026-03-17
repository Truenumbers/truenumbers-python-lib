import requests

class TruenumbersRestApi:
    """
    High‑level client for the Truenumbers REST API.

    This class wraps the HTTP endpoints exposed by the Truenumbers backend and
    provides convenient helpers for working with numberspaces, truenumbers,
    saved queries, and user accounts. All methods raise ``ValueError`` when a
    required argument is missing and ``Exception`` when the underlying HTTP
    request returns a status code >= 400.
    """
    base_url: str = ""
    shared_headers: dict = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, **kwargs):
        """
        Initialize a new Truenumbers REST API client.

        Args:
            base_url (str): Base URL of the Truenumbers API, for example
                ``"https://api.truenumbers.com"``. This value is required.
            shared_headers (dict, optional): Extra HTTP headers to send with every
                request (for example authentication headers). Supplied keys
                override the defaults in ``shared_headers``.

        Raises:
            ValueError: If ``base_url`` is not provided.
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
        Execute a TNQL query against a numberspace.

        Args:
            numberspace (str): Name of the numberspace to query. Required.
            tnql (str): TNQL query string to execute. Required.
            limit (int, optional): Maximum number of rows to return.
                Defaults to ``100``.
            offset (int, optional): Number of rows to skip before returning
                results. Defaults to ``0``.

        Returns:
            dict: A JSON object with keys such as ``"columns"`` (list of column
            names) and ``"rows"`` (list of result rows), along with any
            additional metadata the server includes.

        Raises:
            ValueError: If ``numberspace`` or ``tnql`` is missing.
            Exception: If the API response status code is >= 400.
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
        Execute a TNQL ``GROUP BY`` query against a numberspace.

        This has the same arguments as :meth:`tnql` but hits the ``group-by``
        endpoint and returns grouped results.

        Args:
            numberspace (str): Name of the numberspace to query. Required.
            tnql (str): TNQL query string containing a ``GROUP BY`` clause.
                Required.
            limit (int, optional): Maximum number of grouped rows to return.
                Defaults to ``100``.
            offset (int, optional): Number of groups to skip before returning
                results. Defaults to ``0``.

        Returns:
            dict: A JSON object describing grouped results, typically including
            grouping keys, aggregated values, and any additional metadata.

        Raises:
            ValueError: If ``numberspace`` or ``tnql`` is missing.
            Exception: If the API response status code is >= 400.
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
        """
        Create a new numberspace.

        Args:
            numberspace (str): Name of the numberspace to create.

        Returns:
            dict: A JSON object describing the created numberspace, for example
            including ``"numberspace"`` and implementation‑specific metadata.

        Raises:
            Exception: If the API response status code is >= 400.
        """
        url = f"{self.base_url}/v2/numberflow/numberspace"
        json_payload = { "numberspace": numberspace}
        response = requests.post(url, headers=self.shared_headers, json=json_payload)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def get_numberspaces(self):
        """
        List all numberspaces visible to the current user.

        Returns:
            dict: A JSON object containing the list of numberspaces, typically
            under a key like ``"items"`` or a similar collection field.

        Raises:
            Exception: If the API response status code is >= 400.
        """
        url = f"{self.base_url}/v2/numberflow/numberspace"
        response = requests.get(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def delete_numberspace(self, numberspace: str):
        """
        Delete an existing numberspace.

        Args:
            numberspace (str): Name of the numberspace to delete.

        Returns:
            dict: A JSON object indicating whether the numberspace was deleted
            and any additional status information.

        Raises:
            Exception: If the API response status code is >= 400.
        """
        url = f"{self.base_url}/v2/numberflow/numberspace"
        response = requests.delete(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    
    def get_numberspace(self, numberspace: str):
        """
        Retrieve a single numberspace by name.

        Args:
            numberspace (str): Name of the numberspace to retrieve.

        Returns:
            dict: A JSON object describing the numberspace, including its name
            and associated metadata.

        Raises:
            Exception: If the API response status code is >= 400.
        """
        url = f"{self.base_url}/v2/numberflow/numberspace"
        response = requests.get(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def create_truenumbers_from_statement(self, **kwargs):
        """
        Create one or more Truenumbers from a natural‑language statement.

        This method maps to the
        ``POST /v2/numberflow/numbers`` *Create Truenumbers* endpoint and uses
        the ``trueStatement`` field of the request body.

        Args:
            numberspace (str): Numberspace in which the new Truenumbers will
                be created. Required.
            true_statement (str): Human‑readable statement to parse into
                Truenumbers. Required.
            noReturn (bool, optional): If ``True``, the API will not return the
                created Truenumbers in the response. Defaults to ``False``.
            skipStore (bool, optional): If ``True``, creates Truenumbers
                without storing them. Defaults to ``False``.
            tags (list, optional): Additional tags to attach to every created
                Truenumber. Defaults to an empty list.

        Returns:
            dict: A JSON object representing the created Truenumbers, typically
            containing a list of Truenumber objects with fields such as
            ``"guid"``, ``"subject"``, ``"property"``, ``"value"`` and
            ``"tags"``.

        Raises:
            ValueError: If ``numberspace`` or ``true_statement`` is missing.
            Exception: If the API response status code is >= 400.
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
            Create one or more Truenumbers from a JSON payload.

            This method maps to the
            ``POST /v2/numberflow/numbers`` *Create Truenumbers* endpoint and uses
            the ``truenumbers`` field of the request body.

            Args:
                numberspace (str): Numberspace in which the new Truenumbers will
                    be created. Required.
                truenumbers_json (list[dict]): List of JSON objects representing Truenumbers to create. Required.
                noReturn (bool, optional): If ``True``, the API will not return the
                    created Truenumbers in the response. Defaults to ``False``.
                skipStore (bool, optional): If ``True``, creates Truenumbers
                    without storing them. Defaults to ``False``.
                tags (list, optional): Additional tags to attach to every created
                    Truenumber. Defaults to an empty list.

            Returns:
                dict: A JSON object representing the created Truenumbers, typically
                containing a list of Truenumber objects with fields such as
                ``"guid"``, ``"subject"``, ``"property"``, ``"value"`` and
                ``"tags"``.

            Raises:
                ValueError: If ``numberspace`` or ``truenumbers_json`` is missing.
                Exception: If the API response status code is >= 400.
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
        Delete Truenumbers that match a TNQL query.

        This maps to ``DELETE /v2/numberflow/numbers`` in the REST API.

        Args:
            numberspace (str): Numberspace to delete Truenumbers from.
                Required.
            tnql (str): TNQL query that selects the Truenumbers to delete.
                Required.

        Returns:
            dict: A JSON object describing what was deleted, for example counts
            of affected Truenumbers and any additional deletion metadata.

        Raises:
            ValueError: If ``numberspace`` or ``tnql`` is missing.
            Exception: If the API response status code is >= 400.
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
        Delete a single Truenumber by its unique identifier.

        This maps to ``DELETE /v2/numberflow/numbers/{guid}``.

        Args:
            numberspace (str): Numberspace that owns the Truenumber.
                Required.
            id (str): GUID of the Truenumber to delete. Required.

        Returns:
            dict: A JSON object confirming deletion of the Truenumber and any
            additional status information.

        Raises:
            ValueError: If ``numberspace`` or ``id`` is missing.
            Exception: If the API response status code is >= 400.
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
        Add tags to all Truenumbers that match a TNQL query.

        This wraps ``PATCH /v2/numberflow/numbers/tags`` using the ``addTags``
        field in the request body.

        Args:
            numberspace (str): Numberspace that contains the Truenumbers.
                Required.
            tnql (str): TNQL query that selects which Truenumbers to tag.
                Required.
            tags (list[str]): Tags to add. Required.

        Returns:
            dict: A JSON object indicating how many Truenumbers were updated
            and which tags were added.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Remove tags from all Truenumbers that match a TNQL query.

        This also uses ``PATCH /v2/numberflow/numbers/tags`` but sends
        ``removeTags`` in the request body.

        Args:
            numberspace (str): Numberspace that contains the Truenumbers.
                Required.
            tnql (str): TNQL query that selects which Truenumbers to modify.
                Required.
            tags (list[str]): Tags to remove. Required.

        Returns:
            dict: A JSON object indicating how many Truenumbers were updated
            and which tags were removed.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Fetch a single Truenumber by its GUID.

        This wraps ``GET /v2/numberflow/numbers/{guid}``.

        Args:
            numberspace (str): Numberspace that contains the Truenumber.
                Required.
            id (str): GUID of the Truenumber to retrieve. Required.

        Returns:
            dict: A JSON object representing the requested Truenumber, with
            fields such as ``"guid"``, ``"subject"``, ``"property"``, ``"value"``
            and ``"tags"``.

        Raises:
            ValueError: If ``numberspace`` or ``id`` is missing.
            Exception: If the API response status code is >= 400.
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
        Add tags to a single Truenumber by GUID.

        This maps to ``PATCH /v2/numberflow/numbers/{guid}/tags`` with the
        ``addTags`` field.

        Args:
            numberspace (str): Numberspace that contains the Truenumber.
                Required.
            id (str): GUID of the Truenumber to tag. Required.
            tags (list[str]): Tags to add. Required.

        Returns:
            dict: A JSON object describing the tag update, including which tags
            were added and how many Truenumbers were affected.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Remove tags from a single Truenumber by GUID.

        This also maps to ``PATCH /v2/numberflow/numbers/{guid}/tags``, but
        uses the ``removeTags`` field in the request body.

        Args:
            numberspace (str): Numberspace that contains the Truenumber.
                Required.
            id (str): GUID of the Truenumber to modify. Required.
            tags (list[str]): Tags to remove. Required.

        Returns:
            dict: A JSON object describing the tag update, including which tags
            were removed and how many Truenumbers were affected.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Update Truenumber values based on a natural‑language statement.

        This wraps ``PUT /v2/numberflow/numbers/value`` using the
        ``trueStatement`` representation of Truenumbers.

        Args:
            numberspace (str): Numberspace containing the Truenumbers to
                update. Required.
            true_statement (str): Statement that describes the new values.
                Required.
            tags (list[str]): Tags that help match and/or annotate updated
                Truenumbers. Required.

        Returns:
            dict: A JSON object describing the value update, for example
            including before/after values and counts of updated Truenumbers.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Update Truenumber values using an explicit JSON payload.

        This also calls ``PUT /v2/numberflow/numbers/value``, but sends a
        structured ``truenumbers`` array instead of a ``trueStatement``.

        Args:
            numberspace (str): Numberspace containing the Truenumbers to
                update. Required.
            truenumbers_json (str | dict | list): JSON structure describing
                the Truenumbers and their new values. Required.
            tags (list[str]): Tags that help match and/or annotate updated
                Truenumbers. Required.

        Returns:
            dict: A JSON object describing the value update, for example
            including before/after values and counts of updated Truenumbers.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Execute a batch of heterogeneous Truenumber operations in one call.

        This wraps ``POST /v2/numberflow/batch`` and accepts a list of
        operations described by the ``BatchOperations`` schema.

        Args:
            numberspace (str): Numberspace in which to apply the operations.
                Required.
            operations (list[dict]): List of operation descriptors, each
                conforming to the ``BatchOperations`` schema. Required.

        Returns:
            dict: A JSON object summarizing the result of each operation in the
            batch, typically keyed by operation identifier.

        Raises:
            ValueError: If ``numberspace`` or ``operations`` is missing.
            Exception: If the API response status code is >= 400.
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
        List saved queries in a numberspace.

        This wraps ``GET /v2/numberflow/queries``.

        Args:
            numberspace (str): Numberspace to read saved queries from.

        Returns:
            dict: A JSON object containing saved query metadata such as
            identifiers, names, TNQL bodies and timestamps.

        Raises:
            Exception: If the API response status code is >= 400.
        """
        url = f"{self.base_url}/v2/numberflow/queries"
        response = requests.get(url, headers=self.shared_headers, params={"numberspace": numberspace})
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()

    def create_saved_query(self, **kwargs):
        """
        Create a new saved query.

        This wraps ``POST /v2/numberflow/queries``.

        Args:
            numberspace (str): Numberspace where the saved query will live.
                Required.
            name (str): Human‑friendly name for the saved query. Required.
            tnql (str): TNQL string that defines the query. Required.

        Returns:
            dict: A JSON object describing the created saved query, including
            its identifier, name and TNQL body.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Update an existing saved query.

        This wraps ``PUT /v2/numberflow/queries/{id}``.

        Args:
            numberspace (str): Numberspace that owns the saved query.
                Required.
            id (str): Identifier of the saved query to update. Required.
            name (str): New name for the saved query. Required.
            tnql (str): New TNQL body for the saved query. Required.

        Returns:
            dict: A JSON object describing the updated saved query, including
            its identifier, name and TNQL body.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Delete a saved query by ID.

        This wraps ``DELETE /v2/numberflow/queries/{id}``.

        Args:
            numberspace (str): Numberspace that owns the saved query.
                Required.
            id (str): Identifier of the saved query to delete. Required.

        Returns:
            dict: A JSON object confirming deletion of the saved query and any
            additional status information.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Execute a saved query and return its results.

        This wraps ``GET /v2/numberflow/queries/{id}/results``.

        Args:
            numberspace (str): Numberspace that owns the saved query.
                Required.
            id (str): Identifier of the saved query to execute. Required.

        Returns:
            dict: A JSON object containing the saved query results, similar in
            structure to :meth:`tnql` responses.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Authenticate a user and obtain a session or token.

        This maps to ``POST /v2/users/login``.

        Args:
            email (str): User email address. Required.
            password (str): User password. Required.
            organization (str): Product or organization code used for
                multi‑tenant routing (``productCode`` in the API). Required.

        Returns:
            dict: A JSON object containing authentication details such as
            access tokens, expiry information and user metadata.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        Register a new user account.

        This maps to ``POST /v2/users/register``.

        Args:
            email (str): Email address for the new account. Required.
            password (str): Password for the new account. Required.
            organization (str): Product or organization code used for
                multi‑tenant routing (``productCode`` in the API). Required.

        Returns:
            dict: A JSON object describing the created user and any associated
            verification or onboarding information.

        Raises:
            ValueError: If any required argument is missing.
            Exception: If the API response status code is >= 400.
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
        """
        Verify the current authenticated user session.

        This wraps ``GET /v2/users/verify`` and typically checks that the
        supplied authentication headers/tokens are valid.

        Returns:
            dict: A JSON object describing the authenticated user or session
            state (for example user id, email and token validity).

        Raises:
            Exception: If the API response status code is >= 400.
        """
        url = f"{self.base_url}/v2/users/verify"
        response = requests.get(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Error: {response.status_code} {response.text}")
        return response.json()
    