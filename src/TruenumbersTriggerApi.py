import requests

class TruenumbersTriggerApi:
    """
    TruenumbersTriggerApi class for interacting with the Truenumbers Trigger API.
    """
    base_url: str = ""
    shared_headers: dict = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    def __init__(self, **kwargs):
        """
        Initializes the TruenumbersTriggerApi.
        :param base_url: str (required) - The base URL of the Truenumbers Trigger API.
        :param shared_headers: dict (optional) - The shared headers to be used for all requests.
        """
        base_url = kwargs.get("base_url")
        if not base_url:
            raise ValueError("base_url is required")
        self.base_url = base_url
        shared_headers = kwargs.get("shared_headers")

    def create_trigger(self, **kwargs):
        """
        Creates a trigger.
        :param numberspace: str (required) - The numberspace to create the trigger in.
        :param name: str (required) - The name of the trigger.
        :param description: str (optional) - The description of the trigger.
        :param tnql: str (optional) - The TNQL query to create the trigger with. Required for CREATE and TAG execute_on.
        :param execute_on: list[str] (required) - The execute on of the trigger. CREATE, TAG, CRON
        :param status: str (optional) - The status of the trigger.
        :param tag_on_trigger: list[str] (optional) - The tag on trigger of the trigger.
        :param load_historic_data: bool (optional) - The load historic data of the trigger.
        :param destinations: list[dict] (optional) - The destinations of the trigger. KAFKA, CRON_SCRIPT_DESTINATION, or PYTHON_3
        Returns:
            dict - The result of the trigger creation.
        """
        numberspace = kwargs.get("numberspace")
        if not numberspace:
            raise ValueError("numberspace is required")
        name = kwargs.get("name")
        if not name:
            raise ValueError("name is required")
        description = kwargs.get("description")
        tnql = kwargs.get("tnql")
        execute_on = kwargs.get("execute_on")
        if not execute_on:
            raise ValueError("execute_on is required")
        status = kwargs.get("status")
        tag_on_trigger = kwargs.get("tag_on_trigger")
        load_historic_data = kwargs.get("load_historic_data")

        if ("CREATE" in execute_on or "TAG" in execute_on) and not tnql:
            raise ValueError("tnql is required for CREATE or TAG execute_on")
 
        params = {} if load_historic_data is None or load_historic_data is False else {"loadHistoricData": load_historic_data}

        destinations = kwargs.get("destinations") or [{
            "type": "WEB_SOCKET"
        }]
        payload = {
            "numberspace": numberspace,
            "name": name,
            "description": description,
            "tnql": tnql,
            "executeOn": execute_on,
            "status": status,
            "tagOnTrigger": tag_on_trigger,
            "destinations": destinations
        }
        url = f"{self.base_url}/v1/trigger-definition"
        response = requests.post(url, headers=self.shared_headers, json=payload, params=params)
        if response.status_code >= 400:
            raise Exception(f"Failed to create trigger: {response.text}")
        return response.json()

    def get_triggers(self, **kwargs):
        """
        Gets the triggers.
        :param numberspace: str (required) - The numberspace to get the triggers from.
        :param name: str (optional) - The name of the trigger to get.
        :param status: list[str] (optional) - The status of the triggers to get.
        Returns:
            dict - The result of the trigger retrieval.
        """
        numberspace = kwargs.get("numberspace")
        name = kwargs.get("name")
        status = kwargs.get("status")
        if not numberspace:
            raise ValueError("numberspace is required")
        url = f"{self.base_url}/v1/trigger-definitions"

        status_delimiter = ","
        status_param = status_delimiter.join(status) if status else None
        response = requests.get(url, headers=self.shared_headers, params={"numberspace": numberspace, "name": name, "status": status_param})
        if response.status_code >= 400:
            raise Exception(f"Failed to get triggers: {response.text}")
        return response.json()


    def get_trigger_by_id(self, **kwargs):
        """
        Gets a trigger by id.
        :param id: str (required) - The id of the trigger to get.
        Returns:
            dict - The result of the trigger retrieval.
        """
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        url = f"{self.base_url}/v1/trigger-definitions/{id}"
        response = requests.get(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Failed to get trigger by id: {response.text}")
        return response.json()

    def update_trigger(self, **kwargs):
        """
        Updates a trigger.
        :param id: str (required) - The id of the trigger to update.
        :param name: str (optional) - The name of the trigger to update.
        :param description: str (optional) - The description of the trigger to update.
        :param tnql: str (optional) - The TNQL query to update the trigger with.
        :param execute_on: list[str] (optional) - The execute on of the trigger.
        :param status: str (optional) - The status of the trigger.
        :param tag_on_trigger: list[str] (optional) - The tag on trigger of the trigger.
        :param destinations: list[dict] (optional) - The destinations of the trigger. KAFKA, CRON_SCRIPT_DESTINATION, or PYTHON_3
        Returns:
            dict - The result of the trigger update.
        """
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        name = kwargs.get("name")
        description = kwargs.get("description")
        tnql = kwargs.get("tnql")
        execute_on = kwargs.get("execute_on")
        status = kwargs.get("status")
        tag_on_trigger = kwargs.get("tag_on_trigger")
        destinations = kwargs.get("destinations")

        payload = {
            "name": name,
            "description": description,
            "tnql": tnql,
            "executeOn": execute_on,
            "status": status,
            "tagOnTrigger": tag_on_trigger,
            "destinations": destinations
        }

        url = f"{self.base_url}/v1/trigger-definitions/{id}"
        response = requests.patch(url, headers=self.shared_headers, json=payload)
        if response.status_code >= 400:
            raise Exception(f"Failed to update trigger: {response.text}")
        return response.json()

    def delete_trigger(self, **kwargs):
        """
        Deletes a trigger.
        :param id: str (required) - The id of the trigger to delete.
        Returns:
            dict - The result of the trigger deletion.
        """
        id = kwargs.get("id")
        if not id:
            raise ValueError("id is required")
        url = f"{self.base_url}/v1/trigger-definitions/{id}"
        response = requests.delete(url, headers=self.shared_headers)
        if response.status_code >= 400:
            raise Exception(f"Failed to delete trigger: {response.text}")
        return response.json()