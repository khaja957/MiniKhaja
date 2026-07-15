from pathlib import Path

from .base_generator import BaseGenerator
from studio.settings import StudioSettings


class PlaceholderGenerator(BaseGenerator):

    def generate(self, prompt: str):

        print("Generating asset...")

        print(prompt)

        placeholder = StudioSettings.PLACEHOLDER

        return placeholder