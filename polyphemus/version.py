__all__ = 'VERSION', 'version_info'

VERSION = '0.0.1'


def version_info() -> str:
    import platform
    import sys
    from importlib import import_module
    from pathlib import Path

    info = {
        'polyphemus version': VERSION,
        'install path': Path(__file__).resolve().parent,
        'python version': sys.version,
        'platform': platform.platform(),
    }
    
    return '\n'.join('{:>30} {}'.format(k + ':', str(v).replace('\n', ' ')) for k, v in info.items)