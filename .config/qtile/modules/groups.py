from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod
import subprocess


def go_group_screen(name: str):
    def _inner(qtile) -> None:
        if name in ["1", "2", "3", "4"]:
            qtile.focus_screen(0)
        elif name in ["5", "6", "7", "8"]:
            qtile.focus_screen(1)
        qtile.groups_map[name].cmd_toscreen()

    return _inner


def move_win_group(group_name):
    def _inner(qtile):
        current_group = qtile.current_group.name
        current_screen = qtile.current_screen.index
        if group_name in ["1", "2", "3", "4"]:
            target_screen = 0
        else:
            target_screen = 1

        # Move the window to the target group
        qtile.current_window.togroup(group_name)

        # If the target group is on another screen, switch that screen to its target group
        if target_screen != current_screen:
            qtile.cmd_to_screen(target_screen)
            qtile.groups_map[group_name].cmd_toscreen()
            # Switch back to the original screen and group
            qtile.cmd_to_screen(current_screen)
            qtile.groups_map[current_group].cmd_toscreen()

        # If the target group is on the same screen, also switch to that group
        else:
            qtile.groups_map[group_name].cmd_toscreen()

    return _inner


def get_keyboard_layout():
    try:
        output = subprocess.check_output(["setxkbmap", "-query"])
        layout_line = [
            line for line in output.decode().split("\n") if "layout" in line
        ][0]
        return layout_line.split(":")[1].strip()
    except Exception as e:
        print(f"Failed to get keyboard layout: {e}")
        return "us"


keyboard_layout = get_keyboard_layout()
key_names = []

if keyboard_layout == "fr":  # French (Azerty)
    key_names = [
        "ampersand",
        "eacute",
        "quotedbl",
        "apostrophe",
        "parenleft",
        "minus",
        "egrave",
        "underscore",
    ]
elif keyboard_layout == "us":  # US (Qwerty)
    key_names = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
    ]

labels = [
    "",
    "",
    "",
    "",
    "󰙯",
    "󰖟",
    "󰌲",
    "󰛓",
]

groups = [Group(f"{i+1}", label=labels[i]) for i in range(8)]

for idx, group in enumerate(groups):
    key = key_names[idx]
    keys.extend(
        [
            Key(
                [mod],
                key,
                lazy.function(go_group_screen(group.name)),
                desc=f"Switch to group {group.name}",
            ),
            Key(
                [mod, "shift"],
                key,
                lazy.function(move_win_group(group.name)),
                desc=f"Smart move focused window to group {group.name}",
            ),
        ]
    )
