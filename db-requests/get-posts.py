# coding=UTF-8

@dbRequestHandler('ABLOG-MAIN','GET-POSTS')
def request__get_posts(db,first=0,count=20,user_id=None,**kwargs):
	user_condition = ""
	if user_id != None:
		user_condition = """
		WHERE
			user_id = %s
		""" % (int(user_id))
	return db._make_request(
		"""
		SELECT
			user_name,
			post_ctime,post_mtime,user_id,post_content,post_id
		FROM
			{db_name}.ALLPOSTS
		{user_condition}
		ORDER BY
			post_id DESC
		LIMIT
			{first},{count}
		""",
		('user','ctime','mtime','uid','text','post_id'),
		first=first,
		count=count,
		user_condition=user_condition);

@dbRequestHandler('ABLOG-MAIN','GET-POSTS-COUNT')
def request__get_posts_count(db,user_id=None,**kwargs):
	user_condition = ""
	if user_id != None:
		user_condition = """
		WHERE
			post_user = %s
		""" % (int(user_id))
	reqres = db._make_request(
		"""
		SELECT
			COUNT(*)
		FROM
			{db_name}.POSTS
		{user_condition}
		""",
		user_condition=user_condition);
	return reqres[0][0]
