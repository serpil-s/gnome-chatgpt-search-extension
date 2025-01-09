EXTENSION_UUID = ai21-search@serpil-s
INSTALL_DIR = ~/.local/share/gnome-shell/extensions/$(EXTENSION_UUID)

.PHONY: install uninstall

install:
	@echo "Installing AI21 Search Extension..."
	mkdir -p $(INSTALL_DIR)
	cp -r * $(INSTALL_DIR)
	sudo mkdir -p /usr/share/gnome-shell/search-providers
	sudo cp chatgpt-search-provider.ini /usr/share/gnome-shell/search-providers/
	sudo cp chatgpt-search.desktop /usr/share/applications/
	@echo "Checking dependencies..."
	@if ! command -v python3 &>/dev/null; then sudo apt install -y python3; fi
	@if ! python3 -c "import ai21" &>/dev/null; then pip install ai21; fi
	@echo "Enabling GNOME extension..."
	gnome-extensions enable $(EXTENSION_UUID)
	@echo "Installation complete."

uninstall:
	@echo "Uninstalling AI21 Search Extension..."
	rm -rf $(INSTALL_DIR)
	sudo rm -f /usr/share/gnome-shell/search-providers/chatgpt-search-provider.ini
	sudo rm -f /usr/share/applications/chatgpt-search.desktop
	gnome-extensions disable $(EXTENSION_UUID)
	@echo "Uninstallation complete."
