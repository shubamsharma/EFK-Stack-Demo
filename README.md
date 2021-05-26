# EFK-Stack-Demo
Elasticsearch, Fluentd and Kibana (EFK) Demo on Ubuntu installed on VirtualBox


## OS Requirement
Windows or Linux (Using ubuntu OS installed on Oracle Virtual Box)

## Setup required : 
### - Java installation is mandatory 

### - Python installation
For writing program which will generate log that can be viewed in kibana

### - Curl 
sudo apt install curl

### - Elastic Search 
Download Elastics Search from https://www.elastic.co/downloads/elasticsearch - Used version 7.12.1 <br />
Unzip the file in download section (You can choose any location but make sure you accordingly update the path in execute.sh) 

### - Kibana
Download Elastics Search from https://www.elastic.co/downloads/elasticsearch - Used version 7.12.1 <br />
(Make sure you use the same version of elastic search and kibana

### - Logstash
Download Elastics Search from https://www.elastic.co/downloads/logstash - Used version 7.12.1 <br />
(Make sure you use the same version of elastic search, kibana and Logstash)

## Configuration Required
### - Elastic Search  
No change required (Default host url - http://localhost:9200)

### - Kibana
Make sure you use the same host on which the elastic search is running (Default is correct just uncomment it)
****
The URLs of the Elasticsearch instances to use for all your queries. <br />
elasticsearch.hosts: ["http://localhost:9200"]
****
Default host url for Kibana - http://localhost:5601

### - Fluentd

Create config file logstash_file.conf (This file will have configuration for input, filter and output) <br />
Have also attached the used configuration.

## Run 
Start Elastic Search service <br />
./[UnzipFilePath]/bin/elasticsearch

Start Kibana service <br />
./[UnzipFilePath]/bin/kibana

./[UnzipFilePath]/bin/logstash -r -f [ConfigFileCreatedAbove] # Need to attach the configuration with the logstach<br /> 

Execute below command to do all the above steps through shell <br />
sudo bash execute_logstash.sh "[Python File]" "[Full Log Path]" ["Config File Created Above"]
