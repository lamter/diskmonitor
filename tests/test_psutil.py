#coding:utf-8
import psutil


def test_disk_partitions():
    for d in psutil.disk_partitions():
        print(d)


def test_disk_usage():
    disk_usage = psutil.disk_usage('/')
    print(disk_usage.total / 1000 / 1000 / 1000)



def test_disk_io_counters():
    sdiskio = psutil.disk_io_counters()
    print(sdiskio)



def test_judge():
    