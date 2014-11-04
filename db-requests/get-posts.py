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

@dbRequestHandler('ABLOG-MAIN','GET-POST')
def request__get_post(db,post_id,**kwargs):
	reqres = db._make_request(
		"""
		SELECT
			user_name,
			post_ctime,post_mtime,user_id,post_content,post_id
		FROM
			{db_name}.ALLPOSTS
		WHERE
			post_id={post_id}
		""",
		('user','ctime','mtime','uid','text','post_id'),
		post_id = post_id);
	if reqres == None:
		return None;
	if len(reqres) != 1:
		return None;
	return reqres[0]

@dbRequestHandler('ABLOG-MAIN','MODIFY-POST')
def request__modify_post(db,post_id,new_text,**kwargs):
	new_text = new_text.replace('\\','\\\\').replace('\"','\\\"')
	return db._make_request(
		"""
		UPDATE
			{db_name}.POSTS
				SET 
					post_content="{new_text}",
					post_mtime=CURRENT_TIMESTAMP
			WHERE
				post_id={post_id};
		""",
		new_text=new_text,
		post_id=post_id);

@dbRequestHandler('ABLOG-MAIN','DELETE-POST')
def request__delete_post(db,post_id,**kwargs):
	return db._make_request(
		"""
		DELETE FROM
			{db_name}.POSTS
		WHERE
			post_id={post_id}
		""",
		post_id=post_id);
