#!/bin/bash
sudo rndc flush
sudo rndc reload

sudo rm -rf /var/named/cache/*
sudo rm -rf /var/named/ns_parse_cache/*
sudo rm -rf /var/named/parse_cache/*

sudo systemctl restart named
