sudo service ssh stop
echo "AllowGroups sudo" >> /etc/ssh/sshd_config
echo "AllowUsers sshuser" >> /etc/ssh/sshd_config
sudo service ssh start
