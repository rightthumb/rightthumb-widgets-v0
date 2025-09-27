#!/usr/bin/env bash

export USER=$USER
export HOME=$HOME

vncserver -name remote-desktop -localhost no :1
