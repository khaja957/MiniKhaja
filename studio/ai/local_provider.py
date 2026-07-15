from pathlib import Path
import shutil

from .provider import AIProvider
from studio.settings import StudioSettings

class LocalProvider(AIProvider):

    def generate_image(self, prompt, output_path):

        placeholder = StudioSettings.PLACEHOLDER

        shutil.copy(
            placeholder,
            output_path
        )

        return output_path