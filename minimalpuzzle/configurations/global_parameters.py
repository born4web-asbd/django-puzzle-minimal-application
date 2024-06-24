"""
Global parameters for Django Puzzel PAMA application.
"""
from sharedlibrary.utils.configurations import module_configuration_deeper_conversion_to_attribute_dictionary


# management command database import hook - only those definitions are imported
# in database as ApplicationParametersConfiguration (usualy done at application instance level)
APPLICATION_PARAMETERS_CONFIGURATON_DATABASE_IMPORT = [

]

# *****************************************************************
# *         Global Django Puzzles Application Parameters
# *****************************************************************
GLOBAL_DJANGO_PUZZLE_PARAMETRS = {
    'default_homepage_url': 'accounts:account-listing',
    'use_model_groups_separation': True,
    'use_account_rights': False,
    'use_account_configuratiuon':  True,
}


# *****************************************************************
# *         get_global_parameters method definition
# *****************************************************************
def get_application_parameters():
    """Global parameters access point

    :return:
    """
    return module_configuration_deeper_conversion_to_attribute_dictionary(GLOBAL_DJANGO_PUZZLE_PARAMETRS)
