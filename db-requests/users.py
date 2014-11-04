# coding=UTF-8


@dbRequestHandler('ABLOG-MAIN','GET-USER-INFO')
def request__get_user_info(db,userid,**kwargs):
	reqres = db._make_request(
		"""
		SELECT
			user_id,user_name,
			user_passwd,user_email,
			user_reg_time,user_avatar_path,
			user_about_text
		FROM
			{db_name}.USERS
		WHERE
			user_id = {user_id}
		""",
		('id','name','passwd','email','reg_time','avapath','about'),
		user_id=str(userid) )
	if reqres == None:
		return None
	if len(reqres) != 1:
		return None
	return reqres[0]

@dbRequestHandler('ABLOG-MAIN','GET-USERS')
def request__get_users(db,first,count,**kwargs):
	reqres = db._make_request(
		"""
		SELECT
			user_id,user_name
		FROM
			{db_name}.USERS
		ORDER
			BY user_id
		LIMIT {first},{count}
		""",
		('id','name'),
		first=first,
		count=count );
	return reqres

@dbRequestHandler('ABLOG-MAIN','GET-USERS-COUNT')
def request__get_users_count(db,**kwargs):
	reqres = db._make_request(
		"""
		SELECT
			COUNT(*)
		FROM
			{db_name}.USERS;
		""");
	if reqres == None:
		return None
	return reqres[0][0]

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

@dbRequestHandler('ABLOG-MAIN','SET-USER-AVATAR-PATH')
def request__set_user_avatar_path(db,userid,path,**kwargs):
	db._make_request(
		"""
		UPDATE
			{db_name}.USERS
				SET user_avatar_path="{path}"
			WHERE
				user_id={userid};
		""",
		userid=userid,
		path=path)

@dbRequestHandler('ABLOG-MAIN','SET-USER-DATA')
def request__set_user_avatar_path(db,userid,email,about,**kwargs):
	if about == None:
		about = 'NULL'
	else:
		about = '\"' + about.replace('\\','\\\\').replace('\"','\\\"') + '\"'
	#
	if email == None or email == '':
		email = 'NULL'
	else:
		email = '\"' + email.replace('\\','\\\\').replace('\"','\\\"') + '\"'
	#
	db._make_request(
		"""
		UPDATE
			ABLOG_DB.USERS
				SET
					user_email={email},
					user_about_text={about}
			WHERE
				user_id={userid};
		""",
		userid=userid,
		about=about,
		email=email)
