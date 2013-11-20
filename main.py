#coding=utf-8
from datetime import datetime
import json
import os
import web
import sqlite3
from configs import db
from configs import setting

__author__ = 'Administrator'

urls = (
    '/push', 'push',
    '/', 'index',
    '/favicon.ico', 'faviconICO',
    '/install', 'install',
    '/add', 'add',
    '/del', 'delete',
    '/execute', 'execute',
)

app = web.application(urls, globals())
render = web.template.render('templates/', base='base')

class WebService(Daemon):
        def run(self):
            app.run()

if __name__ == '__main__':
    app.run()


class faviconICO(object):
   def GET(self):
       return web.seeother('/static/images/favicon.ico')

class index:
    def GET(self):
        conn = sqlite3.connect(db.DB)
        cur = conn.cursor()
        cur.execute('select status, name, addr, exe_time, id from tb_job;')
        jobs = []
        for job in cur:
            jobs.append(job)
        return render.index(jobs)


class push:
    def POST(self):
        exe_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        data = web.input()
        data = json.loads(data.payload)
        url = data['repository']['url']
        sql = 'select dir, name, id from tb_job where addr = "%s"' % url
        conn = sqlite3.connect(db.DB)
        cur = conn.cursor()
        cur.execute(sql)
        for job in cur:
            os.chdir('%s/%s' % (job[0], job[1]))
            os.popen('git pull')
            os.popen('chmod 777 cmd.sh')
            os.popen('./cmd.sh')
            os.popen('chmod 644 cmd.sh')
            conn.execute(db.UPDATE_JOB % (setting.STR_MSG_SUCCESS, exe_time, int(job[2])))

        conn.commit()
        cur.close()
        conn.close()
        return ''


class install:
    def GET(self):
        conn = sqlite3.connect(db.DB)
        conn.execute(db.CREATE_JOB_SQL)
        conn.execute(db.CREATE_QUEUE_SQL)
        conn.execute(db.CREATE_LOG_SQL)
        conn.close()
        return web.seeother('/')


class add:
    def GET(self):
        return render.add()

    def POST(self):
        data = web.input()
        addr = data.addr
        name = addr[addr.rfind('/') + 1:]
        dir = data.dir
        conn = sqlite3.connect(db.DB)
        conn.execute(db.INSERT_TO_JOB % (unicode(setting.STR_MSG_WAITIMG, "utf-8"), name, dir, addr))
        conn.commit()
        conn.close()

        return web.seeother('/')


class delete:
    def POST(self):
        data = web.input()
        job_id = data.id

        conn = sqlite3.connect(db.DB)
        conn.execute(db.DELETE_JOB % int(job_id))
        conn.commit()
        conn.close()

        return setting.STR_STATUS_SUCCESS


class execute:
    def POST(self):
        exe_time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        dic_ret = {'msg': setting.STR_MSG_FAIL, 'exe_time': exe_time}
        data = web.input()
        job_id = data.id

        conn = sqlite3.connect(db.DB)
        cur = conn.cursor()
        cur.execute(db.SELECT_DIR_FROM_JOB % int(job_id))
        jobs = cur.fetchall()
        if len(jobs):
            job = jobs[0]
            try:
                os.chdir('%s/%s' % (job[0], job[1]))
                os.popen('chmod 777 cmd.sh')
                os.popen('./cmd.sh')
                dic_ret['msg'] = setting.STR_MSG_SUCCESS
                conn.execute(db.UPDATE_JOB % (setting.STR_MSG_SUCCESS, exe_time, int(job_id)))
            except Exception:
                dic_ret['msg'] = setting.STR_MSG_FAIL
                conn.execute(db.UPDATE_JOB % (setting.STR_MSG_FAIL, exe_time, int(job_id)))

        conn.commit()
        cur.close()
        conn.close()

        return json.dumps(dic_ret)