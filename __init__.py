import datetime

from fgo_lib import *
from fgo_fetch_all import *
from download.download_icons import *

warning_log = os.path.join(os.path.dirname(__file__), 'warning.log')

try:
    get_all_mooncell()
except Exception as e:
    with open(warning_log, 'a', encoding='utf-8') as file:
        file.write(f"{e}\n")
    pass

try:
    update_lib()
except Exception as e:
    with open(warning_log, 'a', encoding='utf-8') as file:
        file.write(f"{e}\n")
    pass

try:
    down_all_card_res()
except Exception as e:
    with open(warning_log, 'a', encoding='utf-8') as file:
        file.write(f"{e}\n")
    pass

try:
    download_icons()
except Exception as e:
    with open(warning_log, 'a', encoding='utf-8') as file:
        file.write(f"{e}\n")
    pass

now = datetime.datetime.now()
auto_upload = f"Auto upload in {now}\n"
upload = os.path.join(os.path.dirname(__file__), 'auto_upload.md')
with open(upload, 'w', encoding='utf-8') as file:
    file.write(auto_upload)
