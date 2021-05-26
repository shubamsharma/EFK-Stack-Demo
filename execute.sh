#!/bin/bash

cd /home/shubam/Downloads/elasticsearch-7.12.1/bin/
#./elasticsearch &
#sleep 120

cd /home/shubam/Downloads/kibana-7.12.1-linux-x86_64/bin/
#./kibana &
#sleep 120

#sudo service td-agent restart

python3 $1/main.py $2


