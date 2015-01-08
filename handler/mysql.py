#coding=utf-8
import sae.const
import MySQLdb
#获取数据库连接
def get_conn():
  conn=MySQLdb.connect(
    host=sae.const.MYSQL_HOST,
    user=sae.const.MYSQL_USER,
    passwd=sae.const.MYSQL_PASS,
    db=sae.const.MYSQL_DB,
    port=int(sae.const.MYSQL_PORT),
    charset='utf8')
  return conn
#执行SQL查询，结果以list(dict...)的形式返回
def query_for_list(query,*param):
  try:
    conn=get_conn()
    try:
      cur=conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
      cur.execute(query, param)
      result = cur.fetchall()
      return result
    finally:
      cur.close()
      conn.close()
  except MySQLdb.Error as e:
    return "Mysql Error Occured! %s" % (e)
    return None
#获取单行型查询结果
def query_for_one(query,*param):
  try:
    conn=get_conn()
    try:
      cur=conn.cursor()
      cur.execute(query, param)
      result = cur.fetchone()
      return result
    finally:
      cur.close()
      conn.close()
  except MySQLdb.Error as e:
    return "Mysql Error Occured! %s" % (e)
    return None
#执行批量查询
def execute_many(query,param_list):
  conn=get_conn()
  try:
    cur=conn.cursor()
    res = cur.executemany(query, param_list)
    conn.commit()
    return res
  except Exception as e:
    conn.rollback()
    raise e
  finally:
    cur.close()
    conn.close()
  return -1
#执行SQL更新操作（如update,insert,delete等）
def execute_sql(query,*param):
  conn=get_conn()
  try:
    cur=conn.cursor()
    cnt = cur.execute(query, param)
    conn.commit()
    return cnt
  except Exception as e:
    conn.rollback()
    raise e
  finally:
    cur.close()
    conn.close()
#执行insert，同时返回新增数据的ID，适合使用auto_increment字段的数据表
def execute_insert_get_id(query,*param):
  try:
    conn=get_conn()
    try:
      cur=conn.cursor()
      cur.execute(query, param)
      insert_id = conn.insert_id()
      conn.commit()
      return insert_id;
    except Exception as e:
      conn.rollback()
      raise e
    finally:
      cur.close()
      conn.close()
  except MySQLdb.Error as e:
    return "Mysql Error Occured! %s" % (e)
    return -1
#以dict的形式执行数据插入操作,table_name为表名，dict为{字段:值}字典
def insert_by_dict(table_name,dict):
  keys = ''
  values = list()
  perc_sign = ''
  cnt = 0
  for key in dict:
    if cnt > 0:
      perc_sign += ','
      keys += ','
    cnt += 1
    perc_sign += '%s'
    keys += key
    values.append(dict[key])
  sql = 'insert into ' + table_name + '(' + keys + ') values(' + perc_sign + ')'
  return execute_sql(sql,*values)
