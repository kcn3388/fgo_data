import re
from path_and_json import *
from urllib.parse import quote, unquote


def lib_cmd(cmd_data: dict) -> dict:
    print("查询纹章" + cmd_data["id"] + "……")
    cmd = {
        "id": cmd_data["id"],
        "name": cmd_data["name"],
        "name_jp": cmd_data["name"],
        "name_other": None,
        "name_link": cmd_data["name_link"],
        "type": cmd_data["type"],
        "error": []
    }

    if "local" in cmd_data:
        cmd["cmd_icon"] = cmd_data["local"]["cmd_icon"]
        cmd["skill_icon"] = cmd_data["local"]["skill_icon"]
    else:
        cmd["cmd_icon"] = cmd_data["cmd_icon"]
        cmd["skill_icon"] = cmd_data["skill_icon"]

    if isinstance(cmd_data["name_other"], list):
        cmd["name_other"] = cmd_data["name_other"]
    else:
        cmd["name_other"] = cmd_data["name_other"].split("&")

    if len(cmd["name_other"]) == 1 and cmd["name_other"][0] == "":
        cmd["name_other"] = []

    local_data_path = os.path.join(mc_path, "cmd", f'{cmd_data["id"]}.txt')
    local_html_path = os.path.join(mc_path, "cmd", f'{cmd_data["id"]}.html')

    if os.path.exists(local_data_path):
        raw_data = open(local_data_path, "r", encoding="utf-8").read().replace("魔{{jin}}", "魔神(人)")
        raw_html = open(local_html_path, "r", encoding="utf-8").read()
    else:
        cmd["error"].append(f"cmd{cmd['id']} init error: no local res")
        return cmd

    painter = re.search(r"\|画师=(.+)", raw_data)
    name_jp = re.search(r"\|日文名称=(.+)", raw_data)
    icon = re.search(r"\|图标=(.+)", raw_data)
    skills = re.search(r"\|持有技能=\n?([\s\S]+?)\n\|", raw_data)
    desc_cn = re.search(r"\|解说=\n?([\s\S]+?)\n\n?\n?\|", raw_data)
    desc_jp = re.search(r"\|日文解说=\n?([\s\S]+?)\n[|<]", raw_data)
    rare = re.search(r"\|稀有度=(.)", raw_data)
    raw_card_name = re.search(r"\|图片名=(.+)", raw_data)
    if not raw_card_name:
        raw_card_name = re.search(r"\|名称=(.+)", raw_data)

    cmd["name_jp"] = name_jp.group(1) if name_jp else ""
    cmd_detail = {
        "画师": painter.group(1) if painter else "",
        "图标": icon.group(1) if icon else "",
        "持有技能": skills.group(1) if skills else "",
        "解说": desc_cn.group(1) if desc_cn else "",
        "日文解说": desc_jp.group(1) if desc_jp else ""
    }

    card_name = raw_card_name.group(1).strip().replace(" ", "_") if raw_card_name else ""
    if cmd["id"] == "74":
        card_name = "魔神小姐"
    raw_file = re.search(rf"(https://media.fgo.wiki/./../){quote(card_name)}.png", raw_html, re.I)
    if not raw_file:
        cmd["error"].append("cards_url not found")
    cmd["detail"] = cmd_detail
    cmd["rare"] = f"{rare.group(1)}星" if rare else "-"
    cmd["cards_url"] = unquote(raw_file.group(0)) if raw_file else ""

    if not cmd["error"]:
        cmd.pop("error")
    return cmd
