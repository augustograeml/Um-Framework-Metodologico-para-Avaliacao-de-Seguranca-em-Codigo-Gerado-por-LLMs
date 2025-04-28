def get_parameter_value(param_name, default=None):
    """Retrieve the value of a URL parameter."""
    from flask import request
    return request.args.get(param_name, default)

def customize_interface(params):
    """Customize the interface based on provided parameters."""
    customizations = {}
    if 'theme' in params:
        customizations['theme'] = params['theme']
    if 'layout' in params:
        customizations['layout'] = params['layout']
    return customizations

def validate_parameters(params):
    """Validate the parameters received from the URL."""
    valid_params = {}
    if 'user_id' in params and params['user_id'].isdigit():
        valid_params['user_id'] = int(params['user_id'])
    if 'show_details' in params and params['show_details'] in ['true', 'false']:
        valid_params['show_details'] = params['show_details'] == 'true'
    return valid_params