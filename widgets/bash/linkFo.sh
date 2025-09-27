#!/bin/bash

printer=true

src=$(realpath "$1")
dst=$(realpath "$2")
user=$3

if [ -z "$src" ] || [ -z "$dst" ]; then
  echo "Usage: ./linkFoV2 src dst [user]"
  exit 1
fi

if [ "$printer" = true ]; then
  echo "Source directory: $src"
  echo "Destination directory: $dst"
fi

if [ -d "$src" ]; then
  if [ ! -z "$user" ]; then
    if [ "$printer" = true ]; then
      echo "Changing ownership to: $user"
    fi
    sudo chown "$user":"$user" "$src"
    chmod 755 "$src"
  fi

  if [ "$printer" = true ]; then
    echo "Creating symlink"
  fi
  ln -s "$src" "$dst"

  if [ "$printer" = true ]; then
    echo "Symlink created at: $dst"
  fi

  if [ -L "$dst" ]; then
    if [ "$printer" = true ]; then
      echo "Symlink exists and points to: $(readlink -f $dst)"
    fi
  else
    echo "Error: Symlink was not created"
  fi
else
  echo "Source directory does not exist: $src"
  exit 1
fi
