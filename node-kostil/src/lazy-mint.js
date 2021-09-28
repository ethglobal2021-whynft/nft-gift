import HDWalletProvider from "@truffle/hdwallet-provider"
import Web3 from "web3"
import axios from "axios"
//import { signTypedData_v4 } from "eth-sig-util"
//import { privateToAddress } from "ethereumjs-util"

//require("@rarible/protocol-ethereum-sdk")

import { createRaribleSdk } from "@rarible/protocol-ethereum-sdk"

import { toAddress } from "@rarible/types"
import { toBigNumber } from "@rarible/types"
import { Web3Ethereum } from "@rarible/web3-ethereum"

//import commonPkg from '@rarible/protocol-ethereum-sdk';
//const { common } = commonPkg;

//const {ff} = common.transferErc721;
//import transferErc721 from commonPkg;
//import { send as sendTemplate } from "@rarible/protocol-ethereum-sdk/src/common"
//import { transferErc721 } from "@rarible/protocol-ethereum-sdk/src/common/transfer-erc721"

//import { common } from "@rarible/protocol-ethereum-sdk";
//const { send } from common

//const sdk = createRaribleSdk(web3, env, { fetchApi: fetch })

//const FormData = require("form-data");
//import FormData from "form-data";
import FormData from "form-data"; // a nodejs module.
global.FormData = FormData; // hack for nodejs;

import fetchApi from "node-fetch"; // a nodejs module.
global.window = {
    fetch: fetchApi,
}
//global.window = {fetch: {bind: }}

//web3.eth.sendTransaction({from: acct1, to:acct2, value: web3.toWei(1, 'ether'), gasLimit: 21000, gasPrice: 20000000000})

// DO NOT PUSH PRIVATE KEYS IN PUBLIC REPO!
const config = {
	privateNafthaleneIos: "",
	rpc: "https://mainnet.infura.io/v3/84653a332a3f4e70b1a46aaea97f0435"
}
const client = axios.create({
	baseURL: "https://api.rarible.com"
})

const privateKey = config.private

function extractAddress(privateKey) {
  return `0x${privateToAddress(Buffer.from(privateKey, "hex")).toString("hex")}`
}

function getAddress(type) {
    if (type != "ERC721") {
         throw new Error("expect only ERC721 token type")
    }
	return "0x60F80121C31A0d46B5279700f9DF786054aa5eE5"
}

export async function frontendToPrivateKey(frontend) {
    if (frontend == "NAFTHALENE_IOS") {
        return config.privateNafthaleneIos
    }
    if (frontend == "WHYNFT_WEB") {
        return config.privateWhynftWeb
    }
    if (frontend == "WHYNFT_INSTAGRAM_IOS") {
        return config.privateInstagramIos
    }
    if (frontend == "TEST_FRONTEND") {
        return config.privateTestAccount
    }
    throw new Error("frontend name error")
}

export async function Transfer(user_address, contract_address, token_address, debug, privateKeyExt) {
    const maker = new HDWalletProvider(privateKeyExt, config.rpc)
    const web3 = new Web3(maker)
    const from_address = "0xa7A1462A3F067E959a4DDD0630F49BE15716341E"
    return await createTransfer(web3, contract_address, token_address, from_address, user_address, privateKeyExt, debug)
}

export async function createTransfer(web3, contractAddress, tokenAddress, from_address, to_address, privateKey, debug) {
    const ethereum = new Web3Ethereum({ web3, gas: 200000})
    const sdk = createRaribleSdk(ethereum, 'mainnet')
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
