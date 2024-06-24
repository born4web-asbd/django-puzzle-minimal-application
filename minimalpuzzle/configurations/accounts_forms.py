"""
User defined forms configuration for module 'accounts'
"""

from django import forms

# UTILS
from accounts.utils.data_access import get_account_home_page_choices

# **************************************
# *     Accounts forms definitions     *
# **************************************

# simplest form definition to be used in many applications - do not modify this one create your own by copy and modify
ACCOUNT_RIGHTS_DATA_FORM_DEFINITION = {
    # Those are data not storred in JSONField but in main model class parameters for example
    'json_data_excluded_fields': [
    ],
    # Those form items are hidden
    'hidden_fields': [
    ],
    # List of form fields items used to generate form. Also order of those items defines order displayed if default
    # Contacts form page templates are used
    'field_definitions': {
        'read_only_access': {
            'field_type': forms.BooleanField,
            'field_arguments': {
                'label': 'Read only access',
                'help_text': 'Uživatel má v rámci aplikace pouze přístup pro čtení, nemůže nic modifikovat',
                'widget': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'required': False,
                'error_messages': {},
                'validators': [],
            }
        },
    }
}
# to show data table expected between 'column name' and 'data item name' stored in AccountRights->rights
ACCOUNT_RIGHTS_TABLE_COLUMN_NAMES = {
    'read_only_access': 'Pouze čtení',
}

ACCOUNT_CONFIGURATIONS_DATA_FORM_DEFINITION = {
    # Contacts listing kind of view uses column names to show. Avoid language problems there is always conversion
    # table expected between 'column name' and 'data item name' stored in Contacts->json_data
    # List of form fields items used to generate form. Also order of those items defines order displayed if default
    # Contacts form page templates are used
    'json_data_excluded_fields': [
    ],
    # Those form items are hidden
    'hidden_fields': [
    ],
    'field_definitions': {
        'default_pagination': {
            'field_type': forms.IntegerField,
            'field_arguments': {
                'label': 'Stránkování',
                'help_text': 'Počet záznamů zobrazených na jedné stránce, než se zorazí šipky na procházení stránek',
                'widget': forms.NumberInput(attrs={'class': 'form-control'}),
                'required': True,
                'error_messages': {},
                'validators': [],
            }
        },
        'rozbalit_detaily': {
            'field_type': forms.BooleanField,
            'field_arguments': {
                'label': 'Rozbalit detaily',
                'help_text': 'Implicitně budou detaily rozbaleny nebo zabaleny tam, kde se to používá.',
                'widget': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                'required': False,
                'error_messages': {},
                'validators': [],
            }
        },
        'home_page_url': {
            'field_type': forms.CharField,
            'field_arguments': {
                'label': 'Domovská stránka',
                'help_text': 'Na tuto stránku se uživatel přepne po příhlášení do aplikace.',
                'widget': forms.Select(choices=get_account_home_page_choices(),
                                       attrs={'class': 'form-control'}),
                'required': False,
                'error_messages': {},
                'validators': [],
            }
        },
    }
}

# to show data table expected between 'column name' and 'data item name' stored in AccountRights->rights
ACCOUNT_CONFIGURATIONS_TABLE_COLUMN_NAMES = {
    'default_pagination': 'Řádků na stránce',
    'rozbalit_detaily': 'Rozbalit detaily',
    'home_page_url': 'Domovská stránka',
}

