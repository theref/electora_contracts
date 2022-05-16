import ape
import pytest


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def voter(accounts):
    return accounts[1]


@pytest.fixture
def candidate(accounts):
    return accounts[3]


@pytest.fixture
def random(accounts):
    return accounts[2]
