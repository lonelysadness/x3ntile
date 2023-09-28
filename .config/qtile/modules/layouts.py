from libqtile import layout

layouts = [
    layout.Columns(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        border_width=2,
        margin=4,
    ),
    layout.Tile(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        border_width=2,
        margin=4,
    ),
    layout.Max(
        border_focus="#1F1D2E",
        border_normal="#1F1D2E",
        margin=4,
    ),
]
