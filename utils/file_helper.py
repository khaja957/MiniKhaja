from pathlib import Path


def get_next_sprite_name(folder: Path, prefix: str):

    folder.mkdir(parents=True, exist_ok=True)

    existing = sorted(
        folder.glob(f"{prefix}_*.png")
    )

    if not existing:
        return f"{prefix}_01.png"

    numbers = []

    for file in existing:

        try:
            number = int(
                file.stem.split("_")[-1]
            )
            numbers.append(number)

        except ValueError:
            continue

    next_number = max(numbers) + 1

    return f"{prefix}_{next_number:02d}.png"