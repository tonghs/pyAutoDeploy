#coding=utf-8
import os
import sqlite3
from configs import setting, db
import sys
reload(sys)
sys.setdefaultencoding('utf8')
__author__ = 'Administrator'


def execute(key, value, exe_time):
    ret_msg = setting.STATE_FAIL
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
    content = ''
    if len(jobs):
        job = jobs[0]
        try:
            project_dir = '%s/%s/' % (job[0], job[1])
            content += '$ cd %s' % project_dir
            os.chdir(project_dir)

            content += '<br>$ git pull<br>'
            content += os.popen('git pull').read()

            #返回原路径
            content += '<br>$ cd %s' % (setting.CUR_DIR % '')
            os.chdir(setting.CUR_DIR % '')

            content += '<br>$ chmod 777 %scmd.sh' % project_dir
            content += os.popen('chmod 777 %scmd.sh' % project_dir).read()

            content += '<br>$ %s/cmd.sh<br>' % project_dir
            content += os.popen('%s/cmd.sh' % project_dir).read()

            content += '<br>$ chmod 644 %scmd.sh' % project_dir
            content += os.popen('chmod 644 %scmd.sh' % project_dir).read()

            conn.execute(db.UPDATE_JOB % (setting.STATE_SUCCESS, exe_time, int(job[2])))
            ret_msg = setting.STATE_SUCCESS

            conn.execute(db.INSERT_TO_LOG % (int(job[2]), exe_time, ret_msg, content))
        except Exception, e:
            ret_msg = setting.STATE_FAIL
            content += '<br><br>************发生错误************<br><br>'
            content += '<br>cd %s<br>' % (setting.CUR_DIR % '')
            #返回原路径
            os.chdir(setting.CUR_DIR % '')
            content += '<br>错误:<br> %s' % e
            conn.execute(db.UPDATE_JOB % (setting.STATE_FAIL, exe_time, int(job[2])))
            conn.execute(db.INSERT_TO_LOG % (int(job[2]), exe_time, ret_msg, content))

    conn.commit()
    cur.close()
    conn.close()

    return ret_msg


def insert_to_log(conn, job_id, exe_time, state, content):
    conn = sqlite3.connect(db.DB)
    conn.execute(db.INSERT_TO_LOG % (int(job_id), exe_time, state, content))
    conn.commit()
    conn.close()