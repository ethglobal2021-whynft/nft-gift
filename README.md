# nft-gift

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
