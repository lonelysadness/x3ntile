import subprocess
from libqtile.widget import GenPollText


class AudioWidget(GenPollText):
    colors = {
        "ON3": "#92A798",
        "ON2": "#607767",
        "ON1": "#404F45",
        "MUTE": "#BF616A",
        "REC": "#607767",
    }

    def __init__(self, **config):
        GenPollText.__init__(self, **config)
        self.add_defaults(
            [
                ("update_interval", 1, "Update interval for the script"),
                ("background", "#202222", "Background color"),
                ("font", "JetBrainsMono Nerd Font Bold", "Default font"),
            ]
        )
        self.mouse_callbacks = {
            "Button1": self.toggle_audio,
            "Button2": self.toggle_microphone,
            "Button3": self.choose_device,
            "Button4": self.volume_up,
            "Button5": self.volume_down,
        }

    def execute_command(self, command):
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        return stdout.decode("utf-8").strip()

    def toggle_audio(self):
        self.execute_command("pactl set-sink-mute @DEFAULT_SINK@ toggle")

    def toggle_microphone(self):
        self.execute_command("pactl set-source-mute @DEFAULT_SOURCE@ toggle")

    def volume_up(self):
        self.execute_command("pactl set-sink-volume @DEFAULT_SINK@ +5%")

    def volume_down(self):
        self.execute_command("pactl set-sink-volume @DEFAULT_SINK@ -5%")

    def choose_device(self):
        try:
            old_sink = self.execute_command("pactl get-default-sink")
            sink_output = self.execute_command("LC_ALL=C pactl list sinks")
            sinks = {}
            for block in sink_output.split("\n\n"):
                name = description = None
                for line in block.split("\n"):
                    if "Name: " in line:
                        name = line.split("Name: ")[1]
                    if "Description: " in line:
                        description = line.split("Description: ")[1]
                    if name and description:
                        sinks[description] = name

            chosen_sink_desc = subprocess.run(
                ["rofi", "-dmenu", "-i", "-p", "Output"],
                input="\n".join(sinks.keys()),
                text=True,
                capture_output=True,
            ).stdout.strip()

            if chosen_sink_desc:
                chosen_sink_name = sinks.get(chosen_sink_desc)
                if chosen_sink_name and chosen_sink_name != old_sink:
                    self.execute_command(f"pactl set-default-sink {chosen_sink_name}")
                    self.execute_command(
                        f"notify-send 'Audio output changed to {chosen_sink_desc}'"
                    )

            old_source = self.execute_command("pactl get-default-source")
            source_output = self.execute_command("LC_ALL=C pactl list sources")
            sources = {}
            for block in source_output.split("\n\n"):
                name = description = None
                for line in block.split("\n"):
                    if "Name: " in line:
                        name = line.split("Name: ")[1]
                    if "Description: " in line:
                        description = line.split("Description: ")[1]
                    if name and description:
                        sources[description] = name

            chosen_source_desc = subprocess.run(
                ["rofi", "-dmenu", "-i", "-p", "Input"],
                input="\n".join(sources.keys()),
                text=True,
                capture_output=True,
            ).stdout.strip()

            if chosen_source_desc:
                chosen_source_name = sources.get(chosen_source_desc)
                if chosen_source_name and chosen_source_name != old_source:
                    self.execute_command(
                        f"pactl set-default-source {chosen_source_name}"
                    )
                    self.execute_command(
                        f"notify-send 'Audio input changed to {chosen_source_desc}'"
                    )

        except Exception as e:
            print(f"Error: {e}")

    def poll(self):
        audio_muted = self.execute_command(
            "LC_ALL=C pactl get-sink-mute @DEFAULT_SINK@"
        ).split(": ")[1]
        microphone_muted = self.execute_command(
            "LC_ALL=C pactl get-source-mute @DEFAULT_SOURCE@"
        ).split(": ")[1]
        volume = int(
            self.execute_command("pactl get-sink-volume @DEFAULT_SINK@")
            .split("/")[1]
            .strip()
            .replace("%", "")
        )

        audio_state = (
            "MUTE"
            if audio_muted == "yes"
            else (
                "ON1" if 0 < volume <= 50 else ("ON2" if 51 <= volume <= 100 else "ON3")
            )
        )

        microphone_state = "MUTE" if microphone_muted == "yes" else "REC"

        audio_icon = (
            ""
            if "ON3" in audio_state
            else ""
            if "ON2" in audio_state
            else ""
            if "ON1" in audio_state
            else ""
        )
        mic_icon = "" if "REC" in microphone_state else ""

        audio_color = self.colors[audio_state]
        mic_color = self.colors[microphone_state]

        return f"<span color='{audio_color}'>{audio_icon}</span>   <span color='{mic_color}'>{mic_icon}</span>"
