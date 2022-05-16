# SPDX-License-Identifier: MIT
#
# Copyright (c) 2021 The electora project team members listed at
# https://gitlab.com/theref/electora/-/graphs/main
#
# This software is published at https://github.com/theref/electora

# import ape
from ape import accounts, networks, project


def main():
    account = accounts.load("MetaMaskTest2")
    return account.deploy(project.SimpleVote)
