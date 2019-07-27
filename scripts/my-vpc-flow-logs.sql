CREATE EXTERNAL TABLE IF NOT EXISTS vpc_flow_logs (
  version int,
  account string,
  interfaceid string,
  sourceaddress string,
  destinationaddress string,
  sourceport int,
  destinationport int,
  protocol int,
  numpackets int,
  numbytes bigint,
  starttime int,
  endtime int,
  action string,
  logstatus string
)
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ' '
LOCATION 's3://j-my-vpc-flowlogs/AWSLogs/674028589551/vpcflowlogs/us-east-2/'
TBLPROPERTIES ("skip.header.line.count"="1");


ALTER TABLE vpc_flow_logs
ADD PARTITION (dt='YYYY-MM-dd')
location 's3://j-my-vpc-flowlogs/AWSLogs/674028589551/vpcflowlogs/us-east-2/2019/07/26';



# create table on top of cloudtrail logs for querying data
CREATE EXTERNAL TABLE IF NOT EXISTS cloudtrail_logs_table(
eventversion STRING,
useridentity STRUCT<
       type:STRING,
       principalid:STRING,
       arn:STRING,
       accountid:STRING,
       accesskeyid:STRING,
       userName:STRING,
       sessioncontext:STRUCT<
           attributes:STRUCT<
               mfaauthenticated:STRING,
               creationdate:STRING>,
           invokedBy:STRING
       >,
        eventtime STRING,
        eventsource STRING,
        eventname STRING,
        awsregion STRING,
        sourceipaddress STRING,
        useragent STRING,
        requestparameters STRING,
        responseelements STRING,
        requestid STRING,
        eventid STRING,
        eventtype STRING,
        recipientaccountid STRING,
)


us-east-2/2019/07/26

PARTITIONED BY(
    region string,
    year string,
    month string,
    day string
)
ROW FORMAT SERDE 'com.amazon.emr.hive.serde.CloudTrailSerde'
STORED AS INPUTFORMAT 'com.amazon.emr.cloudtrail.CloudTrailInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://j-my-cloudtrail-logs/AWSLogs/674028589551/CloudTrail/';

# partition table

ALTER TABLE vpc_flow_logs
ADD PARTITION (
    dt='yyyy-mm-dd'
)
location 's3://j-my-cloudtrail-logs/AWSLogs/674028589551/CloudTrail/us-east-2//2019/07/27';



CREATE EXTERNAL TABLE cloudtrail_logs_table(
eventversion STRING,
useridentity STRUCT<
               type:STRING,
               principalid:STRING,
               arn:STRING,
               accountid:STRING,
               invokedby:STRING,
               accesskeyid:STRING,
               userName:STRING,
sessioncontext:STRUCT<
attributes:STRUCT<
               mfaauthenticated:STRING,
               creationdate:STRING>,
sessionissuer:STRUCT<
               type:STRING,
               principalId:STRING,
               arn:STRING,
               accountId:STRING,
               userName:STRING>>>,
eventtime STRING,
eventsource STRING,
eventname STRING,
awsregion STRING,
sourceipaddress STRING,
useragent STRING,
errorcode STRING,
errormessage STRING,
requestparameters STRING,
responseelements STRING,
additionaleventdata STRING,
requestid STRING,
eventid STRING,
resources ARRAY<STRUCT<
               ARN:STRING,
               accountId:STRING,
               type:STRING>>,
eventtype STRING,
apiversion STRING,
readonly STRING,
recipientaccountid STRING,
serviceeventdetails STRING,
sharedeventid STRING,
vpcendpointid STRING
)
PARTITIONED BY(region string,year string, month string, day string)
ROW FORMAT SERDE 'com.amazon.emr.hive.serde.CloudTrailSerde'
STORED AS INPUTFORMAT 'com.amazon.emr.cloudtrail.CloudTrailInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://j-my-cloudtrail-logs/AWSLogs/674028589551/CloudTrail/';


# replace with your specific settting
# region, year, month, day

ALTER TABLE cloudtrail_logs_table
ADD PARTITION (
    region='us-east-2',
    year=2019,
    month=07,
    day=27
)
location 's3://j-my-cloudtrail-logs/AWSLogs/674028589551/CloudTrail/us-east-2//2019/07/27';


