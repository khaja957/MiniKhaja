from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    @abstractmethod
    def generate(self, prompt: str):
        """
        Generate an asset from a prompt.

        Returns:
            Path to the generated asset.
        """
        pass