from pathlib import Path

from .base_generator import BaseGenerator


class PlaceholderGenerator(BaseGenerator):

    def generate(self, prompt: str):

        print("Generating asset...")

        print(prompt)

        placeholder = Path("studio/resources/placeholder.png")

        return placeholder