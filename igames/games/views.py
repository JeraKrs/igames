from django.http import HttpResponse
import datetime
import json
import time

import pymysql.cursors


PAGE_NUM = 20


def info(request):
	gid = request.GET.get('gid', 1)
	response = {}

	connection = pymysql.connect(
			host='10.0.0.5', port=3306, user='root', password='Keshuai123', db='igame',
			charset='utf8', cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cursor:
			sql = """SELECT * FROM game_save_test where `id`=%s"""
			cursor.execute(sql, (gid, ))
		
			result = cursor.fetchone()
	except Exception as e:
		result = None
	finally:
		connection.close()

	print result
	
	if result is None:
		response['game'] = {}
		response['status'] = 1
	else:
		temp = result.get('save_time', datetime.datetime.now())
		result['save_time'] = time.mktime(temp.timetuple())

		response['game'] = result
		response['status'] = 0

	res = HttpResponse(json.dumps(response), content_type="application/json")

	res["Access-Control-Allow-Origin"] = "*"
	res["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
	res["Access-Control-Max-Age"] = "1000"
	res["Access-Control-Allow-Headers"] = "*"
	return res


def search(request):
	key = request.GET.get('key', '')
	last_id = int(request.GET.get('last_id', '0'))

	connection = pymysql.connect(
			host='10.0.0.5', port=3306, user='root', password='Keshuai123', db='igame',
			charset='utf8', cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cursor:
			sql = """SELECT * FROM game_save_test where id>%s and name like %s ORDER BY id ASC LIMIT %s"""
			cursor.execute(sql, (last_id, '%' + key + '%', PAGE_NUM))
		
			result = cursor.fetchall()
	except Exception as e:
		result = []
	finally:
		connection.close()

	for item in result:
		temp = item.get('save_time', datetime.datetime.now())
		item['save_time'] = time.mktime(temp.timetuple())

	response = {
			'status': 0,
			'games': result}

	res = HttpResponse(json.dumps(response), content_type="application/json")

	res["Access-Control-Allow-Origin"] = "*"
	res["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
	res["Access-Control-Max-Age"] = "1000"
	res["Access-Control-Allow-Headers"] = "*"
	return res


def rank(request):
	response = {}
	page = int(request.GET.get('page', 0))
	begin = page * PAGE_NUM
	end = begin + PAGE_NUM

	connection = pymysql.connect(
			host='10.0.0.5', port=3306, user='root', password='Keshuai123', db='igame',
			charset='utf8', cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cursor:
			sql = """SELECT * FROM game_save_test where id>%s and id<=%s ORDER BY id ASC"""
			cursor.execute(sql, (begin, end))
		
			result = cursor.fetchall()
	except Exception as e:
		result = []
	finally:
		connection.close()

	for item in result:
		temp = item.get('save_time', datetime.datetime.now())
		item['save_time'] = time.mktime(temp.timetuple())

	response = {
			'status': 0,
			'games': result}

	res = HttpResponse(json.dumps(response), content_type="application/json")

	res["Access-Control-Allow-Origin"] = "*"
	res["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
	res["Access-Control-Max-Age"] = "1000"
	res["Access-Control-Allow-Headers"] = "*"
	return res
