.PHONY: run
run: 
	python3 manage.py runserver
.PHONY: create_products
create_products:
	python3 manage.py create_products $(count)
.PHONY: db/migrations/migrate
db/migrations/migrate:
	python3 manage.py migrate

.PHONY: db/migrations/make
db/migrations/make:
	python3 manage.py makemigrations

.PHONY: db/run
db/run:
	docker run --rm --name vishitiy_db -v vishitiy_data:/var/lib/postgresql/data -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres:15-alpine  