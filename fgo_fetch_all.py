from bs4 import BeautifulSoup
from download.download_all_res import *
from get.get_all_cft import *
from get.get_all_cmd import *
from get.get_all_svt import *


def fetch_mooncell(select: int):
    if not os.path.exists(mc_path):
        os.mkdir(mc_path)
    try:
        if select == 1:
            with open(all_servant_path, 'r', encoding="utf-8") as f:
                card_data = json.load(f)
            folder_path = os.path.join(mc_path, "svt")
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            card_type = "svt"
        elif select == 2:
            with open(all_craft_path, 'r', encoding="utf-8") as f:
                card_data = json.load(f)
            folder_path = os.path.join(mc_path, "cft")
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            card_type = "cft"
        elif select == 3:
            with open(all_command_path, 'r', encoding="utf-8") as f:
                card_data = json.load(f)
            folder_path = os.path.join(mc_path, "cmd")
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            card_type = "cmd"
        else:
            with open(all_servant_path, 'r', encoding="utf-8") as f:
                card_data = json.load(f)
            folder_path = os.path.join(mc_path, "svt")
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            card_type = "svt"
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        print("本地没有数据~请先获取数据~\n指令：[更新fgo图书馆] 或 [获取全部内容]")
        return
    try:
        updates = json.load(open(update_data_path, encoding="utf-8"))
    except Exception as e:
        print(e)
        updates = {
            "svt": [],
            "cft": [],
            "cmd": []
        }
    update = updates[card_type]
    _ids = jsonpath(card_data, "$..id")
    links = jsonpath(card_data, "$..name_link")
    loss = []
    for index in range(len(_ids)):
        if int(_ids[index]) not in update:
            if os.path.exists(
                    os.path.join(folder_path, f"{_ids[index]}.html")
            ) or os.path.exists(
                os.path.join(folder_path, f"{_ids[index]}.txt")
            ):
                print(f"Skip {card_type} {_ids[index]} since exists.")
                continue
        print(f"Fetching {card_type} {_ids[index]}.")
        url = f"https://fgo.wiki/w/{quote(links[index], 'utf-8')}"
        root_url = f"https://fgo.wiki/index.php?title={quote(links[index], 'utf-8')}&action=edit"
        try:
            raw_html = requests.get(url, timeout=20, headers=headers).text
            root_text = BeautifulSoup(
                requests.get(root_url, timeout=20, headers=headers).content,
                'html.parser'
            ).find("textarea").text
        except Exception as e:
            print(f"Fetch {card_type} {_ids[index]} error: {e}")
            loss.append(_ids[index])
            continue
        try:
            with open(os.path.join(folder_path, f"{_ids[index]}.html"), "w", encoding="utf-8") as mooncell_html:
                mooncell_html.write(raw_html)
            with open(os.path.join(folder_path, f"{_ids[index]}.txt"), "w", encoding="utf-8") as mooncell_raw:
                mooncell_raw.write(root_text)
        except Exception as e:
            print(f"Saving {card_type} {_ids[index]} error: {e}")
            loss.append(_ids[index])


def get_all_mooncell():
    get_all_svt()
    get_all_cft()
    get_all_cmd()
    for i in range(4):
        fetch_mooncell(i)


def down_all_card_res():
    download_svt()
    download_cft()
    download_cmd()
    down_all_card_res()
