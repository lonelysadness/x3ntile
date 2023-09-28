from libqtile import hook, qtile
import subprocess
import os


def setupscreen(qtile):
    for i, g in [(0, "1"), (1, "5")]:
        qtile.cmd_to_screen(i)
        qtile.groups_map[g].cmd_toscreen(toggle=False)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart_once.sh")
    subprocess.call([home])
    setupscreen(qtile)
