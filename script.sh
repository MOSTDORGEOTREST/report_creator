docker system prune -a -f
docker rm $(docker ps -a -q) -f
docker rmi $(docker images -a -q) -f
git pull
sudo service docker restart
docker-compose up