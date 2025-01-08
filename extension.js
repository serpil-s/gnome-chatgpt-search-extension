const { St } = imports.gi;
const Main = imports.ui.main;
const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;

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
        Gio.Subprocess.new(
            ['python3', `${GLib.get_home_dir()}/.local/share/gnome-shell/extensions/chatgpt-search@serpil-s/utils.py`, "What is AI?"],
            Gio.SubprocessFlags.NONE
        );
    });

    Main.panel._rightBox.insert_child_at_index(button, 0);
}

function disable() {
    Main.panel._rightBox.remove_child(button);
}
