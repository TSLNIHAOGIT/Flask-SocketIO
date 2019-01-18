from gevent import monkey
monkey.patch_all()
import requests

from requests.packages.urllib3.util.ssl_ import create_urllib3_context
create_urllib3_context()