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
Download Kibana from https://www.elastic.co/downloads/elasticsearch - Used version 7.12.1 <br />
(Make sure you use the same version of elastic search and kibana

### - FluentD
Follow steps mentioned below
1. curl -L https://toolbelt.treasuredata.com/sh3install-ubuntu-trusty-td-agent3.sh | sh
2. sudo apt-get install make libcurl4-gnutls-dev --yes
3. sudo apt-get install build-essential
4. sudo /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-elasticsearch

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

Update config file /etc/td-agent/td-agent.conf (This file will have configuration for source and match) <br />
Have also attached the used configuration.

## Run 
Start Elastic Search service <br />
./[UnzipFilePath]/bin/elasticsearch

Start Kibana service <br />
./[UnzipFilePath]/bin/kibana

Start fluentd service <br />
sudo service td-agent start

******
  Some other used commands
  sudo service td-agent start
  sudo service td-agent stop
  sudo service td-agent restart
  sudo service td-agent status
  sudo tail -f /var/log/td-agent/td-agent.log

Execute below command to do all the above steps through shell <br />
sudo bash execute.sh "[Python File]" "[Log File Path]"
