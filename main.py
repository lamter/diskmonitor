# coding:utf-8

import logging
import logging.config
import psutil  # pip install psutil
import json

kwargs_json = 'conf/disk_limit.json'
logging_conf = 'conf/logging.conf'

logging.config.fileConfig(logging_conf)
logger = logging.getLogger()

with open(kwargs_json, 'r') as f:
    kwargs = json.load(f)

HOST = kwargs['host']
disks = kwargs['disks']


def monitor_disk(disk, limit):
    disk_percent = psutil.disk_usage(disk).percent
    if disk_percent > limit:
        # 超过显示，进行 warning
        logger.warning('host:{}\t磁盘:{}\t用量 {}%'.format(HOST, disk, disk_percent))
    else:
        logger.info('host:{}\t磁盘:{}\t用量 {}%'.format(HOST, disk, disk_percent))


for disk, limit in disks.items():
    monitor_disk(disk, limit)
