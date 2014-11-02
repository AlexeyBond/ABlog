# coding=UTF-8

@dbRequestHandler('ABLOG-MAIN','START-NEW-SESSION')
def request__start_new_session(db,user,cookie,**kwargs):
	reqres = db._make_request(
		"""
		INSERT INTO
			{db_name}.SESSIONS
			(session_cookie,session_user_id,session_start_time)
		VALUES
			("{cookie}",{user},CURRENT_TIMESTAMP);
		""",
		cookie=cookie,
		user=user
		);


@dbRequestHandler('ABLOG-MAIN','END-SESSION')
def request__end_session(db,cookie,**kwargs):
	reqres = db._make_request(
		"""
		DELETE FROM
			{db_name}.SESSIONS
		WHERE
			session_cookie="{cookie}";
		""",
		cookie=cookie
		);

@dbRequestHandler('ABLOG-MAIN','IDENTIFY-USER-BY-COOKIES')
def request__identify_user_by_cookie(db,cookies,**kwargs):
	if 'sessionid' not in cookies:
		return None
	cookie = cookies['sessionid']
	reqres = db._make_request(
		"""
		SELECT
			session_user_id,session_start_time,
			user_name
		FROM
			{db_name}.SESSIONS,
			{db_name}.USERS
		WHERE
			session_cookie = "{cookie}"
		AND
			user_id = session_user_id;
		""",
		('user_id','start_time','user_name'),
		cookie=cookie
		)
	if reqres == None:
		return None
	if len(reqres) != 1:
		return None
	return reqres[0]
