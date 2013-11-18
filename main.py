#coding=utf-8
import json
import os
import web
import sqlite3
from configs import db

__author__ = 'Administrator'

urls = (
    '/push', 'push',
    '/', 'index',
    '/install', 'install',
    '/new_job', 'new_job'
)

app = web.application(urls, globals())
render = web.template.render('templates')

if __name__ == '__main__':
    app.run()


class index:
    def GET(self):
        conn = sqlite3.connect(db.DB)
        cur = conn.cursor()
        cur.execute('select id, name, addr from tb_job;')
        jobs = []
        for job in cur:
            jobs.append(job)
        return render.index(jobs)


class push:
    def POST(self):
        data = web.input()
        data = json.loads(data.payload)
        url = data['repository']['url']
        sql = 'select name, dir from tb_job where addr = "%s"' % url
        conn = sqlite3.connect(db.DB)
        cur = conn.cursor()
        cur.execute(sql)
        os.popen('git pull %s.git %s/%s' % (url, cur[0], cur[1]))

        print url

        return render.push(data)


class install:
    def GET(self):
        conn = sqlite3.connect(db.DB)
        conn.execute(db.CREATE_JOB_SQL)
        conn.execute(db.CREATE_QUEUE_SQL)
        conn.execute(db.CREATE_LOG_SQL)
        conn.close()
        return web.seeother('/')


class new_job:
    def GET(self):
        return render.new_job()

    def POST(self):
        data = web.input()
        addr = data.addr
        cmd = data.cmd
        name = addr[addr.rfind('/') + 1: -4]
        dir = data.dir
        params = [(name, dir, cmd, addr)]
        conn = sqlite3.connect(db.DB)
        conn.executemany(db.INSERT_TO_JOB, params)
        conn.commit()
        conn.close()

        return web.seeother('/')