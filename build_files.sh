echo "Build start"
python3.12 -m pip install -r requirements.txt
echo "Build medium"
python3.12 manage.py collectstatic --noinput
echo "Build end"
