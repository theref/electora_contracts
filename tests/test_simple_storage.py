from brownie import SimpleStorage, accounts


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    assert starting_value == expected


def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    expected = 15
    txn = simple_storage.store(expected, {"from": account})
    txn.wait(1)
    assert expected == simple_storage.retrieve()


def test_add_person():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    txn = simple_storage.addPerson("james", 21, {"from": account})
    txn.wait(1)
    assert simple_storage.retrievePerson("james") == 21
