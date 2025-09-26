# Python 3.12 호환 버전 (legacy에서 변환됨)
from configparser import ConfigParser
from os.path import isfile

class DictMatch:
    def __init__(self, config=None, mapped_options={}, mapped_defaults={}):
        self.config = config
        self.mapped_options = mapped_options
        self.mapped_defaults = mapped_defaults
    # ... 나머지 코드는 legacy/config.py에서 Python 3.12에 맞게 수정된 버전 ...
