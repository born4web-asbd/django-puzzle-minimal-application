# TODO: THIS CONFIG FILE OR SOME PARTS BE A TEMPLATE IN SHAREDLIBRARY FOR OTHER DJANGO PUZZLES
"""
Application configuration database import file used by manage command
"""
from sharedlibrary.configurations.global_context_parameters import (GLOBAL_APPLICATION_TEMPLATE_CONFIGURATION_CONTEXT_NAME,
                                                                    VIEW_SPECIFIC_TEMPLATE_CONFIGURATION_CONTEXT_NAME,
                                                                    VIEW_SPECIFIC_BUTTONS_LINKS_CONFIGURATION_CONTEXT_NAME,
                                                                    VIEW_SPECIFIC_COLOR_SCHEME_CONFIGURATION_CONTEXT_NAME,
                                                                    GLOBAL_APPLICATION_BUTTONS_LINKS_CONFIGURATION_CONTEXT_NAME,
                                                                    global_application_color_schema_configuration_CONTEXT_NAME,
                                                                    )

APPLICATIONS = [
    {
        'name': 'ASBD',
        'display_name': 'ASBD',
        'active': True,
        'default': True,
    },
]

APPLICATION_VIEW_MAPPINGS = {
    'ASBD': [

    ],
}

APPLICATION_CONFIGURATIONS = {
    'ASBD': [
        {
            'name': 'ASBD base templates',
            'context_name': GLOBAL_APPLICATION_TEMPLATE_CONFIGURATION_CONTEXT_NAME,
            'type': 'A',
            'attributes': {
                "application_display_name": "PAMA",
                "base_template": "asbd_application_base_template.html",
                "print_template": "asbd_tiskove_sestavy_template.html",
                "favicon_icon": "img/favicon-asbd-invert.png",
            },
            'active': False,

        },
        {
            'name': 'ASBD buttons and links',
            'context_name': GLOBAL_APPLICATION_BUTTONS_LINKS_CONFIGURATION_CONTEXT_NAME,
            'type': 'B',
            'attributes': {
                "button_delete": "btn btn-danger mb-2 btn-block",
                "button_create": "btn btn-primary mb-2 btn-block",
                "button_success": "btn btn-success mb-2",
                "button_info": "btn btn-info mb-2",
                "button_warning": "btn btn-warning mb-2",
                "link_color_normal": "text-primary",
                "link_color_danger": "text-danger",
                "link_color_success": "text-success",
                "link_color_light": "text-light",
                "link_color_white": "text-white",
                "text_color_normal": "text-primary",
                "text_color_danger": "text-danger",
                "text_color_success": "text-success"
            },
            'active': False,
         },
        {
            'name': 'ASBD color schema',
            'context_name': global_application_color_schema_configuration_CONTEXT_NAME,
            'type': 'C',
            'attributes': {
                "menu_row_text_color": "text-white",
                "menu_row_background_color": "bg-dark",
                "navbar_style": "navbar-dark",
                "navbar_background_color": "bg-dark",
                "dynamic_row_text_color": "text-white",
                "dynamic_row_background_color": "bg-secondary",
                "right_menu_backgroung_color": "bg-light",
                "right_menu_text_color": "text-body",
                "right_menu_border": "border-left",
                "right_menu_border_color": "border-dark",
                "footer_border": "border-top",
                "footer_border_color": "border-dark",
                "developer_menu_text_color": "text-body",
            },
            'active': False,
        },
    ],
}

VIEW_TEMPLATE_CONFIGURATIONS = [
]

MODULE_PARAMETERS_CONFIGURATONS = [
    {
        'application': 'ASBD',
        'key': 'CONTACTS',
        'type': 'M',
        'name': 'Contacts configuration',
        'active': True,
        'attributes': {
            'ALLOW_PUBLIC_CONTACTS': False,
        }
    },
    {
        'application': 'ASBD',
        'key': 'ACCOUNTS',
        'type': 'M',
        'name': 'Accounts',
        'active': True,
        'attributes': {
            'ACCOUNT_CAN_CHANGE_OWN_CONFIGURATION': True,
            'ACCOUNT_HOME_PAGE_CHOICES': (('byty:domy-listing', 'Seznam domů'),
                                          ('contacts:contacts-listing', 'Seznam uživatelů')),
        }
    },
    {
        'application': 'ASBD',
        'key': 'UZAVERKY',
        'type': 'M',
        'name': 'Uzaverky',
        'active': True,
        'attributes': {
            'VYPISY_PRUBEH_UZAVERKY_UROVEN_DETAILU': 1,
            'UZAVERKA_PROSTREDNICTVIM_CELERY': True,
        }
    },
]
