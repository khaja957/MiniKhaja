from character.asset import CharacterAsset

from studio.generators.generator_factory import GeneratorFactory


class AssetPipeline:

    def __init__(self):

        self.generator = GeneratorFactory.create()

    def generate(self, name: str, prompt: str):

        path = self.generator.generate(prompt)

        return CharacterAsset(

            name=name,

            asset_type="image",

            file_path=path,

            prompt=prompt
        )