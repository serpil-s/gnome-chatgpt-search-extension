install:
	mkdir -p ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
	cp * ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
	gnome-extensions enable chatgpt-search@serpil-s

uninstall:
	gnome-extensions disable chatgpt-search@serpil-s
	rm -rf ~/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s
