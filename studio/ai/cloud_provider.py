from pathlib import Path

from .provider import AIProvider


class CloudProvider(AIProvider):

    def generate_image(
        self,
        prompt,
        output_path
    ):

        raise NotImplementedError(
            "Cloud provider not implemented yet."
        )