const { Clutter, St } = imports.gi;
const Main = imports.ui.main;

let button;

function enable() {
    button = new St.Button({
        style_class: 'system-menu-action',
        reactive: true,
        can_focus: true,
        track_hover: true,
        label: 'AI Search',
    });

    Main.panel._leftBox.insert_child_at_index(button, 0);

    button.connect('clicked', () => {
        imports.misc.util.spawn(['python3', '/usr/share/gnome-shell/extensions/ai-question-search@serpil-s/ai_question_search.py']);
    });
}

function disable() {
    if (button) {
        button.destroy();
        button = null;
    }
}
