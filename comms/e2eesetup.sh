#!/bin/bash

# Directories
ENCRYPTED_DIR="$HOME/encrypted"
DECRYPTED_DIR="$HOME/decrypted"

# Ensure necessary directories exist
mkdir -p "$ENCRYPTED_DIR" "$DECRYPTED_DIR"

# Install necessary packages
install_packages() {
    sudo apt update
    sudo apt install -y gocryptfs firejail tor syncthing magic-wormhole
}

# Setup gocryptfs encryption
setup_gocryptfs() {
    if [ ! -f "$ENCRYPTED_DIR/gocryptfs.conf" ]; then
        echo "Initializing gocryptfs..."
        gocryptfs -init "$ENCRYPTED_DIR"
    fi
    gocryptfs "$ENCRYPTED_DIR" "$DECRYPTED_DIR"
}

# Configure Syncthing
setup_syncthing() {
    echo "Configuring Syncthing..."
    syncthing &
    sleep 5
    killall syncthing
    sed -i 's/<globalAnnounceEnabled>true<\/globalAnnounceEnabled>/<globalAnnounceEnabled>false<\/globalAnnounceEnabled>/g' ~/.config/syncthing/config.xml
    sed -i 's/<relaysEnabled>true<\/relaysEnabled>/<relaysEnabled>false<\/relaysEnabled>/g' ~/.config/syncthing/config.xml
    echo "Syncthing configured. Run 'syncthing' to start."
}

# Configure Tor Hidden Service for Syncthing
setup_tor_syncthing() {
    echo -e "HiddenServiceDir /var/lib/tor/syncthing/\nHiddenServicePort 22000 127.0.0.1:22000" | sudo tee -a /etc/tor/torrc
    sudo systemctl restart tor
    echo "Tor Hidden Service created. Address:"
    sudo cat /var/lib/tor/syncthing/hostname
}

# Setup Magic Wormhole
setup_magicwormhole() {
    echo "Magic Wormhole installed. Use 'wormhole send <file>' to share and 'wormhole receive <code>' to receive."
}

# Main menu
main_menu() {
    echo "Choose your file transfer method:"
    echo "1) Syncthing"
    echo "2) Magic Wormhole"
    echo "3) Setup Tor Hidden Service for Syncthing"
    echo "4) Exit"
    read -rp "Enter your choice: " choice

    case "$choice" in
        1)
            setup_gocryptfs
            setup_syncthing
            ;;
        2)
            setup_magicwormhole
            ;;
        3)
            setup_tor_syncthing
            ;;
        4)
            exit 0
            ;;
        *)
            echo "Invalid option, try again."
            main_menu
            ;;
    esac
}

# Run setup
install_packages
main_menu
