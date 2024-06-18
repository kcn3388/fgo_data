from path_and_json import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn"
}


def download(url: str, path):
    try:
        png = requests.get(url, timeout=20, headers=headers).content
    except Exception as e:
        return e
    if isinstance(png, Exception):
        return png
    if not os.path.exists(path):
        with open(path, "wb") as f:
            f.write(png)
        return 0
    else:
        return 1
        # you can use this comment when you do not know what exception to catch:
        # noinspection PyBroadException
