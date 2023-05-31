
from download.download_all_res import *
from get.get_all_cft import *
from get.get_all_cmd import *
from get.get_all_svt import *


def get_all_mooncell():
    get_all_svt()
    get_all_cft()
    get_all_cmd()


def down_all_card_res():
    download_svt()
    download_cft()
    download_cmd()
