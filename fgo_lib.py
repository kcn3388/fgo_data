import json
from lib_online.lib_cft import *
from lib_online.lib_cmd import *
from lib_online.lib_svt import *
from path_and_json import *


def update_lib():
    with open(all_servant_path, 'r', encoding="utf-8") as f:
        svt = json.load(f)
    with open(all_craft_path, 'r', encoding="utf-8") as f:
        cft = json.load(f)
    with open(all_command_path, 'r', encoding="utf-8") as f:
        cmd = json.load(f)

    servants = []
    for each_svt in svt:
        data = lib_svt(each_svt)
        servants.append(data)

    if os.path.exists(lib_servant_path):
        try:
            old_servants = json.load(open(lib_servant_path, encoding="utf-8"))
            if not old_servants == servants:
                with open(lib_servant_path, "w", encoding="utf-8") as f:
                    f.write(json.dumps(servants, indent=2, ensure_ascii=False))
        except json.decoder.JSONDecodeError:
            pass
    else:
        with open(lib_servant_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(servants, indent=2, ensure_ascii=False))

    crafts = []
    for each_cft in cft:
        data = lib_cft(each_cft)
        crafts.append(data)

    if os.path.exists(lib_craft_path):
        try:
            old_crafts = json.load(open(lib_craft_path, encoding="utf-8"))
            if not old_crafts == crafts:
                with open(lib_craft_path, "w", encoding="utf-8") as f:
                    f.write(json.dumps(crafts, indent=2, ensure_ascii=False))
        except json.decoder.JSONDecodeError:
            pass
    else:
        with open(lib_craft_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(crafts, indent=2, ensure_ascii=False))

    commands = []
    for each_cmd in cmd:
        data = lib_cmd(each_cmd)
        commands.append(data)

    if os.path.exists(lib_command_path):
        try:
            old_commands = json.load(open(lib_command_path, encoding="utf-8"))
            if not old_commands == commands:
                with open(lib_command_path, "w", encoding="utf-8") as f:
                    f.write(json.dumps(commands, indent=2, ensure_ascii=False))
        except json.decoder.JSONDecodeError:
            pass
    else:
        with open(lib_command_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(commands, indent=2, ensure_ascii=False))
