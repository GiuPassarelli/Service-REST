#!/bin/bash
echo "start'"
sudo apt update -y;
echo 111
sudo apt install python3-pip -y;
pip3 install Flask;
echo 222
pip3 install flask_restful;
echo 123
tmux new -d -s server_tmux 'python3 webserver.py;';
