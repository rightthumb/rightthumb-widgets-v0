#!/bin/bash

# Ensure a PowerShell script is provided
if [ -z "$1" ]; then
    echo "Usage: $0 script.ps1"
    exit 1
fi

PS1_FILE="$1"
APP_NAME="$(basename "$PS1_FILE" .ps1)"
CS_FILE="$APP_NAME.cs"
BUILD_DIR="$APP_NAME.AppDir"
OUT_DIR="$APP_NAME.ps1.AppImage"
INDEX_DB="/var/lib/plocate/plocate.db"

# Define required executables
REQUIREMENTS=("dotnet" "pwsh" "appimagetool" "mksquashfs" "plocate")

# Detect package manager
if command -v apt &>/dev/null; then
    PKG_MANAGER="sudo apt install -y"
    UPDATE_CMD="sudo apt update"
elif command -v dnf &>/dev/null; then
    PKG_MANAGER="sudo dnf install -y"
    UPDATE_CMD="sudo dnf check-update"
elif command -v pacman &>/dev/null; then
    PKG_MANAGER="sudo pacman -Sy --needed"
    UPDATE_CMD="sudo pacman -Syu"
else
    echo "Unsupported Linux distribution. Exiting."
    exit 1
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to find executables using plocate
find_with_plocate() {
    if command_exists plocate; then
        plocate -b "\$1" | head -n 1 | xargs dirname 2>/dev/null
    else
        echo ""
    fi
}

# Function to install a package via the package manager
install_package() {
    echo "Installing $1..."
    eval "$UPDATE_CMD && $PKG_MANAGER $1"
}

# Function to update plocate database
update_plocate_db() {
    if [ -w "$INDEX_DB" ]; then
        echo "Updating plocate database..."
        sudo updatedb
    else
        echo "Running plocate database update (without root)..."
        updatedb
    fi
}

# Main check loop
MISSING_REQUIREMENTS=()
for exe in "${REQUIREMENTS[@]}"; do
    if ! command_exists "$exe"; then
        PATH_FOUND=$(find_with_plocate "$exe")

        if [ -z "$PATH_FOUND" ]; then
            MISSING_REQUIREMENTS+=("$exe")
        else
            echo "Found $exe in $PATH_FOUND"
            export PATH="$PATH:$PATH_FOUND"
        fi
    fi
done

# If any requirements are missing, check plocate and prompt to install
if [ "${#MISSING_REQUIREMENTS[@]}" -gt 0 ]; then
    if ! command_exists plocate; then
        echo "plocate is not installed. Do you want to install plocate to find missing dependencies? (Y/N)"
        read -r RESPONSE
        if [[ "$RESPONSE" =~ ^[Yy]$ ]]; then
            install_package "plocate"
            update_plocate_db
        fi
    fi

    # Re-check for missing dependencies after installing plocate
    STILL_MISSING=()
    for exe in "${MISSING_REQUIREMENTS[@]}"; do
        PATH_FOUND=$(find_with_plocate "$exe")
        if [ -z "$PATH_FOUND" ]; then
            STILL_MISSING+=("$exe")
        else
            echo "Located $exe in $PATH_FOUND"
            export PATH="$PATH:$PATH_FOUND"
        fi
    done

    # If still missing after using plocate, install via package manager
    if [ "${#STILL_MISSING[@]}" -gt 0 ]; then
        echo "The following packages are still missing: ${STILL_MISSING[*]}"
        echo "Installing missing dependencies..."
        for pkg in "${STILL_MISSING[@]}"; do
            install_package "$pkg"
        done
    fi
fi

# 📝 Generate C# wrapper
cat <<EOF > "$CS_FILE"
using System;
using System.Diagnostics;
using System.IO;
using System.Text;

class Program {
    static void Main() {
        string scriptPath = "$PS1_FILE";
        ProcessStartInfo psi = new ProcessStartInfo("pwsh", "-ExecutionPolicy Bypass -NoProfile -File " + scriptPath);
        psi.UseShellExecute = false;
        psi.RedirectStandardOutput = true;
        Process process = Process.Start(psi);
        process.WaitForExit();
    }
}
EOF

# 🎯 Create and build .NET project
dotnet new console -o "$APP_NAME" --force > /dev/null
mv "$CS_FILE" "$APP_NAME/Program.cs"
cd "$APP_NAME" || exit
dotnet publish -c Release -r linux-x64 --self-contained true > /dev/null
cd ..

# 📂 Create AppDir structure
mkdir -p "$BUILD_DIR/usr/bin"
mkdir -p "$BUILD_DIR/usr/share/icons"

# Copy compiled binary
cp "$APP_NAME/bin/Release/net8.0/linux-x64/publish/$APP_NAME" "$BUILD_DIR/usr/bin/$APP_NAME"

# Copy PowerShell script inside AppImage
cp "$PS1_FILE" "$BUILD_DIR/script.ps1"

# 🔄 Create AppRun script
cat <<EOF > "$BUILD_DIR/AppRun"
#!/bin/bash
exec "\$(dirname "\$0")/usr/bin/$APP_NAME"
EOF
chmod +x "$BUILD_DIR/AppRun"

# 🖥️ Create Desktop Entry
cat <<EOF > "$BUILD_DIR/$APP_NAME.desktop"
[Desktop Entry]
Name=$APP_NAME
Exec=AppRun
Icon=$APP_NAME
Type=Application
Categories=Utility;
EOF

# 🚀 Create AppImage
appimagetool "$BUILD_DIR" "$OUT_DIR"

# 🧹 Cleanup (optional)
rm -rf "$APP_NAME" "$BUILD_DIR"

echo "✅ AppImage created: $OUT_DIR"
