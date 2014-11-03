#!/usr/bin/python
# coding=UTF-8

def _template_NAVBAR():
	yield """
		<style>body { padding-top: 70px; }</style>
		<div class="navbar navbar-default navbar-fixed-top" role="navigation">
			<div class="container">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a class="navbar-brand" href="/">ABlog</a>
				</div>
				<div class="navbar-collapse collapse">
					<ul class="nav navbar-nav">
						<li><a href='/home'>Домой</a></li>
						<li><a href='/posts?start=0&amp;count=10'>Записи</a></li>
						<li><a href='/users?start=0&amp;count=10'>Пользователи</a></li>
						<li><a href='/about'>О сайте</a></li>
					</ul>
				</div>
			</div>
		</div>"""