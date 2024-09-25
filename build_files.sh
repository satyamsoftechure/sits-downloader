echo "Build start"
python3.12 -m pip install -r requirements.txt
echo "Build end"
echo "Build start"
python3.12 manage.py collectstatic --noinput --clear
echo "Build end"