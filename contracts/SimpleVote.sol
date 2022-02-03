// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

contract SimpleVote is Ownable {
    uint256 fundingAmount;
    mapping(address => bool) private registeredVoters;

    constructor(uint256 _fundingAmount) {
        fundingAmount = _fundingAmount;
    }

    function whitelistAddress(address payable user) public onlyOwner {
        registeredVoters[user] = true;
        user.transfer(fundingAmount);
    }
}
