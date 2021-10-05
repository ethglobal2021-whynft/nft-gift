import HDWalletProvider from "@truffle/hdwallet-provider"
import Web3 from "web3"
import axios from "axios"

import { createRaribleSdk } from "@rarible/protocol-ethereum-sdk"

import { toAddress } from "@rarible/types"
import { toBigNumber } from "@rarible/types"
import { Web3Ethereum } from "@rarible/web3-ethereum"

import FormData from "form-data"; // a nodejs module.
global.FormData = FormData; // hack for nodejs;

import fetchApi from "node-fetch"; // a nodejs module.
global.window = {
    fetch: fetchApi,
}
//global.window = {fetch: {bind: }}

// DO NOT PUSH PRIVATE KEYS IN PUBLIC REPO!
const config = {
	mainnetRpc: "https://mainnet.infura.io/v3/84653a332a3f4e70b1a46aaea97f0435",
 	rinkebyRpc: "https://rinkeby.infura.io/v3/84653a332a3f4e70b1a46aaea97f0435",
 	rinkeby: "rinkeby"
}


export async function Transfer(user_address, contract_address, token_address, debug, privateKeyExt) {
    const maker = new HDWalletProvider(privateKeyExt, config.rinkebyRpc)
    const web3 = new Web3(maker)
    const from_address = "0xa7A1462A3F067E959a4DDD0630F49BE15716341E"
    return await createTransfer(web3, contract_address, token_address, from_address, user_address, privateKeyExt, debug)
}

export async function createTransfer(web3, contractAddress, tokenAddress, from_address, to_address, privateKey, debug) {
    const ethereum = new Web3Ethereum({ web3, gas: 200000})
    const sdk = createRaribleSdk(ethereum, config.rinkeby)
    const [from] = from_address
    const contract = toAddress(contractAddress)
    const tokenId = toBigNumber(tokenAddress)
    if (debug == "DEBUG") {
        console.log("DEBUG")
        console.log(contract, tokenId, tokenAddress, from)
        return "DEBUG_HASH"
    }
    const hash = await sdk.nft.transfer(
        {
            assetClass: "ERC721",
            contract: contract,
            tokenId: tokenId,
        },
        to_address,
        from
    )
    return hash
}