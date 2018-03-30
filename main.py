# coding:utf-8

import logging
import logging.config
import psutil  # pip install psutil
import json
from collections import OrderedDict

kwargs_json = 'conf/disk_limit.json'
logging_conf = 'conf/logging.conf'

logging.config.fileConfig(logging_conf)
logger = logging.getLogger()

with open(kwargs_json, 'r') as f:
    kwargs = json.load(f)

HOST = kwargs['host']
disks = kwargs['disks']


def monitor_disk(disk, limit):
    disk_usage = psutil.disk_usage(disk)
    # 进行 GB 换算
    to_GB = lambda x: round(x / 1000 / 1000 / 1000, 2)

    usage = OrderedDict((
        ("host", HOST),
        ("total", to_GB(disk_usage.total)),
        ("used", to_GB(disk_usage.used)),
        ("free", to_GB(disk_usage.free)),
        ("percent", int(disk_usage.percent)),
    ))

    log = '\nhost:{host}\ntotal:{total}GB\nused:{used}GB\nfree:{free}GB\npercent:{percent}%'.format(**usage)

    if eval(limit.format(**usage)):
        # 超过显示，进行 warning
        logger.warning(log)
    else:
        logger.info(log)


for disk, limit in disks.items():
    monitor_disk(disk, limit)
