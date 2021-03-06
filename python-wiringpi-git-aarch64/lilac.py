#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'action-extra-aarch64'

def pre_build():
    aur_pre_build('python-wiringpi-git')
    add_arch(['aarch64'])

post_build = aur_post_build

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
