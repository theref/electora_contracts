# electora
--------

## Minimum viable product
A web app that allows Admins to login and create Elections.
Admins whitelist Voters (by email) and set the Candidates.
Voters can login and participate in Elections by voting.
An Election has a smart contract and all Voters have a pre-populated and funded key-pair.
When a Voter votes, they are signing a tx that interacts with the smart contract.
At the Election closing point, results are published.

### Smart Contract
Will be written in Solidity and initially published to a test network.
Rinkeby and Kovan are ETH test networks.
Brownie will be used for Solidity development.

The smart contract needs to be configurable because number of voters and candidates will always change.

### Web App
Will be done using Anvil.
Needs a db for storing Admins, Candidates, Voters, key-pairs.
Backend will handle creating and deploying the smart contract for the Election.
Front end will handle voting.

## Dev Setup
Install `docker` https://docs.docker.com/get-docker/

Install `pipx` via https://pypa.github.io/pipx/installation/
```
pipx install pre-commit black isort
```

Clone this repo:
```
git clone git@gitlab.com:theref/electora.git
cd electora
pre-commit install
```

To run the tests
```
docker build -t electora-brownie .
docker run --rm -v $PWD:/usr/src electora-brownie brownie test
```
