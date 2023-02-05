// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract MidiNFT {
    // Define the struct to store the information of each NFT: (TODO: convert to an NFT)
    struct MidiPiece {
        address owner;
        string ipfsLink;
        uint256 fee;
    }
    // Define the address of the DAO wallet (public):
    address public daoWallet;       
    // Define the mapping to store the NFTs:
    mapping(uint256 => MidiPiece) midiPieces;
    // Define the counter to count the number of NFTs:
    uint256 midiPieceCounter;


    // constructor to accept the address of the DAO wallet:
    constructor(address _daoWallet) {
        daoWallet = _daoWallet;
    }
    // Define the function to create the NFT:
    function createMidiPiece(string memory _ipfsLink, uint256 _fee) public {
        uint256 id = midiPieceCounter;
        midiPieceCounter ++;
        midiPieces[id] = MidiPiece({
            owner: msg.sender,
            ipfsLink: _ipfsLink,
            fee: _fee
        });
    }
    // Define the function to access the link:

    function accessLink(uint256 id) public payable {
        MidiPiece storage midiPiece = midiPieces[id];
        require(midiPiece.fee <= msg.value, "The fee is not enough.");
        // Provide the link to the user
        // ...
    }
}
