#!/usr/bin/env python
from genericpath import isfile
import os
from colorama import init as init_colorama, Fore as ForeColor


init_colorama()


def validate_dir(dir_name):
    error = False
    for fn in os.listdir(dir_name):
        fn_path = os.path.join(dir_name, fn)
        if os.path.isdir(fn_path) and not fn.startswith("."):
            card_fn = fn_path + ".card.md"
            if not os.path.exists(card_fn):
                print(f"{ForeColor.RED}ERROR:{ForeColor.RESET} card file {card_fn} not found")
                error = True
        if os.path.isfile(fn_path) and fn.endswith(".card.md"):
            card_path = fn[:-len(".card.md")]
            if card_path == "template":
                continue
            full_card_path = os.path.join(dir_name, card_path)
            if not os.path.isdir(full_card_path):
                print(f"{ForeColor.RED}ERROR:{ForeColor.RESET} card file {full_card_path} has no corresponding path")
    return error


if __name__ == "__main__":
    error = False
    for fn in os.listdir("."):
        if os.path.isdir(fn) and not fn.startswith("."):
            error |= validate_dir(fn)
    if not error:
        print(f"{ForeColor.GREEN}No errors found!{ForeColor.RESET}")