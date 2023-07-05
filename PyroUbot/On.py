class abc:
    def command_filter(self, commands, case_sensitive=False):
        command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

        async def func(_, __, message):
            if message.text and message.from_user:
                prefix = await self.get_prefix(message.from_user.id)
                text = message.text.strip()
                matched_prefix = next((p for p in prefix if text.startswith(p)), None)
                if matched_prefix:
                    without_prefix = text[len(matched_prefix) :]

                    commands = commands if isinstance(commands, list) else [commands]
                    commands = {c if case_sensitive else c.lower() for c in commands}

                    for cmd in commands:
                        if not re.match(
                            rf"^(?:{cmd})(?:\s|$)",
                            without_prefix,
                            flags=re.IGNORECASE if not case_sensitive else 0,
                        ):
                            continue

                        without_command = re.sub(
                            rf"{cmd}\s?",
                            "",
                            without_prefix,
                            count=1,
                            flags=re.IGNORECASE if not case_sensitive else 0,
                        )
                        message.command = [cmd] + [
                            re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                            for m in command_re.finditer(without_command)
                        ]

                        return True
            return False

        return filters.create(func)
