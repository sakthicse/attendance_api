import os
import string
from lockfile import LockFile, AlreadyLocked
from configparser import ConfigParser
from django.core.exceptions import ImproperlyConfigured
from django.utils.crypto import get_random_string

VALID_KEY_CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits


class FilePermissionError(Exception):
    """The file permissions are insecure."""
    pass


def load_environment_file(envfile,base_dir, key_length=64):
    config = None
    lock = LockFile(base_dir)

    with lock:
        if not os.path.exists(envfile):
            # Create empty file if it doesn't exists
            config = ConfigParser()
            config.add_section('django')
            config['django']['secret_key'] = get_random_string(key_length, VALID_KEY_CHARS)

            with open(envfile, 'w') as configfile:
                config.write(configfile)

        if not config:
            config = ConfigParser()
            config.read_file(open(envfile))

        if not config.has_section('django'):
            raise ImproperlyConfigured('Missing `django` section in the environment file.')

        if not config.get('django', 'secret_key', fallback=None):
            raise ImproperlyConfigured('Missing `secret_key` in django section in the environment file.')

        # Register all keys as environment variables
        for key, value in config.items('django'):
            envname = 'DJANGO_%s' % key.upper()  # Prefix to avoid collisions with existing env variables
            if envname not in os.environ:  # Don't replace existing defined variables
                os.environ[envname] = value