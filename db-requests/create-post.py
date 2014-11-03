#coding=UTF-8

@dbRequestHandler('ABLOG-MAIN','NEW-POST')
def request__authenticate_user(db,userid,posttext,**kwargs):
	posttext = posttext.replace('\"','\\\"')
	reqres = db._make_request(
		"""
		INSERT
		INTO {db_name}.POSTS
			(post_ctime,post_mtime,post_user,post_content)
		VALUES
			(CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,{user_id},"{text}");
		""",
		user_id=userid,
		text=posttext)