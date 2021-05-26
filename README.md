# EFK-Stack-Demo
Elasticsearch, Fluentd and Kibana (EFK) Dema on Ubuntu installed on VirtualBox


### OS Requirement
Windows or Linux (Using ubuntu OS installed on Oracle Virtual Box)

### Setup required : 
#### Java installation is mandatory 

#### Python installation
For writing program which will generate log that can be viewed in kibana

#### Curl 
sudo apt install curl

#### Elastic Search 
Download Elastics Search from https://www.elastic.co/downloads/elasticsearch - Used version 7.12.1
Unzip the file in download section (You can choose any location but make sure you accordingly update the path in execute.sh)

#### Kibana
Download Elastics Search from https://www.elastic.co/downloads/elasticsearch - Used version 7.12.1
(Make sure you use the same version of elastic search and kibana

#### Fluentd
curl -L https://toolbelt.treasuredata.com/sh/install-ubuntu-trusty-td-agent3.sh | sh
sudo apt-get install make libcurl4-gnutls-dev --yes
sudo apt-get install build-essential
sudo /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-elasticsearch


### Configuration Required :





