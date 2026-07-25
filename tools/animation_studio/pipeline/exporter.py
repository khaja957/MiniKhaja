from pathlib import Path
import json
import cv2

from pipeline.stage import PipelineStage
from models.animation_asset import AnimationAsset


LOOPING_ANIMATIONS = {
    "Idle",
    "Idle_at_wall",
    "Walk",
    "Run",
    "Sleep"
}


class ExportStage(PipelineStage):

    def begin(self, context):

        project = context.project

        project.output_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        print(
            f"Exporting frames to: {project.output_folder}"
        )

    # ----------------------------------------------------------

    def process(self, context):

        project = context.project

        asset = AnimationAsset()

        asset.name = project.video_path.stem

        asset.fps = project.fps

        asset.frame_count = len(project.frames)

        asset.canvas_width = project.normalized_width

        asset.canvas_height = project.normalized_height

        asset.loop = asset.name in LOOPING_ANIMATIONS

        #
        # Bottom-center pivot
        #
        asset.pivot_x = asset.canvas_width // 2

        asset.pivot_y = asset.canvas_height - 1

        total = len(project.frames)

        for index, frame in enumerate(project.frames):

            if context.cancelled:
                return

            filename = f"{index:04d}.png"

            filepath = project.output_folder / filename

            success = cv2.imwrite(
                str(filepath),
                frame
            )

            if not success:

                raise RuntimeError(
                    f"Failed to export {filepath}"
                )

            #
            # Store only filename
            #
            asset.frames.append(filename)

            context.report(
                "Export",
                index + 1,
                total
            )

        #
        # Save asset in project
        #
        project.asset = asset

        #
        # Generate metadata
        #
        metadata = {

            "name": asset.name,

            "fps": asset.fps,

            "loop": asset.loop,

            "frame_count": asset.frame_count,

            "canvas": {

                "width": asset.canvas_width,

                "height": asset.canvas_height

            },

            "pivot": {

                "x": asset.pivot_x,

                "y": asset.pivot_y

            },

            "frames": asset.frames

        }

        metadata_file = (
            project.output_folder /
            "metadata.json"
        )

        with open(
            metadata_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                metadata,
                f,
                indent=4
            )

    # ----------------------------------------------------------

    def end(self, context):

        asset = context.project.asset

        print()

        print("Export completed successfully.")

        print(
            f"Frames : {asset.frame_count}"
        )

        print(
            f"Canvas : "
            f"{asset.canvas_width} x "
            f"{asset.canvas_height}"
        )

        print(
            f"Pivot  : "
            f"({asset.pivot_x}, "
            f"{asset.pivot_y})"
        )

        print(
            f"Loop   : {asset.loop}"
        )