import json
import re

from path_and_json import *


def get_all_cft():
    root_cft_url = "https://fgo.wiki/w/%E7%A4%BC%E8%A3%85%E5%9B%BE%E9%89%B4"
    try:
        get_all = requests.get(root_cft_url, timeout=20, headers=headers)
    except Exception as e:
        return e

    raw_data = get_all.text
    rule = re.compile(r'override_data(\s)?=(\s)?\".+event=0')
    data = re.search(rule, raw_data).group(0)
    data = re.sub(r'override_data(\s)?=(\s)?\"', "", data).split("\\n")
    for i in range(len(data) - 1, -1, -1):
        data[i] = data[i].replace('\\\"', '"')
        if data[i] == '':
            data.pop(i)

    updated_crafts = []
    crafts = []
    old_all_cft = []
    if os.path.exists(all_craft_path):
        try:
            old_all_cft = json.load(open(all_craft_path, encoding="utf-8"))
        except json.decoder.JSONDecodeError:
            old_all_cft = []

    rule_all_cft = re.compile(r"raw_str(\s)?=(\s)?\"id.+//media.fgo.wiki/.+\.(png|jpg)")
    all_cft_icons = re.search(rule_all_cft, raw_data).group(0).split(",")
    rule_png = re.compile(r"//media.fgo.wiki/.+\.(png|jpg)")
    for i in range(len(all_cft_icons) - 1, -1, -1):
        if not re.match(rule_png, all_cft_icons[i]):
            all_cft_icons.pop(i)
        else:
            all_cft_icons[i] = all_cft_icons[i].replace("//", "https://")

    for i in range(0, len(data), 9):
        cft = {
            "id": data[i].replace("id=", ""),
            "name": data[i + 1].replace("name=", ""),
            "name_link": data[i + 2].replace("name_link=", ""),
            "name_other": data[i + 3].replace("name_other=", ""),
            "des": data[i + 4].replace("des=", ""),
            "des_max": data[i + 5].replace("des_max=", ""),
            "tag": data[i + 6].replace("tag=", ""),
            "type": data[i + 7].replace("type=", ""),
            "event": data[i + 8].replace("event=", "")
        }
        cid = cft["id"]
        cid = cid.zfill(3)
        rule_cmd = re.compile(rf"https://media.fgo.wiki/.+礼装{cid}\.(png|jpg)")
        for each in all_cft_icons:
            if re.match(rule_cmd, each):
                i_each = all_cft_icons.index(each)
                cft["online"] = {
                    "cft_icon": each,
                    "skill_icon": all_cft_icons[i_each + 1]
                }

                cft["local"] = {
                    "cft_icon": each.split("/").pop(),
                    "skill_icon": all_cft_icons[i_each + 1].split("/").pop()
                }

        if cft not in old_all_cft:
            updated_crafts.append(int(cft["id"]))
        crafts.append(cft)

    if old_all_cft == crafts:
        return 1, None

    with open(all_craft_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(crafts, indent=2, ensure_ascii=False))
