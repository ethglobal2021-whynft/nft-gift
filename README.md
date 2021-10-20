# nft-gift
Before Hack, we had experience working with NFT, and we realized that people often buy NFT to resell it.

To make NFT market strong, we need to come up with some kind of strong collect use case. But why do people need to collect NFT?

Once we met an example in real life: one woman wanted to buy an artwork of a famous artist as a gift to her boss. Neither the boss nor the woman understood anything about the crypt, but the artwork had to be presented. We realized that there is a demand for gifts in the NFT and created an easy way to receive such gifts. This may be needed not only by ordinary people, but also by companies and charitable foundations, and various NFT agencies and Gamers.

## User Flow
### Centralized Version (current)
- Sender wants to make a nft gift
- We buy the gift (NFT) sender want (so, we own the NFT)
- We prepare hashed secured link and give it to sender or via email, etc. to receiver
- With link receiver specify wallet and wait for transfer (from our address to specified address) to be completed (rarible transfer)

### Decentralized Version
Our solution consists of two parts: special smart contract and backend. The key point is that only smart contract will be granted to make transfer, so centralized part (our backend) remains trustless. The backend denies all transfer permissions to wrong address and smart contract perform transfer by checking password from receiver.

Backend consists of javascript blockchain callers (here we use rarible nftABI and rarible wrapper of  "safeTransferFrom" method) and local database to track & match pending gifts. Client part uses only javascript code.  

An examples of a fully worked out scenario (contracts): 
- https://rinkeby.etherscan.io/address/0x0264837577091a402a6A62738a9e5Fecad107407
- https://rinkeby.etherscan.io/address/0xd4Ba7daA7F3A5DbE2453210C4D458959687C20a6

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
