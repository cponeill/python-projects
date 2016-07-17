#This file is a bash script related to the 21.co docker jail

echo $1:$2 | chpasswd &>/dev/null
docker-mkjail $1 &>/dev/null
sleep 3600
killall --user $1 &>/dev/null
docker-rmjail $1 &>/dev/null
deluser --remove-home $1 &>/dev/null
