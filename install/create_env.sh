#!/bin/bash

sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-full


# Paths
BASHRC_DOT="$HOME/.bashrc."
ENV_PATH="$HOME/env"

# Step 1: Check if the virtual environment already exists
if [ -d "$ENV_PATH" ]; then
    echo "Virtual environment already exists at $ENV_PATH. Doing nothing."
    exit 0
fi

# Step 2: Create the virtual environment
python3 -m venv "$ENV_PATH"
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment at $ENV_PATH."
    exit 1
fi
echo "Virtual environment created at $ENV_PATH."

# Step 3: Ensure .bashrc. exists and starts with #!/bin/bash
if [ ! -f "$BASHRC_DOT" ]; then
    echo "Creating $BASHRC_DOT with #!/bin/bash."
    echo "#!/bin/bash" > "$BASHRC_DOT"
fi

# Step 4: Add auto-activation code to .bashrc. if not already present
if ! grep -q "/bin/activate" "$BASHRC_DOT"; then
    echo "Adding auto-activation code to $BASHRC_DOT."
    {
        echo -e "\n# Auto-activate virtual environment"
        echo "if [ -d \"$ENV_PATH\" ]; then"
        echo "    source \"$ENV_PATH/bin/activate\""
        echo "fi"
    } >> "$BASHRC_DOT"
fi

# Step 5: Activate the environment immediately
source "$ENV_PATH/bin/activate"
echo "Virtual environment activated. You can now use it."

echo "export env_='true'" >> "$ENV_PATH/bin/activate"

exit 0



if [ -d "$HOME/env" ]; then
    source "$HOME/env/bin/activate"
fi
