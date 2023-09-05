import os


def os_or_default(os_var, default):
    if os.getenv(os_var) is not None:
        return os.getenv(os_var)
    else:
        return default