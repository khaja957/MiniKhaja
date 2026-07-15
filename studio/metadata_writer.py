import json
from dataclasses import asdict


class MetadataWriter:

    @staticmethod
    def save(metadata, json_path):

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(
                asdict(metadata),
                f,
                indent=4,
                ensure_ascii=False
            )