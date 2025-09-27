#!/bin/bash
echo "update"; sudo apt update -y; echo "upgrade"; sudo apt upgrade -y;
# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

#Get the necessary components
sudo apt-mark hold udisks2
[ ! -f /root/.parrot ] && sudo apt update || echo "Parrot detected, not updating apt cache since that will break the whole distro"
sudo apt install keyboard-configuration -y
sudo apt install sudo sudo wget -y
sudo apt install sudo sudo curl -y
sudo apt install xfce4 xfce4-terminal tigervnc-standalone-server -y
sudo apt install xfe -y
sudo apt clean
#Setup the necessary files
mkdir ~/.vnc
sudo curl -s  https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/widgets/bash/dt/files/xstartup.sh -o ~/.vnc/xstartup
sudo curl -s  https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/widgets/bash/dt/files/vncserver-start.sh -o /usr/local/bin/vncserver-start
sudo curl -s  https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/widgets/bash/dt/files/vncserver-stop.sh -o /usr/local/bin/vncserver-stop
sudo chmod +x ~/.vnc/xstartup
sudo chmod +x /usr/local/bin/vncserver-start
sudo chmod +x /usr/local/bin/vncserver-stop
echo " "
echo "Running browser patch"
sudo wget https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/widgets/bash/dt/files/ubchromiumfix.sh && sudo chmod +x ubchromiumfix.sh
sudo ./ubchromiumfix.sh && rm -rf ubchromiumfix.sh
echo "You can now start vncserver by running vncserver-start"
echo " "
echo "It will ask you to enter a password when first time starting it."
echo " "
echo "The VNC Server will be started at 127.0.0.1:5901"
echo " "
echo "You can connect to this address with a VNC Viewer you prefer"
echo " "
echo "Connect to this address will open a window with Xfce4 Desktop Environment"
echo " "
echo " "
echo " "
echo "Running vncserver-start"
echo " "
echo " "
echo " "
echo "To Kill VNC Server just run vncserver-stop"
echo " "
echo " "
echo " "
sudo echo 'export DISPLAY=":1"' | sudo tee -a /etc/profile

cat > ~/.Xresources << 'EOF'
! Fonts
Xft.dpi: 96
Xft.antialias: true
Xft.hinting: true
Xft.hintstyle: hintslight
Xft.rgba: rgb

! Cursor
Xcursor.theme: Adwaita
Xcursor.size: 24

! URxvt terminal settings (if you use it)
URxvt*scrollBar: false
URxvt*font: xft:Monospace:size=10
URxvt*foreground: #ffffff
URxvt*background: #1e1e1e

! xterm fallback
XTerm*faceName: Monospace
XTerm*faceSize: 10
XTerm*foreground: white
XTerm*background: black

! GTK theming
Gtk/DecorationLayout: menu:minimize,maximize,close
EOF
# sudo echo "xfce4-session &" >> ~/.vnc/xstartup

cd /tmp
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg --ignore-depends -i google-chrome-stable_current_amd64.deb || true
apt-get install -f

# google-chrome &


source /etc/profile
vncserver-start