#coding=utf-8
import os

__author__ = 'Administrator'

CUR_DIR_ORI = os.getcwd()
CUR_DIR = '%s/%%s' % CUR_DIR_ORI


STR_STATUS_SUCCESS = 'success'
STR_STATUS_FAIL = 'fail'

STATE_FAIL = 0
STATE_SUCCESS = 1
STATE_WAITING = 2

STATUS = ('已失败', '已成功', '未执行')
