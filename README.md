# nft-gift

## User Flow
### Centralized Version (current)
- Sender wants to make a nft gift
- We buy the gift (NFT) sender want (so, we own the NFT)
- We prepare hashed secured link and give it to sender or via email, etc. to receiver
- With link receiver specify wallet and wait for transfer (from our address to specified address) to be completed (rarible transfer)

### Decentralized Version
Our solution consists of two parts: special smart contract and backend. The key point is that only smart contract will be granted to make transfer, so centralized part (our backend) remains trustless. The backend denies all transfer permissions to wrong address and smart contract perform transfer by checking password from receiver.

Backend consists of javascript blockchain callers (here we use rarible nftABI and rarible wrapper of  "safeTransferFrom" method) and local database to track & match pending gifts. Client part uses only javascript code.  

An example of a fully worked out scenario (contract): https://rinkeby.etherscan.io/address/0xd4Ba7daA7F3A5DbE2453210C4D458959687C20a6

> check [research notebook](https://github.com/ethglobal2021-whynft/nft-gift/blob/main/research/darilka_contract_workflow.ipynb)

## ToDo

- [ ] compose files to deploy folder
- [ ] prod entrypoint and etc.
- [ ] deprecate `front/`
- [ ] debug off


## Debug
2 simple steps:

1. Create your env file from `.env.example`
(or merely copy the one: for debug it is okie)
2. From the current project directory (where `docker-compose.yml`) run:
```bash
docker-compose up --build
```
3. By defaults in `.env.example` there is prepared 1 gift with its special debug url to obtain. To go to the page proceed to:
`http://localhost:8000/gift/url-only-for-demonstration-dogu-without-transferring`

### To stop
`cntrl + c`

### To create a new gift
- via django admin or via db connector go to gift table and create a link with specifying corresponding  rarible meta.
- check the link after that it works as expected.
