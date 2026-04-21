# Remove old versions
sudo apt-get remove -y docker docker-engine docker.io containerd runc || true

# Install dependencies
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Add Docker’s official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
  $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine + Compose plugin
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


sudo systemctl enable docker
sudo systemctl start docker




sudo wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 \
  -O /usr/local/bin/yq
sudo chmod +x /usr/local/bin/yq
yq --version


sudo apt-get install -y openssl
sudo apt-get install -y git

docker --version
docker compose version
yq --version
openssl version

sudo ufw allow from any to any port 80 proto tcp
sudo ufw allow from any to any port 443 proto tcp
sudo ufw allow from any to any port 53 proto tcp


sudo mkdir -p /etc/stackweaver
sudo chmod 755 /etc/stackweaver


echo "sudo usermod -aG docker \$USER"
echo "sudo usermod -aG docker \$USER"



# RELOGIN required
