const { St, Clutter } = imports.gi;
const Main = imports.ui.main;

let button;

function init() {}

function enable() {
    button = new St.Button({
        style_class: 'system-menu-action',
        reactive: true,
        can_focus: true,
        track_hover: true,
        label: 'ChatGPT Search'
    });
    button.connect('clicked', () => {
        imports.misc.util.spawn(['python3', `${GLib.get_home_dir()}/.local/share/gnome-shell/extensions/gnome-chatgpt-search-extension@serpil-s.github.com/utils.py`]);
    });

    Main.panel._rightBox.insert_child_at_index(button, 0);
}

function disable() {
    Main.panel._rightBox.remove_child(button);
}
