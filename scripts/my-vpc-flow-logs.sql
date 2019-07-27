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

