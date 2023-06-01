import datetime
import traceback

from fgo_lib import *
from fgo_fetch_all import *
from download.download_icons import *

if __name__ == "__main__":
    warning_log = os.path.join(os.path.dirname(__file__), 'warning.log')
    now = datetime.datetime.now()

    try:
        get_all_mooncell()
    except Exception as e:
        print(traceback.format_exc())
        with open(warning_log, 'a', encoding='utf-8') as file:
            file.write(f"{now}\n{e}\n{traceback.format_exc()}\n")
        pass

    try:
        update_lib()
    except Exception as e:
        print(traceback.format_exc())
        with open(warning_log, 'a', encoding='utf-8') as file:
            file.write(f"{now}\n{e}\n{traceback.format_exc()}\n")
        pass

    try:
        down_all_card_res()
    except Exception as e:
        print(traceback.format_exc())
        with open(warning_log, 'a', encoding='utf-8') as file:
            file.write(f"{now}\n{e}\n{traceback.format_exc()}\n")
        pass

    try:
        download_icons()
    except Exception as e:
        print(traceback.format_exc())
        with open(warning_log, 'a', encoding='utf-8') as file:
            file.write(f"{now}\n{e}\n{traceback.format_exc()}\n")
        pass

    auto_upload = f"Auto upload in {now}\n"
    upload = os.path.join(os.path.dirname(__file__), 'auto_upload.md')
    with open(upload, 'w', encoding='utf-8') as file:
        file.write(auto_upload)
