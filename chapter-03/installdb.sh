sudo apt-get install gnupg


# Now import the key using the command below.


wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -


# Create the sources list file as per your Linux distribution. We have added the
# list of sources as per Debian.


echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list


# Run update command


sudo apt-get update


# Now install Mongodb, using the below command.


sudo apt-get install -y mongodb-org


# Once the installation is successful, start MongoDB using the below command.


sudo systemctl start mongod


