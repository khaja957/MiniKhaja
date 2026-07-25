from pathlib import Path

import cv2

from pipeline.stage import PipelineStage
from models.animation_asset import AnimationAsset


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

    def process(self, context):

        project = context.project

        asset = AnimationAsset(

            name=project.video_path.stem,

            fps=project.fps,

            frame_count=len(project.frames),

            canvas_width=project.normalized_width,

            canvas_height=project.normalized_height

        )

        total = len(project.frames)

        for index, frame in enumerate(project.frames):

            if context.cancelled:
                return

            filename = (
                project.output_folder /
                f"{index:04d}.png"
            )

            success = cv2.imwrite(
                str(filename),
                frame,
            )

            if not success:

                raise RuntimeError(

                    f"Failed to export {filename}"

                )

            asset.frame_paths.append(filename)

            context.report(

                "Export",

                index + 1,

                total

            )

        project.asset = asset

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

