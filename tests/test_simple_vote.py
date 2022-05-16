import brownie
import pytest
from brownie import SimpleVote, accounts, exceptions
from web3 import Web3


def test_add_to_whitelist():
    owner = accounts[0]
    voter = accounts.add()
    simple_vote = SimpleVote.deploy(0, {"from": owner})
    tx = simple_vote.whitelistAddress(voter, {"from": owner})
    tx.wait(1)
    assert simple_vote.hasRole(Web3.keccak(text="REGISTERED_VOTER"), voter)
    assert not simple_vote.hasRole(Web3.keccak(text="REGISTERED_VOTER"), accounts[1])


def test_add_to_whitelist_with_wrong_acccount():
    owner = accounts[0]
    voter = accounts.add()
    simple_vote = SimpleVote.deploy(0, {"from": owner})
    with pytest.raises(exceptions.VirtualMachineError):
        simple_vote.whitelistAddress(voter, {"from": accounts[1]})


def test_create_candidate_array():
    owner = accounts[0]
    simple_vote = SimpleVote.deploy(2, {"from": owner})
    assert simple_vote.votes(0) == 0
    assert simple_vote.votes(1) == 0
    with pytest.raises(exceptions.VirtualMachineError):
        simple_vote.votes(2)


def test_vote_for_candidate():
    owner = accounts[0]
    voter = accounts.add()
    simple_vote = SimpleVote.deploy(2, {"from": owner})
    tx = simple_vote.whitelistAddress(voter, {"from": owner})
    tx.wait(1)
    tx = simple_vote.vote(0, {"from": voter})
    tx.wait(1)
    assert simple_vote.votes(0) == 1


def test_cannot_vote_twice():
    owner = accounts[0]
    voter = accounts.add()
    simple_vote = SimpleVote.deploy(2, {"from": owner})
    tx = simple_vote.whitelistAddress(voter, {"from": owner})
    tx.wait(1)
    tx = simple_vote.vote(0, {"from": voter})
    tx.wait(1)
    with pytest.raises(exceptions.VirtualMachineError):
        tx = simple_vote.vote(0, {"from": voter})
        tx.wait(1)
