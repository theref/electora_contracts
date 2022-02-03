from brownie import SimpleVote, accounts
from web3 import Web3


def test_whitelist_address():
    account = accounts[0]
    simple_vote = SimpleVote.deploy(Web3.toWei(0.1, "ether"), {"from": account})
    simple_vote.whitelistAddress(accounts[1], {"from": account})
    assert accounts[1].balance() == Web3.toWei(0.1, "ether")
