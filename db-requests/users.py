# coding=UTF-8


@dbRequestHandler('ABLOG-MAIN','GET-USER-INFO')
def request__get_user_info(db,userid,**kwargs):
	reqres = db._make_request(
		"""
		SELECT
			user_id,user_name,
			user_passwd,user_email
		FROM
			{db_name}.USERS
		WHERE
			user_id = {user_id}
		""",
		('id','name','passwd','email'),
		user_id=str(userid) )
	if reqres == None:
		return None
	if len(reqres) != 1:
		return None
	return reqres[0]

@dbRequestHandler('ABLOG-MAIN','GET-USER-NAME')
def request__get_user_info(db,userid,**kwargs):
	reqres = db._make_request(
		"""
		SELECT
			user_name
		FROM
			{db_name}.USERS
		WHERE
			user_id = {user_id}
		""",
		user_id=str(userid) )
	if reqres == None:
		return None
	if len(reqres) != 1:
		return None
	return reqres[0][0]
