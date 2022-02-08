import brownie
from brownie import SimpleVote, accounts
from web3 import Web3


def test_add_to_whitelist():
    owner = accounts[0]
    voter = accounts.add()
    funding_amount = Web3.toWei(0.01, "ether")
    simple_vote = SimpleVote.deploy(funding_amount, {"from": owner})
    tx = simple_vote.whitelistAddress(voter, {"from": owner, "value": funding_amount})
    tx.wait(1)
    assert voter.balance() == funding_amount


def test_add_to_whitelist_with_wrong_acccount():
    owner = accounts[0]
    voter = accounts.add()
    funding_amount = Web3.toWei(0.01, "ether")
    simple_vote = SimpleVote.deploy(funding_amount, {"from": owner})
    with brownie.reverts():
        simple_vote.whitelistAddress(
            voter, {"from": accounts[1], "value": funding_amount}
        )


# def test_whitelist_user_can_vote():
#     owner = accounts[0]
#     voter = accounts.add()
#     funding_amount = Web3.toWei(0.01, "ether")
#     simple_vote = SimpleVote.deploy(funding_amount, {"from": owner})
#     tx = simple_vote.whitelistAddress(voter, {"from": owner, "value": funding_amount})
#     tx.wait(1)
#     candidate = "A"
#     tx = simple_vote.vote(candidate, {"from": voter})
#     tx.wait(1)
#     assert simple_vote.getVote(voter) == "A"
