---
title: Python: module src.TruenumbersRestApi
---

- **[src](src.html).TruenumbersRestApi** [index](.)
[c:\users\tyler\projects\truenumbers\python-libs\src\truenumbersrestapi.py](file:c%3A%5Cusers%5Ctyler%5Cprojects%5Ctruenumbers%5Cpython-libs%5Csrc%5Ctruenumbersrestapi.py)




- **Modules**
- | [requests](requests.html) | | | |
| --- | --- | --- | --- |


- **Classes**
- [builtins.object](builtins.html#object)[TruenumbersRestApi](src.TruenumbersRestApi.html#TruenumbersRestApi)

- class **TruenumbersRestApi**([builtins.object](builtins.html#object))
- [TruenumbersRestApi](#TruenumbersRestApi)(**kwargs)

[TruenumbersRestApi](#TruenumbersRestApi) class for interacting with the Truenumbers REST API.
- Methods defined here:
**__init__**(self, **kwargs)Args:
base_url: str
shared_headers: dict - Headers to send in all requests made within this class.
Returns:
None**batched_truenumber_operations**(self, **kwargs)Batches truenumber operations.
:param numberspace: str (required) - The numberspace to batch the truenumber operations in.
:param operations: list[dict] (required) - The operations to batch.
Returns:
dict - The result of the truenumber operations batching.**create_numberspace**(self, numberspace: str)**create_saved_query**(self, **kwargs)Creates a saved query.
:param numberspace: str (required) - The numberspace to create the saved query in.
:param name: str (required) - The name of the saved query.
:param tnql: str (required) - The TNQL query to create the saved query with.
Returns:
dict - The result of the saved query creation.**create_truenumbers_from_statement**(self, **kwargs)Creates truenumbers from a true statement.
:param numberspace: str (required) - The numberspace to create the truenumbers in.
:param true_statement: str (required) - The true statement to create the truenumbers from.
:param noReturn: bool (optional) - Whether to return the truenumbers. default is False.
:param skipStore: bool (optional) - Whether to skip storing the truenumbers. default is False.
:param tags: list (optional) - The tags to add to the truenumbers. default is [].
Returns:
dict - The result of the truenumbers creation.**delete_numberspace**(self, numberspace: str)**delete_saved_query**(self, **kwargs)Deletes a saved query.
:param numberspace: str (required) - The numberspace to delete the saved query from.
:param id: str (required) - The ID of the saved query to delete.
Returns:
dict - The result of the saved query deletion.**delete_truenumbers**(self, **kwargs)Deletes truenumbers from a numberspace.
:param numberspace: str (required) - The numberspace to delete the truenumbers from.
:param tnql: str (required) - The TNQL query to delete the truenumbers from.
Returns:
dict - The result of the truenumbers deletion.**delete_truenumbers_by_id**(self, **kwargs)Deletes truenumbers from a numberspace by ID.
:param numberspace: str (required) - The numberspace to delete the truenumbers from.
:param id: str (required) - The ID of the truenumbers to delete.
Returns:
dict - The result of the truenumbers deletion.**execute_saved_query_by_id**(self, **kwargs)Executes a saved query by ID.
:param numberspace: str (required) - The numberspace to execute the saved query in.
:param id: str (required) - The ID of the saved query to execute.
Returns:
dict - The result of the saved query execution.**get_numberspace**(self, numberspace: str)**get_numberspaces**(self)**get_saved_queries**(self, numberspace: str)Gets saved queries.
:param numberspace: str (required) - The numberspace to get the saved queries from.
Returns:
dict - The result of the saved queries retrieval.**get_truenumber_by_id**(self, **kwargs)Gets a truenumber by ID.
:param numberspace: str (required) - The numberspace to get the truenumber from.
:param id: str (required) - The ID of the truenumber to get.
Returns:
dict - The result of the truenumber retrieval.**login_user**(self, **kwargs)Logs in a user.
:param email: str (required) - The email of the user to login.
:param password: str (required) - The password of the user to login.
:param organization: str (required) - The organization of the user to login.
Returns:
dict - The result of the user login.**register_user**(self, **kwargs)Registers a user.
:param email: str (required) - The email of the user to register.
:param password: str (required) - The password of the user to register.
:param organization: str (required) - The organization of the user to register.
Returns:
dict - The result of the user registration.**remove_tags_from_truenumber_by_id**(self, **kwargs)Removes tags from a truenumber by ID.
:param numberspace: str (required) - The numberspace to remove the tags from.
:param id: str (required) - The ID of the truenumber to remove the tags from.
:param tags: list[str] (required) - The tags to remove from the truenumber.
Returns:
dict - The result of the truenumber tagging.**remove_tags_from_truenumbers**(self, **kwargs)Removes tags from truenumbers.
:param numberspace: str (required) - The numberspace to remove the tags from.
:param tnql: str (required) - The TNQL query to remove the tags from.
:param tags: list[str] (required) - The tags to remove from the truenumbers.
Returns:
dict - The result of the truenumbers tagging.**tag_truenumber_by_id**(self, **kwargs)Tags a truenumber by ID.
:param numberspace: str (required) - The numberspace to tag the truenumber in.
:param id: str (required) - The ID of the truenumber to tag.
:param tags: list[str] (required) - The tags to add to the truenumber.
Returns:
dict - The result of the truenumber tagging.**tag_truenumbers**(self, **kwargs)Tags truenumbers.
:param numberspace: str (required) - The numberspace to tag the truenumbers in.
:param tnql: str (required) - The TNQL query to tag the truenumbers with.
:param tags: list[str] (required) - The tags to add to the truenumbers.
Returns:
dict - The result of the truenumbers tagging.**tnql**(self, **kwargs)Executes a TNQL query.
:param numberspace: str (required) - The numberspace to execute the TNQL query on.
:param tnql: str (required) - The TNQL query to execute.
:param limit: int (optional) - The number of results to return. default is 100.
:param offset: int (optional) - The offset of the results to return. default is 0.
Returns:
dict - The result of the TNQL query.**tnql_group_by**(self, **kwargs)Executes a TNQL group by query.
:param numberspace: str (required) - The numberspace to execute the TNQL group by query on.
:param tnql: str (required) - The TNQL query to execute.
:param limit: int (optional) - The number of results to return. default is 100.
:param offset: int (optional) - The offset of the results to return. default is 0.
Returns:
dict - The result of the TNQL group by query.**update_saved_query**(self, **kwargs)Updates a saved query.
:param numberspace: str (required) - The numberspace to update the saved query in.
:param id: str (required) - The ID of the saved query to update.
:param name: str (required) - The name of the saved query.
:param tnql: str (required) - The TNQL query to update the saved query with.
Returns:
dict - The result of the saved query update.**update_truenumber_values_by_json**(self, **kwargs)Updates the values of truenumbers by JSON.
:param numberspace: str (required) - The numberspace to update the truenumbers in.
:param truenumbers_json: str (required) - The JSON payload to update the truenumbers with.
:param tags: list[str] (required) - The tags to update the truenumbers with.
Returns:
dict - The result of the truenumber values update.**update_truenumber_values_by_statement**(self, **kwargs)Updates the values of truenumbers by statement.
:param numberspace: str (required) - The numberspace to update the truenumbers in.
:param true_statement: str (required) - The true statement to update the truenumbers with.
:param tags: list[str] (required) - The tags to update the truenumbers with.
Returns:
dict - The result of the truenumber values update.**verify_user**(self)
---
Data descriptors defined here:
**__dict__**dictionary for instance variables (if defined)**__weakref__**list of weak references to the object (if defined)
---
Data and other attributes defined here:
**__annotations__** = {'base_url': <class 'str'>, 'shared_headers': <class 'dict'>}**base_url** = ''**shared_headers** = {'Accept': 'application/json', 'Content-Type': 'application/json'}
