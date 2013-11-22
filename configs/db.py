#coding=utf-8
from configs import setting

__author__ = '华帅'

DB = setting.CUR_DIR % 'db'

# 初始化
CREATE_JOB_SQL = 'create table tb_job (id integer primary key autoincrement, name varchar(100), dir varchar(100), ' \
                 'url varchar(500), exe_time datetime, state varchar(10));'
CREATE_LOG_SQL = 'create table tb_log (id integer primary key autoincrement, ' \
                 'job_id integer, exe_time datetime, state varchar(10), content text);'
CREATE_QUEUE_SQL = 'create table tb_queue (id integer primary key autoincrement, job_id integer, job_name varchar(100));'

# 任务相关
SELECT_JOB = 'SELECT state, name, url, exe_time, id FROM tb_job;'
SELECT_DIR_FROM_JOB_BY_ID = 'select dir, name, id from tb_job where id = %d;'
SELECT_DIR_FROM_JOB_BY_URL = 'select dir, name, id from tb_job where url = "%s";'

INSERT_TO_JOB = 'insert into tb_job (state, name, dir, url) values ("%s", "%s", "%s", "%s");'

UPDATE_JOB = 'update tb_job set state = "%s", exe_time = "%s" where id = %d;'

DELETE_JOB = 'delete from tb_job where id = %d;'

# 日志相关
SELECT_LOG = 'select id, exe_time, state from tb_log where job_id = %d order by id desc limit 100;'
SELECT_TOP10_LOG = 'select tb_job.name, tb_log.exe_time, tb_log.id from tb_log left join tb_job on tb_job.id =' \
                   ' tb_log.job_id order by tb_log.id desc limit 10;'
SELECT_LOG_CONTENT_BY_ID = 'select content from tb_log where id = %d;'

INSERT_TO_LOG = 'insert into tb_log (job_id, exe_time, state, content) values (%d, "%s", %d, "%s");'

DELETE_LOG = 'delete from tb_log where job_id = %d;'

