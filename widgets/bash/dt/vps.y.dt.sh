#!/bin/bash
ssh -L 59001:localhost:5901 -C -N -l scott yavin.m-eta.app &
echo $! > $HOME/vps.y.dt.pid
