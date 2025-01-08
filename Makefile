install:
	mkdir -p ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
	cp * ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
	sudo mkdir -p /usr/share/gnome-shell/search-providers
	sudo cp chatgpt-search-provider.ini /usr/share/gnome-shell/search-providers/
	sudo cp chatgpt-search.desktop /usr/share/applications/
	sudo cp org.gnome.ChatGPT.service /usr/share/dbus-1/services/
	gnome-extensions enable chatgpt-search@serpil-s

uninstall:
	gnome-extensions disable chatgpt-search@serpil-s || echo "Extension not enabled."
	rm -rf ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
	sudo rm -f /usr/share/gnome-shell/search-providers/chatgpt-search-provider.ini
	sudo rm -f /usr/share/applications/chatgpt-search.desktop
	sudo rm -f /usr/share/dbus-1/services/org.gnome.ChatGPT.service
