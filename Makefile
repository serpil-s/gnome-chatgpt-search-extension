install:
	mkdir -p ~/.local/share/gnome-shell/extensions/chatgpt-search@yourusername
	cp * ~/.local/share/gnome-shell/extensions/chatgpt-search@yourusername
	gnome-extensions enable chatgpt-search@yourusername

uninstall:
	gnome-extensions disable chatgpt-search@yourusername
	rm -rf ~/.local/share/gnome-shell/extensions/chatgpt-search@yourusername
