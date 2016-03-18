#! /bin/bash

nohup /opt/logstash/bin/logstash agent -f /etc/logstash/conf.d/ > /dev/null 2>&1&
