 pip install -r requirement.txt 
pip freeze > requirements.txt
 
docker build -t my-flask-app .

docker run -p 5000:5000 my-flask-app