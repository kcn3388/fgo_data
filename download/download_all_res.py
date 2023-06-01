import json
import re

from download.download import *
from path_and_json import *


def download_svt():
    basic_url = "https://fgo.wiki"
    for each in res_paths:
        if not os.path.exists(each):
            os.mkdir(each)

    print("开始下载从者相关……")
    if os.path.exists(svt_path):
        try:
            with open(all_servant_path, 'r', encoding="utf-8") as f:
                svt = json.load(f)
            for i in svt:
                for j in i["online"]:
                    # 如果是从者
                    if j == "svt_icon":
                        local = os.path.join(svt_path, i["local"][j])
                        online = basic_url + i["online"][j]
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
                        online = basic_url + i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
                    # 如果是职阶
                    if j == "class_icon":
                        local = os.path.join(class_path, i["local"][j])
                        online = basic_url + i["online"][j]
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
    basic_url = "https://fgo.wiki"
    for each in res_paths:
        if not os.path.exists(each):
            os.mkdir(each)

    print("开始下载礼装相关……")
    if os.path.exists(cft_path):
        try:
            with open(all_craft_path, 'r', encoding="utf-8") as f:
                cft = json.load(f)
            for i in cft:
                for j in i["online"]:
                    # 如果是礼装
                    if j == "cft_icon":
                        local = os.path.join(cft_path, i["local"][j])
                        online = basic_url + i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
                    # 如果是技能
                    if j == "skill_icon":
                        local = os.path.join(skill_path, i["local"][j])
                        online = basic_url + i["online"][j]
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
    basic_url = "https://fgo.wiki"
    for each in res_paths:
        if not os.path.exists(each):
            os.mkdir(each)

    print("开始下载纹章相关……")
    if os.path.exists(cmd_path):
        try:
            with open(all_command_path, 'r', encoding="utf-8") as f:
                cmd = json.load(f)
            for i in cmd:
                for j in i["online"]:
                    # 如果是纹章
                    if j == "cmd_icon":
                        local = os.path.join(cmd_path, i["local"][j])
                        online = basic_url + i["online"][j]
                        if os.path.exists(local):
                            continue
                        print(f"======开始下载：{local}======")
                        download_stat = download(online, local)
                        if not isinstance(download_stat, int):
                            print("download icons error, reason: " + str(download_stat))
                    # 如果是技能
                    if j == "skill_icon":
                        local = os.path.join(skill_path, i["local"][j])
                        online = basic_url + i["online"][j]
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
