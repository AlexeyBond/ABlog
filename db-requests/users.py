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

@dbRequestHandler('ABLOG-MAIN','GET-USER-ID-BY-NAME')
def request__get_user_info(db,name,**kwargs):
	reqres = db._make_request(
		"""
		SELECT
			user_id
		FROM
			{db_name}.USERS
		WHERE
			user_name = "{name}";
		""",
		name=name)
	if reqres == None:
		return None
	if len(reqres) != 1:
		return None
	return reqres[0][0]

@dbRequestHandler('ABLOG-MAIN','NEW-USER')
def request__get_user_info(db,name,passwd,**kwargs):
	db._make_request(
		"""
		INSERT INTO
			{db_name}.USERS
			(user_name,user_passwd,user_reg_time)
		VALUES
			("{name}","{passwd}",CURRENT_TIMESTAMP);
		""",
		name=name,
		passwd=passwd)
