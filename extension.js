const { Clutter, St } = imports.gi;
const Main = imports.ui.main;

let button; // Uzantı UI bileşeni için bir değişken

function enable() {
    // Button UI nesnesi oluştur
    button = new St.Button({
        style_class: 'system-menu-action',
        reactive: true,
        can_focus: true,
        track_hover: true,
        label: 'AI Question Search',
    });

    // GNOME Shell UI'ya ekle
    Main.panel._leftBox.insert_child_at_index(button, 0);

    // Tıklama olayını bağla
    button.connect('clicked', () => {
        imports.misc.util.spawn(['python3', '/usr/share/gnome-shell/extensions/ai-question-search@serpil-s/ai_question_search.py']);
    });
}

function disable() {
    // Button nesnesini kaldır ve temizle
    if (button) {
        button.destroy(); // Nesneyi yok et
        button = null;    // Referansı temizle
    }
}
