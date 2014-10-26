# coding=UTF-8

@dbRequestHandler('ABLOG-MAIN','AUTHENTICATE-USER')
def request__authenticate_user(db,username,passwd,**kwargs):
	reqres = db._make_request(
		"""
		SELECT user_id
		FROM {db_name}.USERS
		WHERE
			user_name = "{login}"
		AND
			user_passwd ="{password}"
		""",
		login=username,
		password=passwd)
	if reqres == None:
		return None;
	if len(reqres) != 1:
		return None;
	return reqres[0][0]
