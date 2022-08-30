#!/usr/bin/env python
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
    return error


if __name__ == "__main__":
    error = False
    for fn in os.listdir("."):
        if os.path.isdir(fn) and not fn.startswith("."):
            error |= validate_dir(fn)
    if not error:
        print(f"{ForeColor.GREEN}No errors found!{ForeColor.RESET}")