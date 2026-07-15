from studio.ai.local_provider import LocalProvider


class AIService:

    def __init__(self):

        self.provider = LocalProvider()

    def generate_image(
        self,
        prompt,
        output_path
    ):

        return self.provider.generate_image(
            prompt,
            output_path
        )