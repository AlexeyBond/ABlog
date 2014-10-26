# coding=UTF-8

@dbRequestHandler('ABLOG-MAIN','RANDOM-20-USERS')
@storeResult(seconds=5)
def request__top_20_users(db,**kwargs):
	return db._make_request(
		"""
		SELECT
			user_id, user_name, user_email,
			CEIL(RAND()*10000000) AS rand_num
		FROM {db_name}.USERS
		ORDER BY rand_num
		LIMIT 0,20;
		""",
		('id','name','email') )
