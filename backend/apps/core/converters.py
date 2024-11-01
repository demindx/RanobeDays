class SliceConverter:
    regex = "[0-9]+:[0-9]+"

    def to_python(self, value: str):
        value = value.replace('[', '').replace(']', '')
        value = value.split(':')
        return (int(value[0]), int(value[1]))

    def to_url(self, value: tuple[int]):
        return f'[{value[0]}:{value[1]}]'
