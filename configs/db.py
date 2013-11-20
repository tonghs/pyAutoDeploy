#coding=utf-8
__author__ = '华帅'

DB = 'db'

CREATE_JOB_SQL = 'create table tb_job (id integer primary key autoincrement,' \
                 ' name varchar(100), dir varchar(100), addr varchar(500), exe_time datetime);'
CREATE_LOG_SQL = 'create table tb_log (id integer primary key autoincrement, ' \
                 'job_id integer, exe_time varchar(19), content text);'
CREATE_QUEUE_SQL = 'create table tb_queue (id integer primary key autoincrement, job_id integer, att_cmd text);'

INSERT_TO_JOB = 'insert into tb_job (name, dir, addr) values (?, ?, ?);'