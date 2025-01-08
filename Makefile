install:
	mkdir -p ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
	cp * ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
	sudo mkdir -p /usr/share/gnome-shell/search-providers
	sudo cp chatgpt-search-provider.ini /usr/share/gnome-shell/search-providers/
	sudo cp chatgpt-search.desktop /usr/share/applications/
	gnome-extensions enable chatgpt-search@serpil-s

uninstall:
	gnome-extensions disable chatgpt-search@serpil-s
	rm -rf ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
	sudo rm -f /usr/share/gnome-shell/search-providers/chatgpt-search-provider.ini
	sudo rm -f /usr/share/applications/chatgpt-search.desktop
