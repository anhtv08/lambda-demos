 An Sample lambda function to support the cost management
 -----------
 
 Todo
 ====
 
 1. Using aws Parameter store to config the sns_arn name
 2. Using cloud formation template to define roles/policy and aws config rules with lambda function.
 
 
 
 Description
 -----------
 The function will terminate the ec2 instance which doest having required tags when it launch and sending notifiction using sns
 
 Build Run and deployment
 -----------
 
 ```
sh scripts/deploySamApp.sh

```
 
 Note
 -----------
 
The function is free of charge with free tier account and might occur some cost after free-tiered period complement
 
 
 
 