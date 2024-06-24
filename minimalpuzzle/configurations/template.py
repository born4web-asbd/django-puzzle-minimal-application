"""
Template specific configurations for ASBD Django Puzzle Application
"""

# ##############################################################
# #				 	  Template configuration				   #
# ##############################################################
# default context_name => GLOBAL_APPLICATION_TEMPLATE_CONFIGURATION_CONTEXT_NAME
DEFAULT_APPLICATION_TEMPLATE_CONFIGURATION = {
    "application_display_name": "ASBD",
    "base_template": "asbd_application_base_template.html",
    "print_template": "",
    "favicon_icon": "img/favicon-asbd-invert.png",  # relative to DJANGO_PUZZLE_APPLICATION_CONFIG["TEMPLATES"]/static/
}

# ##############################################################
# #	 	     Buttons and Links configuration				   #
# ##############################################################
# default context_name => GLOBAL_APPLICATION_BUTTONS_LINKS_CONFIGURATION_CONTEXT_NAME
DEFAULT_APPLICATION_BUTTONS_LINKS_CONFIGURATION = {
    "button_delete": "btn btn-danger mb-2 btn-block",
    "button_create": "btn btn-primary mb-2 btn-block",
    "button_success": "btn btn-success mb-2",
    "button_info": "btn btn-info mb-2",
    "button_warning": "btn btn-warning mb-2",
    "link_color_normal": "text-primary",
    #"link_color_normal": "text-danger",
    "link_color_danger": "text-danger",
    #"link_color_danger": "text-success",
    "link_color_success": "text-success",
    "link_color_light": "text-light",
    "link_color_white": "text-white",
    "text_color_normal": "text-primary",
    "text_color_danger": "text-danger",
    "text_color_success": "text-success"
}

# ##############################################################
# #	 	  		Color scheme configuration					   #
# ##############################################################
# default context_name => GLOBAL_APPLICATION_COLOR_SCHEME_CONFIGURATION_CONTEXT_NAME
DEFAULT_APPLICATION_COLOR_SCHEME_CONFIGURATION = {
    "menu_row_text_color": "text-white",
    "menu_row_background_color": "bg-dark",
    "navbar_style": "navbar-dark",
    "navbar_background_color": "bg-dark",
    "dynamic_row_text_color": "text-warning",
    "dynamic_row_background_color": "bg-info",

    "right_menu_background_color": "bg-light",
    "right_menu_text_color": "text-body",
    "right_menu_border_mobile": "border-top",
    "right_menu_border_desktop": "border-left",
    "right_menu_border_color": "border-dark",

    "left_menu_background_color": "bg-light",
    "left_menu_text_color": "text-body",
    "left_menu_border_mobile": "border-bottom",
    "left_menu_border_desktop": "border-right",
    "left_menu_border_color": "border-dark",

    "footer_border": "border-top",
    "footer_border_color": "border-dark",
    "developer_menu_text_color": "text-body",
}
