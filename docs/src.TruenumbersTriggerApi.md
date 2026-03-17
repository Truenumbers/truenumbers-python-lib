---
title: Python: module src.TruenumbersTriggerApi
---

- **[src](src.html).TruenumbersTriggerApi** [index](.)
[c:\users\tyler\projects\truenumbers\python-libs\src\truenumberstriggerapi.py](file:c%3A%5Cusers%5Ctyler%5Cprojects%5Ctruenumbers%5Cpython-libs%5Csrc%5Ctruenumberstriggerapi.py)




- **Modules**
- | [requests](requests.html) | | | |
| --- | --- | --- | --- |


- **Classes**
- [builtins.object](builtins.html#object)[TruenumbersTriggerApi](src.TruenumbersTriggerApi.html#TruenumbersTriggerApi)

- class **TruenumbersTriggerApi**([builtins.object](builtins.html#object))
- [TruenumbersTriggerApi](#TruenumbersTriggerApi)(**kwargs)

[TruenumbersTriggerApi](#TruenumbersTriggerApi) class for interacting with the Truenumbers Trigger API.
- Methods defined here:
**__init__**(self, **kwargs)Initializes the [TruenumbersTriggerApi](#TruenumbersTriggerApi).
:param base_url: str (required) - The base URL of the Truenumbers Trigger API.
:param shared_headers: dict (optional) - The shared headers to be used for all requests.**create_trigger**(self, **kwargs)Creates a trigger.
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
dict - The result of the trigger creation.**delete_trigger**(self, **kwargs)Deletes a trigger.
:param id: str (required) - The id of the trigger to delete.
Returns:
dict - The result of the trigger deletion.**get_trigger_by_id**(self, **kwargs)Gets a trigger by id.
:param id: str (required) - The id of the trigger to get.
Returns:
dict - The result of the trigger retrieval.**get_triggers**(self, **kwargs)Gets the triggers.
:param numberspace: str (required) - The numberspace to get the triggers from.
:param name: str (optional) - The name of the trigger to get.
:param status: list[str] (optional) - The status of the triggers to get.
Returns:
dict - The result of the trigger retrieval.**update_trigger**(self, **kwargs)Updates a trigger.
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
---
Data descriptors defined here:
**__dict__**dictionary for instance variables (if defined)**__weakref__**list of weak references to the object (if defined)
---
Data and other attributes defined here:
**__annotations__** = {'base_url': <class 'str'>, 'shared_headers': <class 'dict'>}**base_url** = ''**shared_headers** = {'Accept': 'application/json', 'Content-Type': 'application/json'}
