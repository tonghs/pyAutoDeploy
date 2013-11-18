#coding=utf-8
import json
import web
import os
__author__ = 'Administrator'

urls = (
    '/push', 'push',
    '/', 'index'
)

app = web.application(urls, globals())
render = web.template.render('templates')

if __name__ == '__main__':
    app.run()


class index:
    def GET(self):
        return render.index()


class push:
    def POST(self):
        data = json.loads(web.input())
        print "New commit by: {}".format(data['commits'][0]['author']['name'])

        return render.push(data)
