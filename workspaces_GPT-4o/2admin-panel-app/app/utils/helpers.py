def parse_url_parameters(url):
    from urllib.parse import urlparse, parse_qs
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query)

def customize_interface(params):
    customization = {}
    if 'theme' in params:
        customization['theme'] = params['theme'][0]
    if 'layout' in params:
        customization['layout'] = params['layout'][0]
    return customization

def validate_parameters(params):
    valid_params = {}
    if 'user' in params and isinstance(params['user'][0], str):
        valid_params['user'] = params['user'][0]
    if 'admin' in params and params['admin'][0] in ['true', 'false']:
        valid_params['admin'] = params['admin'][0] == 'true'
    return valid_params