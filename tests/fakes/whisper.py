class FakeModel:
    def transcribe(self, audio, language="en", fp16=False):
        return {"segments": [{"text": "test"}]}

def load_model(name="base"):
    return FakeModel()
