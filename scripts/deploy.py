# SPDX-License-Identifier: MIT
#
# Copyright (c) 2021 The electora project team members listed at
# https://gitlab.com/theref/electora/-/graphs/main
#
# This software is published at https://github.com/theref/electora

from brownie import SimpleStorage, accounts, config, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if (network.show_active) == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
