how to use lambda get .json files from s3 and input the data to the dynamoDB
===
* Create a policy
  * enter the `IAM` service
  * choose `policies`
  * create `policy`
  * choose `CloudWatch` service. Because this is a demo, we grant all resource and actions to it
  <img src="https://github.com/birdsdule/AWS-study/blob/master/pics/image1.png" width=275><br>
  * add `S3` service and `dynamoDB` in same way
  * here we name the policy as "s3_json_dynamoDB"
  * create a role, choose `lambda`->next->select the policy we just build->name it
* Build a S3 Bucket
  * follow with guide to build a simple S3
* Create the dynamoDB
  * create a dynamoDB. I choose the movie `release year` as partition key and movie `title` as range key
    <img src="https://github.com/birdsdule/AWS-study/blob/master/pics/image2.png" width=205><br>
* Build lambda function
  * select the role we create in step 1 at the `Execution role`
  * [demo_code](https://github.com/birdsdule/AWS-study/blob/master/codes/lambda_demo.py)<br>
  * cause the decode json data is in dict format, you can put the item just like the demo code or you can set data in following format  
    <img src="https://github.com/birdsdule/AWS-study/blob/master/pics/image3.png" width=155><br>
  * if the data file is too big, you have to extend the lambda timeout (rather than 3s default)
  * save the lambda
* Use cloudwatch to monitor and debug
  * because the default trigger is `file create action`, everytime we upload a new file into S3 bucket, it'll call the lambda once.
  * upload a json file
  * in the `logs` find the lambda we built
  * check the running result
  * if there are no error, we can see the data input into the dynamoDB successfully
