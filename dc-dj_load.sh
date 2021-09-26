# https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata
# https://stackoverflow.com/questions/58235385/django-loaddata-command-from-docker-container
cat db.json |docker-compose exec -T web python manage.py loaddata --format=json -