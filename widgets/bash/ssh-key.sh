#!/bin/bash

rm -rf ~/.ssh
ssh-keygen -t rsa

ssh-copy-id -i ~/.ssh/id_rsa.pub scott@hoth.eyeformeta.com
ssh-copy-id -i ~/.ssh/id_rsa.pub scott@bespin.eyeformeta.com
ssh-copy-id -i ~/.ssh/id_rsa.pub scott@mandalore.eyeformeta.com

ssh-copy-id -i ~/.ssh/id_rsa.pub root@hoth.eyeformeta.com
ssh-copy-id -i ~/.ssh/id_rsa.pub root@bespin.eyeformeta.com
ssh-copy-id -i ~/.ssh/id_rsa.pub root@mandalore.eyeformeta.com

