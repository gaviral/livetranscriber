class FakeWebSocket:
    def on(self, *a, **k):
        pass
    def start(self, *a, **k):
        pass
    def send(self, *a, **k):
        pass
    def finish(self):
        pass

class _WSWrapper:
    def v(self, _):
        return FakeWebSocket()

class _Listen:
    def __init__(self):
        self.websocket = _WSWrapper()

class DeepgramClient:
    def __init__(self, api_key, opts=None):
        self.listen = _Listen()

class DeepgramClientOptions:
    def __init__(self, options=None):
        self.options = options

class LiveOptions(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.update(kwargs)

class LiveTranscriptionEvents:
    Open = "open"
    Transcript = "transcript"
    Error = "error"
    Close = "close"
