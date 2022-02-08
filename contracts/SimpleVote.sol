// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract SimpleVote is Ownable, AccessControl {
    bytes32 public constant REGISTERED_VOTER = keccak256("REGISTERED_VOTER");
    uint256 fundingAmount;
    uint256[] public votes;

    constructor(uint256 _fundingAmount, uint256 _num_candidates) {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        fundingAmount = _fundingAmount;
        votes = new uint256[](_num_candidates);
    }

    function whitelistAddress(address payable user) public payable onlyOwner {
        grantRole(REGISTERED_VOTER, user);
        user.transfer(fundingAmount);
    }

    function vote(uint256 candidate) public {
        require(hasRole(REGISTERED_VOTER, msg.sender));
        votes[candidate]++;
        renounceRole(REGISTERED_VOTER, msg.sender);
    }
}
