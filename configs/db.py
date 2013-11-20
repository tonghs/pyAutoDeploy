#coding=utf-8
from configs import setting

__author__ = '华帅'

DB = setting.CUR_DIR % 'db'

CREATE_JOB_SQL = 'create table tb_job (id integer primary key autoincrement, name varchar(100), dir varchar(100), ' \
                 'addr varchar(500), exe_time datetime, status varchar(10));'
CREATE_LOG_SQL = 'create table tb_log (id integer primary key autoincrement, ' \
                 'job_id integer, exe_time varchar(19), content text);'
CREATE_QUEUE_SQL = 'create table tb_queue (id integer primary key autoincrement, job_id integer, att_cmd text);'

INSERT_TO_JOB = 'insert into tb_job (status, name, dir, addr) values ("%s", "%s", "%s", "%s");'
DELETE_JOB = 'delete from tb_job where id = %d;'
SELECT_DIR_FROM_JOB = 'select dir, name from tb_job where id = %d;'

UPDATE_JOB = 'update tb_job set status = "%s", exe_time = "%s" where id = %d'