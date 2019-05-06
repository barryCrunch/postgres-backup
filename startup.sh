#!/bin/bash

printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env.sh
cron -f
