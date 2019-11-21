#!/bin/bash
sudo apt update -y;
sudo apt install python3-pip -y;
pip3 install Flask;
pip3 install flask_restful;
tmux new -d -s server_tmux 'python3 webserver.py;';
