import copy
import re

from bs4 import BeautifulSoup

from lib_online.lib_json import *
from path_and_json import *


def lib_cft(cft_data: dict) -> dict:
    url = "https://fgo.wiki/w/" + cft_data["name_link"]
    print("查询礼装" + cft_data["id"] + "……")
    cft = {
        "id": cft_data["id"],
        "name": cft_data["name"],
        "name_other": None,
        "name_link": cft_data["name_link"],
        "type": cft_data["type"]
    }

    if "local" in cft_data:
        cft["cft_icon"] = cft_data["local"]["cft_icon"]
        cft["skill_icon"] = cft_data["local"]["skill_icon"]
    else:
        cft["cft_icon"] = cft_data["cft_icon"]
        cft["skill_icon"] = cft_data["skill_icon"]

    if isinstance(cft_data["name_other"], list):
        cft["name_other"] = cft_data["name_other"]
    else:
        cft["name_other"] = cft_data["name_other"].split("&")

    if len(cft["name_other"]) == 1 and cft["name_other"][0] == "":
        cft["name_other"] = []

    try:
        response = requests.get(url, timeout=20, headers=headers)
    except Exception as e:
        cft["error"] = [f"cft{cft['id']} aiorequest error: {e}"]
        return cft

    raw_html = response.text
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        cfts = soup.find(class_="wikitable nodesktop").find("tbody")
    except Exception as e:
        cft["error"] = [f"cft{cft['id']} first bs error: {e}"]
        return cft

    info = [cfts.find("a", title="画师一览").text.strip() if cfts.find("a", title="画师一览") else ""]
    effect_soup = cfts.find_all("th")
    rule_effect = re.compile(r"Cost|HP|ATK")
    for each_es in effect_soup:
        next_es = each_es.find_next("td")
        if re.match(rule_effect, each_es.text.strip()):
            info.append(next_es.text.strip())

    info_soup = cfts.find_all("div", class_="poem")
    for each_is in info_soup:
        next_p = each_is.find_next("p")
        if next_p:
            info.append(next_p.text.strip())
        else:
            info.append("")

    detail_counter = 0
    single_cft_detail = copy.deepcopy(cft_detail)
    for each_cd in single_cft_detail:
        single_cft_detail[each_cd] = info[detail_counter]
        detail_counter += 1
    cft["detail"] = single_cft_detail

    card_url = ""
    curl_soup = cfts.find_all("span")
    for each_cls in curl_soup:
        if each_cls.text.strip() == "卡面为游戏资源原始图片，未经任何处理。":
            curl_soup = each_cls
            break

    try:
        curl_soup = curl_soup.find_next("img").get("data-srcset")
        rule_card = re.compile(r"/images/.+?.\.(?:png|jpg)")
        card_set = re.findall(rule_card, curl_soup)
        card_url = card_set[-1]
    except Exception as e:
        if "error" in cft:
            cft["error"].append(f"cft{cft['id']} get card img error: {e}")
        else:
            cft["error"] = [f"cft{cft['id']} get card img error: {e}"]
        pass

    cft["cards_url"] = card_url

    star = ""
    try:
        rule_star = re.compile(r"wgCategories.+星")
        star = re.search(rule_star, raw_html).group(0)
        star = star.split("\"")[-1].split("星")[0]
    except Exception as e:
        if "error" in cft:
            cft["error"].append(f"cft{cft['id']} get star error: {e}")
        else:
            cft["error"] = [f"cft{cft['id']} get star error: {e}"]
        pass

    cft["rare"] = star + "星"

    return cft
