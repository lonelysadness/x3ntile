from libqtile import bar, qtile, widget
from libqtile.config import Screen
from .audio_widget import *


def create_image_widget(filename, margin=0, background=None, mouse_callbacks=None):
    return widget.Image(
        filename=filename,
        margin=margin,
        background=background,
        mouse_callbacks=mouse_callbacks,
    )


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


screen1 = Screen(
    top=bar.Bar(
        [
            widget.Spacer(length=15, background="#0F1212"),
            create_image_widget(
                "~/.config/qtile/assets/logo.png",
                margin=2,
                background="#0F1212",
                mouse_callbacks={"Button1": power},
            ),
            create_image_widget("~/.config/qtile/assets/sep_1.png"),
            widget.GroupBox(
                fontsize=18,
                borderwidth=4,
                highlight_method="block",
                active="#607767",
                block_highlight_text_color="#B2BEBC",
                highlight_color="#D0DAF0",
                inactive="#0F1212",
                foreground="#4B427E",
                this_current_screen_border="#202222",
                this_screen_border="#202222",
                other_current_screen_border="#202222",
                other_screen_border="#202222",
                urgent_border="#202222",
                rounded=False,
                disable_drag=True,
            ),
            widget.Spacer(length=18),
            create_image_widget("~/.config/qtile/assets/sep_2.png"),
            create_image_widget(
                "~/.config/qtile/assets/layout.png", background="#202222"
            ),
            widget.CurrentLayout(),
            create_image_widget("~/.config/qtile/assets/sep_3.png"),
            create_image_widget(
                "~/.config/qtile/assets/search.png",
                margin=2,
                background="#0F1212",
                mouse_callbacks={"Button1": search},
            ),
            widget.TextBox(
                fmt="Search",
                background="#0F1212",
                mouse_callbacks={"Button1": search},
            ),
            create_image_widget("~/.config/qtile/assets/sep_4.png"),
            widget.WindowName(
                format="{name}",
                empty_group_string="Desktop",
            ),
            create_image_widget("~/.config/qtile/assets/sep_5.png"),
            widget.Systray(
                background="#0F1212",
            ),
            widget.TextBox(text=" ", background="#0F1212"),
            create_image_widget(
                "~/.config/qtile/assets/sep_1.png", background="#202222"
            ),
            widget.Spacer(length=-7),
            widget.Spacer(length=8),
            widget.CheckUpdates(
                colour_have_updates="#607767",
                distro="Arch_paru",
                execute="kitty -e paru",
                update_interval=3600,
            ),
            create_image_widget("~/.config/qtile/assets/sep_6.png"),
            widget.Spacer(length=8),
            AudioWidget(fontsize=15),
            create_image_widget("~/.config/qtile/assets/sep_3.png"),
            create_image_widget(
                "~/.config/qtile/assets/Misc/clock.png",
                background="0F1212",
                margin=6,
            ),
            widget.Clock(
                format="%I:%M %p",
                background="#0F1212",
            ),
            widget.Spacer(length=18, background="#0F1212"),
        ],
        24,
        border_color="#0F1212",
        border_width=[0, 0, 0, 0],
        margin=[0, 0, 0, 0],
    ),
)

screen2 = Screen(
    top=bar.Bar(
        [
            widget.Spacer(length=15, background="#0F1212"),
            create_image_widget(
                "~/.config/qtile/assets/logo.png",
                margin=2,
                background="#0F1212",
                mouse_callbacks={"Button1": power},
            ),
            create_image_widget("~/.config/qtile/assets/sep_1.png"),
            widget.GroupBox(
                fontsize=18,
                borderwidth=4,
                highlight_method="block",
                active="#607767",
                block_highlight_text_color="#B2BEBC",
                highlight_color="#D0DAF0",
                inactive="#0F1212",
                foreground="#4B427E",
                this_current_screen_border="#202222",
                this_screen_border="#202222",
                other_current_screen_border="#202222",
                other_screen_border="#202222",
                urgent_border="#202222",
                rounded=False,
                disable_drag=True,
            ),
            widget.Spacer(length=8),
            create_image_widget("~/.config/qtile/assets/sep_2.png"),
            create_image_widget(
                "~/.config/qtile/assets/layout.png", background="#202222"
            ),
            widget.CurrentLayout(),
            create_image_widget("~/.config/qtile/assets/sep_3.png"),
            create_image_widget(
                "~/.config/qtile/assets/search.png",
                margin=2,
                background="#0F1212",
                mouse_callbacks={"Button1": search},
            ),
            widget.TextBox(
                fmt="Search",
                background="#0F1212",
                mouse_callbacks={"Button1": search},
            ),
            create_image_widget("~/.config/qtile/assets/sep_4.png"),
            widget.WindowName(
                format="{name}",
                empty_group_string="Desktop",
            ),
            create_image_widget("~/.config/qtile/assets/sep_5.png"),
            widget.TextBox(text=" ", background="#0F1212"),
            create_image_widget("~/.config/qtile/assets/sep_1.png"),
            create_image_widget(
                "~/.config/qtile/assets/Misc/ram.png", background="#202222"
            ),
            widget.Memory(
                format="{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}",
                update_interval=5,
            ),
            create_image_widget("~/.config/qtile/assets/sep_6.png"),
            widget.Spacer(length=8),
            widget.CPU(
                update_interval=1,
            ),
            create_image_widget("~/.config/qtile/assets/sep_6.png"),
            widget.TextBox(
                fmt="GPU",
            ),
            widget.NvidiaSensors(foreground="#607767"),
            create_image_widget(
                "~/.config/qtile/assets/sep_3.png", background="#202222"
            ),
            create_image_widget(
                "~/.config/qtile/assets/Misc/clock.png",
                background="0F1212",
                margin=6,
            ),
            widget.Clock(
                format="%I:%M %p",
                background="#0F1212",
            ),
            widget.Spacer(length=18, background="#0F1212"),
        ],
        24,
        border_color="#0F1212",
        border_width=[0, 0, 0, 0],
        margin=[0, 0, 0, 0],
    ),
)

screens = [screen1, screen2]
