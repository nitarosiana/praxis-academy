import pymysql
from app import app
	from db_config import mysql
	from flask import jsonify
	from flask import flash, request
	
	# create 			
	@app.route('/create', methods=['POST'])
	def create_user():
		try:
			_json = request.json
			_profil_setting = _json['profil_setting']
			_news = _json['news']
			_memo = _json['memo']
			_outgoing = _json['outgoing']
			_expression = _json['expression']
			_event_calendar = _json['event_calendar']

 
			
				# insert
				sqlQuery = "INSERT INTO user(profil_setting, news, memo, outgoing, expression, event_calendar) VALUES(%s, %s, %s, %s, %s, %s, %s)"
				data = (_profil_setting, _news, _memo, _outgoing, _expression, _event_calendar,)
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute(sqlQuery, data)
				conn.commit()
				res = jsonify('User creating successfully.')
				res.status_code = 200
 
				return res
			else:
				return not_found()
		except Exception as e:
			print(e)
		finally:
			cursor.close() 
			conn.close()
			
	@app.route('/user')
	def user():
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute("SELECT * FROM user")
			rows = cursor.fetchall()
			res = jsonify(rows)
			res.status_code = 200
 
			return res
		except Exception as e:
			print(e)
		finally:
			cursor.close() 
			conn.close()
			
	@app.route('/user/<int:user_id>')
	def user(user_id):
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute("SELECT * FROM user WHERE id=%s", user_id)
			row = cursor.fetchone()
			res = jsonify(row)
			res.status_code = 200
 
			return res
		except Exception as e:
			print(e)
		finally:
			cursor.close() 
			conn.close()
 
	@app.route('/update', methods=['PUT'])
	def update_user():
		try:
			_json = request.json
			_user_id = _json['id']
			_profil_setting = _json['profil_setting']
			_news = _json['news']
			_memo = _json['memo']
			_outgoing = _json['outgoing']
			_expression = _json['expression']
			_event_calendar = _json['event_calendar']
 
			
				
				# update
				sql = "UPDATE user SET profil_setting=%s, news=%s, memo=%s, outgoing=%s, expression=%s, event_calendar=%s WHERE id=%s"
				data = (_profil_setting, _news, _memo, _outgoing, _expression, _event_calendar)
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute(sql, data)
				conn.commit()
				res = jsonify('User updating successfully.')
				res.status_code = 200
 
				return res
			else:
				return not_found()
		except Exception as e:
			print(e)
		finally:
			cursor.close() 
			conn.close()
 
	# delete	
	@app.route('/delete/<int:user_id>, methods=['DELETE']')
	def delete_user(user_id):
		try:
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute("DELETE FROM user WHERE id=%s", (user_id,))
			conn.commit()
			res = jsonify('User deleted successfully.')
			res.status_code = 200
			return res
 
		except Exception as e:
			print(e)
		finally:
			cursor.close() 
			conn.close()
			
	@app.errorhandler(404)
	def not_found(error=None):
	    message = {
	        'status': 404,
	        'message': 'There is no record: ' + request.url,
	    }
	    res = jsonify(message)
	    res.status_code = 404
 
	    return res
			
	if __name__ == "__main__":
	    app.run()	