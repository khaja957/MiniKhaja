from dataclasses import dataclass
from datetime import datetime


@dataclass
class AssetMetadata:

    character: str
    animation: str
    version: int
    prompt: str
    created: str = datetime.now().isoformat()