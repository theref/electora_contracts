import brownie
from brownie import SimpleVote, accounts
from web3 import Web3


def test_add_to_whitelist():
    owner = accounts[0]
    voter = accounts.add()
    funding_amount = Web3.toWei(0.01, "ether")
    simple_vote = SimpleVote.deploy(funding_amount, 0, {"from": owner})
    tx = simple_vote.whitelistAddress(voter, {"from": owner, "value": funding_amount})
    tx.wait(1)
    assert voter.balance() == funding_amount


def test_add_to_whitelist_with_wrong_acccount():
    owner = accounts[0]
    voter = accounts.add()
    funding_amount = Web3.toWei(0.01, "ether")
    simple_vote = SimpleVote.deploy(funding_amount, 0, {"from": owner})
    with brownie.reverts():
        simple_vote.whitelistAddress(
            voter, {"from": accounts[1], "value": funding_amount}
        )


def test_create_candidate_array():
    owner = accounts[0]
    funding_amount = Web3.toWei(0.01, "ether")
    simple_vote = SimpleVote.deploy(funding_amount, 2, {"from": owner})
    assert simple_vote.votes(0) == 0
    assert simple_vote.votes(1) == 0
    with brownie.reverts():
        simple_vote.votes(2)


def test_vote_for_candidate():
    owner = accounts[0]
    voter = accounts.add()
    funding_amount = Web3.toWei(0.01, "ether")
    simple_vote = SimpleVote.deploy(funding_amount, 2, {"from": owner})
    tx = simple_vote.whitelistAddress(voter, {"from": owner, "value": funding_amount})
    tx.wait(1)
    tx = simple_vote.vote(0, {"from": voter})
    tx.wait(1)
    assert simple_vote.votes(0) == 1


def test_cannot_vote_twice():
    owner = accounts[0]
    voter = accounts.add()
    funding_amount = Web3.toWei(0.01, "ether")
    simple_vote = SimpleVote.deploy(funding_amount, 2, {"from": owner})
    tx = simple_vote.whitelistAddress(voter, {"from": owner, "value": funding_amount})
    tx.wait(1)
    tx = simple_vote.vote(0, {"from": voter})
    tx.wait(1)
    with brownie.reverts():
        tx = simple_vote.vote(0, {"from": voter})
        tx.wait(1)
