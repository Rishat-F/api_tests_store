from json import JSONDecodeError
from typing import Optional

from pydantic import BaseModel, ValidationError
from requests import Response


class Validator:
    @staticmethod
    def structure(
        response: Response, type_response: Optional[BaseModel] = None
    ) -> Response:
        """
        Try to structure response json.

        Return modified response with 'data' field.
        Raise exceptions if response json not valid.
        """
        if type_response:
            try:
                response.data = type_response.parse_obj(response.json())
            except ValidationError as e:
                print(e.json())  # ToDo: Логгирование вместо принта
                raise e
            except JSONDecodeError as e:
                raise e
        return response
