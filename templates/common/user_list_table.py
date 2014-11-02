# coding=UTF-8

def _template_user_list_table(count=10):
	top_users = makeDBRequest('RANDOM-20-USERS')
	n = 0
	yield """
	<div class='col-md-3 col-lg-2'>
		<div class="list-group">
			<div class="list-group-item">
				<a href='/users' class='list-group-item-heading'>Пользователи</p>
			</div>"""
	if top_users is None:
		yield """
		<div class="list-group-item">
			<p class='list-group-item-text' textcolor='red'>[Database request failed]</p>
		</div>"""
	else:
		for x in top_users:
			yield """<div class="list-group-item">
				<p class='list-group-item-text'><a href='/user?id="""
			yield x['id']
			yield "'>"
			yield x['name']
			yield "</a> <a href='/posts?user="
			yield x['id']
			yield "'><span class='badge'>"
			yield str(x['nposts'])
			yield '</span></a>'
			n = n + 1
			if n >= count:
				break
			
			yield '</p></div>'
	yield """
		</div>
	</div>"""
