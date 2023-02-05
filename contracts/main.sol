// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/math/SafeMath.sol";

contract MidiNFT {
    using SafeMath for uint256;

    // Define the struct to store the information of each NFT: (TODO: convert to an NFT)
    struct MidiPiece {
        address owner;
        string ipfsLink;
        uint256 cost;
        uint256 dao_fee_percent;
    }
    // Define the address of the DAO wallet (public):
    address public daoWallet;       
    // Define the mapping to store the NFTs:
    mapping(uint256 => MidiPiece) midiPieces;
    // Define the mapping to store the purchase information:
    mapping(uint256 => mapping(address => bool)) purchased;
    // Define the counter to count the number of NFTs:
    uint256 midiPieceCounter;


    // constructor to accept the address of the DAO wallet:
    constructor(address _daoWallet) {
        daoWallet = _daoWallet;
    }
    // Define the function to create the NFT:
    function createMidiPiece(string memory _ipfsLink,uint256 _cost, uint256 _dao_fee_percent) public {
        uint256 id = midiPieceCounter;
        midiPieceCounter ++;
        midiPieces[id] = MidiPiece({
            owner: msg.sender,
            ipfsLink: _ipfsLink,
            cost: _cost,
            dao_fee_percent: _dao_fee_percent
        });
    }
    // Define the function to access the link:

    function accessLink(uint256 id) public payable returns (string memory) {
        // Check if the user has purchased the NFT:
        // if not purchased, check if the fee is enough:
        MidiPiece storage current_midiPiece = midiPieces[id];
        if (!purchased[id][msg.sender]) {
            require(current_midiPiece.cost <= msg.value, "The fee is not enough to purchase.");
            // Transfer msg.value * dao_fee_percent to the DAO wallet:
            uint256 dao_fee = msg.value.mul(current_midiPiece.dao_fee_percent).div(100);
            payable(daoWallet).transfer(dao_fee);
            // Transfer the rest to the owner:
            uint256 owner_fee = msg.value.sub(dao_fee);
            payable(current_midiPiece.owner).transfer(owner_fee);
            // Update the purchase information:
            purchased[id][msg.sender] = true;
        }
        // Provide the link to the user
        return current_midiPiece.ipfsLink;
    }
}
