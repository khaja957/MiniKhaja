from abc import ABC, abstractmethod
from pathlib import Path


class AIProvider(ABC):

    @abstractmethod
    def generate_image(
        self,
        prompt: str,
        output_path: Path,
    ) -> Path:
        """
        Generate an image.

        Returns the saved image path.
        """
        pass