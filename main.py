#coding=utf-8
from datetime import datetime
import json
import os
import web
import sqlite3
from configs import db
from configs import setting
import util

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
render = web.template.render(setting.CUR_DIR % 'templates/', base='base')

application = app.wsgifunc()

if __name__ == '__main__':
    app.run()


class faviconICO(object):
    def GET(self):
        return web.seeother('/static/images/favicon.ico')


class index:
    def GET(self):
        conn = sqlite3.connect(db.DB)
        cur = conn.cursor()
        cur.execute(db.SELECT_JOB)
        jobs = []
        for job in cur:
            state = job[0]
            state_text = setting.STATUS[int(job[0])]
            name = job[1]
            url = job[2]
            exe_time = job[3]
            id = job[4]
            dic_job = {'state': state, 'state_text': state_text, 'name': name, 'url': url, 'exe_time': exe_time, 'id': id }
            jobs.append(dic_job)
        return render.index(jobs)


class push:
    def POST(self):
        exe_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = web.input()
        data = json.loads(data.payload)
        url = data['repository']['url']
        util.execute('url', url, exe_time)
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
        url = data.url
        name = url[url.rfind('/') + 1:]
        dir = data.dir
        conn = sqlite3.connect(db.DB)
        conn.execute(db.INSERT_TO_JOB % (setting.STATE_WAITING, name, dir, url))
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
        exe_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dic_ret = {'state': setting.STATE_FAIL, 'msg': setting.STATUS[int(setting.STATE_FAIL)], 'exe_time': exe_time}
        data = web.input()
        job_id = data.id

        state = util.execute('id', job_id, exe_time)
        dic_ret['msg'] = setting.STATUS[int(state)]
        dic_ret['state'] = state

        return json.dumps(dic_ret)