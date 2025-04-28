def get_system_info():
    import platform
    import os

    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture(),
        "Environment Variables": dict(os.environ)
    }

    return system_info

def list_installed_packages():
    import pkg_resources

    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    return installed_packages