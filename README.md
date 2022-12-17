# abra Assignment

## how to use

1. Create users in django admin app


2. Generate token using “token” endpoint 
(you need username & password)


3. Add token to the postman-collection-variables


4. Send messages, read messages


5. You can only delete messages sent or received by you


6. Get messages - in order to get all **unread** messages add 
{“messages”:”unread”} to request params, if you want to 
get **all** messages send the request without params.
