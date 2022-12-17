# abra Assignment

## how to use

1. Create users in django admin app


2. Generate a token using the “token” endpoint 
(you need to add username & password to the body request)


3. Add a token to the postman-collection-variables


4. Send messages (to other users by their username) & read messages


5. You can only delete messages sent or received by you


6. Get messages - in order to get all **unread** messages add 
{“messages”:”unread”} to request params, if you want to 
get **all** messages, send the request without params.
