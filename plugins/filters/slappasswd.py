import hashlib
import os
from base64 import encodestring as encode


def slappasswd(password, salt=None):
    """Creates salted (random or passed in) SHA1 rootpw"""
    if salt is None:
        salt = os.urandom(8)
    sha = hashlib.sha1(password)
    sha.update(salt)
    ssha = encode('{}{}'.format(sha.digest(), salt)).strip()
    return '{{SSHA}}{}'.format(ssha)


class FilterModule(object):
    """Exposes filters to ansible"""
    def filters(self):
        return {
            'slappasswd': slappasswd
        }
