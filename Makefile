
collectstatic:
	@docker-compose run --no-deps web python manage.py collectstatic --noinput


ssl_cert:
	@
