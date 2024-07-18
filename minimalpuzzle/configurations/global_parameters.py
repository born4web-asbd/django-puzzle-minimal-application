"""
Global parameters for Django Puzzel PAMA application.
"""
from sharedlibrary.utils.configs import module_configuration_deeper_conversion_to_attribute_dictionary
import importlib

# management command database import hook - only those definitions are imported
# in database as ApplicationParametersConfiguration (usualy done at application instance level)
APPLICATION_PARAMETERS_CONFIGURATON_DATABASE_IMPORT = [

]

# *****************************************************************
# * Global Django Puzzles Application Module Parameters Overrides
# *****************************************************************
GLOBAL_DJANGO_PUZZLE_MODULE_PARAMETERS_OVERRIDES = {
    'accounts': {
        'ALLOW_CHANGE_ACCOUNT_RIGHTS': False,
    },
    'contacts': {
        'ALLOW_PUBLIC_CONTACTS': True,
    },
    'feedback': {
        'ALOW_NEW_CATEGORIES': True,
    },
    # module_name: { module parametres dictionary overrides }
}


# *****************************************************************
# *         Global Django Puzzles Application Parameters
# *****************************************************************
GLOBAL_DJANGO_PUZZLE_PARAMETRS = {
    'default_homepage_url': 'accounts:account-listing',
    'use_model_groups_separation': True,
    'use_account_rights': False,
    'use_account_configuration':  True,
}


# *****************************************************************
# *         get_global_parameters method definition
# *****************************************************************
def get_application_parameters():
    """Global parameters access point

    :return:
    """
    return module_configuration_deeper_conversion_to_attribute_dictionary(GLOBAL_DJANGO_PUZZLE_PARAMETRS)


def get_global_parameters():
    """Global application parameters access point
    - take configuration pydantic model for application always pydantic_models.DjangoPuzzleGlobalParameters
    - read all configurations
    - return dictionary with configuration keys and correspondig configuration parameters (again as dict)

    :return: {GLOBAL_PARAMETERS_GROUP_NAME: CONFIG_KEY_PARAMETERS_DICTIONARY}
    """
    from sharedlibrary.utils.configuration.application_parameters import get_django_puzzle_application_name
    from sharedlibrary.datatypes.attribute_dictionary import AttributeDictionary

    configuration_model = importlib.import_module(
        f'{get_django_puzzle_application_name()}.pydantic_models'
    ).DjangoPuzzleGlobalParameters()

    return AttributeDictionary.from_complex_dict(configuration_model.dict())
