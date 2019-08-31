Todo:
=======

A template to deploy application


Simple lambda example using
- RDS
- SQN
- API gateway


Flow of application as below
================

1. API gateway recieving request from client
2. An lambda function associate with API to get payload and putting to sqs
3. Lmabda function drail message from queue and store into db