const { Gio, St, Clutter } = imports.gi;
const Main = imports.ui.main;
const Util = imports.misc.util;

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
        Util.spawn(['python3', `${Me.path}/utils.py`]);
    });

    Main.panel._rightBox.insert_child_at_index(button, 0);
}

function disable() {
    Main.panel._rightBox.remove_child(button);
}
