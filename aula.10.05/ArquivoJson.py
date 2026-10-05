import json
from pathlib import Path

CONFIG_FILE = Path('settings.json')
DEFAULT_CONFIG = {"theme": "dark", "font_size": 14, "auto_save": True}
def carregar_configuracoes():
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
            return DEFAULT_CONFIG

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

opts = carregar_configuracoes()
print(f"Tema atual: {opts['theme']}, {opts['auto_save']}")
