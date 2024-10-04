echo "Build start"
python3.12 -m pip install -r requirements.txt
echo "Build end"
echo "Build start"
python3.12 manage.py collectstatic --noinput --clear
echo "Build end"
echo "Downloading FFmpeg..."
mkdir -p bin
curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz | tar -xJ --strip-components=1 -C ./bin
chmod +x ./bin/ffmpeg
echo "FFmpeg installed successfully."
