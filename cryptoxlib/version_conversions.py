import sys
import asyncio
import time


def get_compatible_version():
    python_version = sys.version_info
    if python_version.major == 3 and python_version.minor == 6:
        return True, False
    elif python_version.major == 3 and python_version.minor > 6:
        return False,True
    else:
        return False, False

 
IS_PYTHON36, IS_PYTHON37_UP = get_compatible_version()


def async_run(f):
    if IS_PYTHON36:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(f)
    elif IS_PYTHON37_UP:
        return asyncio.run(f)

    raise Exception(f'Unsupported Python version! Only versions 3.6+ are supported.')


def async_create_task(f):
    if IS_PYTHON36:
        loop = asyncio.get_event_loop()
        return loop.create_task(f)
    elif IS_PYTHON37_UP:
        return asyncio.create_task(f)

    raise Exception(f'Unsupported Python version! Only versions 3.6+ are supported.')


def get_current_time_ms():
    if IS_PYTHON36:
        return time.time() * 1000.0
    else:
        return time.time_ns() / 1000000.0