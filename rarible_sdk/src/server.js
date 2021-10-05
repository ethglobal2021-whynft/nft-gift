'use strict';
import { Transfer } from './lazy-mint.js';


import express from 'express';

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App setUp
const app = express();
app.use(express.json());

app.post('/', async (request, response) => {
  // Pass ipfs & user_address
  console.log('get', request.body);
  try {
    const link = await Transfer(request.body.user_receiver, request.body.contract, request.body.token, request.body.sender_private_ext)
    console.log('Response with link', link);
    response.json({link: link, status: "OK"});
  } catch (error) {
    console.error(error);
    response.json({error: error, status: "ERROR"});
    return;
  }
});

app.get('/healthcheck', async (request, response) => {
  response.json({status: 'ok'});
});

app.listen(PORT, HOST);
console.log(`Express Kostil Server is running on http://${HOST}:${PORT}`);
