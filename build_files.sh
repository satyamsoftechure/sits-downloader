echo "Build start"
python3.12 -m pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "Build end"