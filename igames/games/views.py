from django.http import HttpResponse
import datetime
import json
import time

from igames.settings import mysql_dbs

PAGE_NUM = 5 

def info(request):
	gid = request.GET.get('gid', 1)
	response = {}

	connection = mysql_dbs['game']
	with connection.cursor() as cursor:
		sql = """SELECT * FROM game_save where `id`=%s"""
		cursor.execute(sql, (gid, ))
		
		result = cursor.fetchone()
	
	if result is None:
		response['game'] = {}
		response['status'] = 1
	else:
		temp = result.get('save_time', datetime.datetime.now())
		result['save_time'] = time.mktime(temp.timetuple())

		response['game'] = result
		response['status'] = 0

	return HttpResponse(json.dumps(response), content_type="application/json")


def search(request):
	key = request.GET.get('key', '')
	last_id = int(request.GET.get('last_id', '0'))

	connection = mysql_dbs['game']
	with connection.cursor() as cursor:
		sql = """SELECT * FROM game_save where id>%s and name like %s ORDER BY id ASC LIMIT %s"""
		cursor.execute(sql, (last_id, '%' + key + '%', PAGE_NUM))
		
		result = cursor.fetchall()

	for item in result:
		temp = item.get('save_time', datetime.datetime.now())
		item['save_time'] = time.mktime(temp.timetuple())

	response = {
			'status': 0,
			'games': result}

	return HttpResponse(json.dumps(response), content_type="application/json")


def rank(request):
	response = {}
	page = int(request.GET.get('page', 0))
	begin = page * PAGE_NUM
	end = begin + PAGE_NUM

	connection = mysql_dbs['game']
	with connection.cursor() as cursor:
		sql = """SELECT * FROM game_save where id>%s and id<=%s ORDER BY id ASC"""
		cursor.execute(sql, (begin, end))
		
		result = cursor.fetchall()

	for item in result:
		temp = item.get('save_time', datetime.datetime.now())
		item['save_time'] = time.mktime(temp.timetuple())

	response = {
			'status': 0,
			'games': result}

	return HttpResponse(json.dumps(response), content_type="application/json")
