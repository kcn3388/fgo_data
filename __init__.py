import datetime

from fgo_lib import *
from fgo_fetch_all import *
from download.download_icons import *

try:
    get_all_mooncell()
except:  # noqa
    pass

try:
    update_lib()
except:  # noqa
    pass

try:
    down_all_card_res()
except:  # noqa
    pass

try:
    download_icons()
except:  # noqa
    pass

now = datetime.datetime.now()
auto_upload = f"Auto upload in {now}\n"
upload = os.path.join(os.path.dirname(__file__), 'auto_upload.md')
with open(upload, 'w', encoding='utf-8') as file:
    file.write(auto_upload)
