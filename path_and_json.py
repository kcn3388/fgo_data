import os
import requests

from typing import Union

headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn"
}

banned_id = ["333", "240", "168", "151", "152", "149", "83"]

runtime_path = os.path.dirname(__file__)

basic_path = os.path.join(runtime_path, "img", "fgo")
icon_path = os.path.join(basic_path, "icons")
svt_path = os.path.join(icon_path, "svt_icons")
cft_path = os.path.join(icon_path, "cft_icons")
skill_path = os.path.join(icon_path, "skill_icons")
cmd_path = os.path.join(icon_path, "cmd_icons")
card_path = os.path.join(icon_path, "card_icons")
class_path = os.path.join(icon_path, "class_icons")

res_paths = [basic_path, icon_path, svt_path, cft_path, skill_path, cmd_path, card_path, class_path]

data_path = os.path.join(runtime_path, 'data')
news_img_path = os.path.join(runtime_path, 'news')
banner_path = os.path.join(data_path, 'banner.json')
config_path = os.path.join(data_path, 'config.json')
pools_path = os.path.join(data_path, 'pools.json')
gacha_path = os.path.join(data_path, 'gacha.json')
lucky_path = os.path.join(data_path, 'lucky_bag.json')
banner_data_path = os.path.join(data_path, 'b_data.json')
update_data_path = os.path.join(data_path, 'update.json')

old_pools_path = os.path.join(runtime_path, 'data/old_pools.json')

news_path = os.path.join(data_path, 'news.json')
news_detail_path = os.path.join(data_path, 'news_detail.json')

static_path = os.path.join(runtime_path, 'res')
seal_path = os.path.join(static_path, '海の翁.jpg')
frame_path = os.path.join(static_path, 'background.png')
back_path = os.path.join(static_path, 'back.jpg')
back_cn_path = os.path.join(static_path, 'back_cn.png')
mask_path = os.path.join(static_path, 'mask.png')
font_path = os.path.join(static_path, 'SourceHanSansSC-Regular.otf')

crt_folder_path = os.path.join(runtime_path, "crt")
crt_path = "ca-certificates.crt"

all_servant_path = os.path.join(data_path, "all_svt.json")
all_command_path = os.path.join(data_path, "all_cmd.json")
all_craft_path = os.path.join(data_path, "all_cft.json")

lib_servant_path = os.path.join(data_path, "lib_svt.json")
lib_command_path = os.path.join(data_path, "lib_cmd.json")
lib_craft_path = os.path.join(data_path, "lib_cft.json")

all_json = [
    banner_path, config_path, pools_path, gacha_path, lucky_path,
    banner_data_path, update_data_path, old_pools_path,
    news_path, news_detail_path,
    all_servant_path, all_command_path, all_craft_path,
    lib_servant_path, lib_command_path, lib_craft_path
]


def get_content(url: str) -> Union[Exception, bytes]:
    try:
        return requests.get(url, timeout=20, headers=headers).content
    except Exception as e:
        return e
