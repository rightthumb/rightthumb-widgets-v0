#!/bin/bash
ssh -L 59001:localhost:5901 -C -N -l scott tatooine.m-eta.app &
echo $! > $HOME/vps.t.dt.pid
