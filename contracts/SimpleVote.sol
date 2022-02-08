// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract SimpleVote is Ownable, AccessControl {
    bytes32 public constant REGISTERED_VOTER = keccak256("REGISTERED_VOTER");
    uint256 fundingAmount;
    mapping(uint256 => uint256) public votes;

    constructor(uint256 _fundingAmount) {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        fundingAmount = _fundingAmount;
    }

    function whitelistAddress(address payable user) public payable onlyOwner {
        grantRole(REGISTERED_VOTER, user);
        user.transfer(fundingAmount);
    }
}
