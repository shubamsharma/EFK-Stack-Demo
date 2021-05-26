import sys
import os
import json
import time
import datetime
from os.path import abspath, dirname,join

cur_path = os.path.dirname(str(sys.argv[1]))

log_file = cur_path + "/log.json"
log_json = dict()
log_json['Data'] = {}
print(log_file)
def main():
    i = 0
    while(True):
        print(i)
        i = i+1
        log_json['Data']['Count'] = i
        log_json['Created'] = datetime.datetime.utcnow().isoformat()

        with open(log_file,"a") as f:
            json.dump(log_json,f)#,ensure_ascii = False)
            f.write("\n")
        time.sleep(0.10)

main()

