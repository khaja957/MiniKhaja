from .placeholder_generator import PlaceholderGenerator


class GeneratorFactory:

    @staticmethod
    def create():

        return PlaceholderGenerator()