class Link(str):
    def __new__(cls, value):
        prefix = 'http://www.reddit.com/r/music'
        if not value.startswith(prefix):
            raise ValueError(f"Link must start with '{prefix}'")
        return str.__new__(cls, value)
