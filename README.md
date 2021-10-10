# nft-gift

## User Flow
### Centralized Version (current)
- Sender wants to make a nft gift
- We buy the gift (NFT) sender want to our address
- We prepare hashed secured link and send it via email to receiver
- With link receiver specify wallet and wait for transfer (from the our address to specified address) to be completed

### Decentralized Version
todo: describe

## ToDo

- [ ] compose files to deploy folder
- [ ] prod entrypoint and etc.
- [ ] deprecate `front/`
- [ ] debug off
- [ ] nft gift (domain) or nft.gifts


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
