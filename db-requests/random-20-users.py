# coding=UTF-8

@dbRequestHandler('ABLOG-MAIN','RANDOM-20-USERS')
@storeResult(seconds=5)
def request__random_20_users(db,**kwargs):
	reqres = db._make_request(
		"""
		SELECT
			user_id, user_name, user_email,
			CEIL(RAND()*10000000) AS rand_num
		FROM {db_name}.USERS
		ORDER BY rand_num
		LIMIT 0,20;
		""",
		('id','name','email') )
	if reqres == None:
		return None
	for user in reqres:
		user['nposts'] = makeDBRequest('GET-POSTS-COUNT',user_id=user['id'])
	return reqres
