#coding=utf-8
import os
import sqlite3
from configs import setting, db

__author__ = 'Administrator'


def execute(key, value, exe_time):
    ret_msg = setting.STR_MSG_FAIL
    if key == 'url':
        sql = db.SELECT_DIR_FROM_JOB_BY_URL % value
    elif key == 'id':
        sql = db.SELECT_DIR_FROM_JOB_BY_ID % int(value)
    else:
        return ret_msg

    conn = sqlite3.connect(db.DB)
    cur = conn.cursor()
    cur.execute(sql)
    jobs = cur.fetchall()

    if len(jobs):
        job = jobs[0]
        try:
            project_dir = '%s/%s/' % (job[0], job[1])
            os.chdir(project_dir)
            os.popen('git pull')
            #返回原路径
            os.chdir(setting.CUR_DIR % '')
            os.popen('chmod 777 %scmd.sh' % project_dir)
            os.popen('%s/cmd.sh' % project_dir)
            os.popen('chmod 644 %scmd.sh' % project_dir)
            conn.execute(db.UPDATE_JOB % (setting.STR_MSG_SUCCESS, exe_time, int(job[2])))
            ret_msg = setting.STR_MSG_SUCCESS
        except Exception:
            #返回原路径
            os.chdir(setting.CUR_DIR % '')
            conn.execute(db.UPDATE_JOB % (setting.STR_MSG_FAIL, exe_time, int(job[2])))
            ret_msg = setting.STR_MSG_FAIL

    conn.commit()
    cur.close()
    conn.close()

    return ret_msg