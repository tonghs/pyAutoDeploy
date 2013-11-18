#coding=utf-8
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
        data = web.input()
        print data.payload

        return render.push(data)
