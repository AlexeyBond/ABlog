# coding=UTF-8

@dbRequestHandler('ABLOG-MAIN','GET-POSTS')
def request__get_posts(db,first=0,count=20,**kwargs):
	return db._make_request(
		"""
		SELECT
			user_name,
			post_ctime,post_mtime,post_user,post_content
		FROM
			{db_name}.USERS, {db_name}.POSTS
		WHERE
			post_user = user_id
		ORDER BY
			post_id DESC
		LIMIT
			{first},{count}
		""",
		('user','ctime','mtime','uid','text'),
		first=first, count=count);
