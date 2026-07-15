from pathlib import Path


class StudioSettings:

    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    ASSETS = PROJECT_ROOT / "assets"

    SOURCE_IMAGES = ASSETS / "source" / "images"

    SOURCE_VIDEOS = ASSETS / "source" / "videos"

    SOURCE_PROMPTS = ASSETS / "source" / "prompts"

    PROCESSED = ASSETS / "processed"

    EXPORT = ASSETS / "exported"

    PLACEHOLDER = (
        PROJECT_ROOT
        / "studio"
        / "resources"
        / "placeholder.png"
    )

    GENERATED = SOURCE_IMAGES / "generated"