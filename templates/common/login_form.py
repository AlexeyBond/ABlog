#!/usr/bin/python
# coding=UTF-8

def _template_LOGIN_FORM():
	return """
	<form name='login_form' action='/login' method='POST'>
		<div class="form-group">
			<div class="input-group">
				<input class="form-control" placeholder='Username' type='text' name='login' />
			</div>
		</div>
		<div class="form-group">
			<div class="input-group">
				<input class="form-control" type='password' placeholder='Password' name='password' />
			</div>
		</div>
		<div class="form-group">
			<div class="input-group">
				<input type='submit' class='btn btn-xs btn-primary' value='Sign in!' />
				<span width='10px' />
				<a href='/register' class='btn btn-xs btn-default'>Register...</a>
			</div>
		</div>
	</form>"""
