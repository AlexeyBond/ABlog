# coding=UTF-8

def _template_user_list_table(count=10):
	top_users = makeDBRequest('RANDOM-20-USERS')
	yield """
	<div class='col-md-3 col-lg-2'>
		<div class="list-group">
			<div class="list-group-item">
				<h3 class='list-group-item-heading'>Users</h3>
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
			yield '</a>'
			if x['email'] != None:
				yield '(<a href="mailto:'
				yield x['email']
				yield '">email</a>)'
			yield '</p></div>'
	yield """
		</div>
	</div>"""
