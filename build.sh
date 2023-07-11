set -o errexit
pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations && python manage.py migrate
python manage.py loaddata ./products/fixtures/brands.json
python manage.py loaddata ./products/fixtures/categories.json
python manage.py loaddata ./products/fixtures/shoes.json
# python manage.py loaddata ./reviews/fixtures/reviews.json