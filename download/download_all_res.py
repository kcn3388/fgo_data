import json
import re

from download.download import *
from path_and_json import *
from urllib.parse import quote


def download_svt():
    for each in res_paths:
        if not os.path.exists(each):
            os.mkdir(each)

    if os.path.exists(svt_path):
        try:
            with open(all_servant_path, 'r', encoding="utf-8") as f:
                svt = json.load(f)
            for i in svt:
                for j in i["online"]:
                    # 如果是从者
                    if j == "svt_icon":
                        local = os.path.join(svt_path, i["local"][j])
                        online = i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
                    # 如果是指令卡
                    rule = re.compile(r"(ultimate|card\d)_icon")
                    if re.match(rule, j):
                        local = os.path.join(card_path, i["local"][j])
                        online = i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
                    # 如果是职阶
                    if j == "class_icon":
                        local = os.path.join(class_path, i["local"][j])
                        online = i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
        except json.decoder.JSONDecodeError:
            print("不存在从者数据……跳过")
    else:
        print("不存在从者数据……跳过")


def download_cft():
    for each in res_paths:
        if not os.path.exists(each):
            os.mkdir(each)

    if os.path.exists(cft_path):
        try:
            with open(all_craft_path, 'r', encoding="utf-8") as f:
                cft = json.load(f)
            for i in cft:
                for j in i["online"]:
                    # 如果是礼装
                    if j == "cft_icon":
                        local = os.path.join(cft_path, i["local"][j])
                        online = i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
                    # 如果是技能
                    if j == "skill_icon":
                        local = os.path.join(skill_path, i["local"][j])
                        online = i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
        except json.decoder.JSONDecodeError:
            print("不存在礼装数据……跳过")
    else:
        print("不存在礼装数据……跳过")


def download_cmd():
    for each in res_paths:
        if not os.path.exists(each):
            os.mkdir(each)

    if os.path.exists(cmd_path):
        try:
            with open(all_command_path, 'r', encoding="utf-8") as f:
                cmd = json.load(f)
            for i in cmd:
                for j in i["online"]:
                    # 如果是纹章
                    if j == "cmd_icon":
                        local = os.path.join(cmd_path, i["local"][j])
                        online = i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
                    # 如果是技能
                    if j == "skill_icon":
                        local = os.path.join(skill_path, i["local"][j])
                        online = i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
        except json.decoder.JSONDecodeError:
            print("不存在纹章数据……跳过")
    else:
        print("不存在纹章数据……跳过")


def download_icon_skill():
    for each in res_paths:
        if not os.path.exists(each):
            os.mkdir(each)
    root_url = "https://fgo.wiki/w/技能一览/技能图标"
    icon_list_url = "https://fgo.wiki/index.php?title=模板:技能图标一览&action=edit"
    try:
        raw_html = requests.get(root_url, timeout=20, headers=headers).text
        raw_icon_html = requests.get(icon_list_url, timeout=20, headers=headers).text
    except Exception as e:
        print(f"aiorequest error: {e}")
        return e

    all_skill_icons = re.search(r"图标列表\n\|(.+)\n\|;;}}{{#vardefine", raw_icon_html)
    if not all_skill_icons:
        return
    raw_skill_icons = all_skill_icons.group(1)
    skill_icons = raw_skill_icons.split(";;")
    for each_icon in skill_icons:
        local_icon = f"{each_icon}.png"
        raw_icon_url = re.search(rf"https://media.fgo.wiki/./../{quote(each_icon)}.png", raw_html)
        if each_icon == "被暴击发生耐性提升" and not raw_icon_url:
            local_icon = f"{each_icon}2.png"
            raw_icon_url = re.search(rf"https://media.fgo.wiki/./../{quote(each_icon)}2.png", raw_html)

        online_icon = raw_icon_url.group(0) if raw_icon_url else ""
        if not online_icon:
            print(f"get skill icon {each_icon} fail: 404")
            continue

        local = os.path.join(skill_path, local_icon)
        if os.path.exists(local):
            continue
        print(f"======开始下载：{local}======")
        download_stat = download(online_icon, local)
        if not isinstance(download_stat, int):
            print("download icons error, reason: " + str(download_stat))
