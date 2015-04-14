

class MiniMatch:

    _defaults = dict(
      follow_links=True,
      list_directories=True
    )

    def __init__(self, *patterns, **kwargs):
        self._patterns = patterns

        self.__dict__.update(MiniMatch._defaults)
        self.__dict__.update(kwargs)

