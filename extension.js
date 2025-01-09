const { Clutter, St } = imports.gi;
const Main = imports.ui.main;

let button; // Uzantının eklediği buton

function enable() {
    // Yeni bir buton oluştur
    button = new St.Button({
        style_class: 'system-menu-action',
        reactive: true,
        can_focus: true,
        track_hover: true,
        label: 'Ask AI',
    });

    // GNOME Shell UI'ya butonu ekle
    Main.panel._leftBox.insert_child_at_index(button, 0);

    // Butona tıklama olayını bağla
    button.connect('clicked', () => {
        imports.misc.util.spawn(['python3', '/usr/share/gnome-shell/extensions/ai-question-search@serpil-s/ai_question_search.py']);
    });
}

function disable() {
    // Oluşturulan butonu temizle
    if (button) {
        button.destroy(); // Butonu yok et
        button = null;    // Referansı sıfırla
    }
}
