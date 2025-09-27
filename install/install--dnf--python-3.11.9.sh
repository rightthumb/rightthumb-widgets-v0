#!/bin/bash

set -e  # Exit on error

echo "🔧 Installing dependencies..."
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel wget make xz-devel

echo "📥 Downloading Python 3.11.9 source..."
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz
sudo tar xzf Python-3.11.9.tgz
cd Python-3.11.9

echo "⚙️ Configuring and building..."
sudo ./configure --enable-optimizations
sudo make -j"$(nproc)"

echo "🚀 Installing Python 3.11.9..."
sudo make altinstall

echo "🔧 Installing pip3.11..."
python3.11 -m ensurepip --upgrade

echo "✅ Done! Checking version..."
python3.11 --version



alias python3='python3.11'

if [ ! -f "filename" ]; then
	echo "#!/bin/bash" > /.bashrc.
fi
echo "alias python3='python3.11'" >> $HOME/.bashrc.
echo "alias pip3='pip3.11'" >> $HOME/.bashrc.

alias python3='python3.11'
alias pip3='pip3.11'
