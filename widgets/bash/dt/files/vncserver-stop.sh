#!/usr/bin/env bash

export USER=$USER
export HOME=$HOME

vncserver -kill :1
rm -rf $HOME/.vnc/localhost:1.pid
rm -rf /tmp/.X1-lock
rm -rf /tmp/.X11-unix/X1
