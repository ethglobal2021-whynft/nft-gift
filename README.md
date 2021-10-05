# nft-gift

## User Flow
### Centralized Version (current)
- Sender wants to present a gift
- Buy the gift (NFT) to our centralized account
- Prepare hashed secured link and send it to email
- With link specify wallet and wait for transfer (from the centralized to specified address) to be completed

### Decentralized Version
todo: describe

## Debug
2 simple steps:

1. Create your env file from `.env.example`
(or merely copy the one: for debug it is okie)
2. From the current project directory (where `docker-compose.yml`) run:
```bash
docker-compose up --build
```
3. By defaults in `.env.example` there is prepared 1 gift with its special debug url to obtain. To go to the page proceed to:
`http://localhost:8000/gift/foo`

### To stop
`cntrl + c`

### To create new gift
- via django admin or via db connector go to gift table and create a link with specifying corresponding  rarible meta.
- check the link after that it works as expected
