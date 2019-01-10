from falguard import Validator

from .paths import SWAGGER_JSON

# Initialize a validator that can be used by decorators for Falcon API's
validator = Validator(str(SWAGGER_JSON))
