import numpy as np

from pipeline.stage import PipelineStage


class CanvasStage(PipelineStage):

    def process(self, context):

        project = context.project

        normalized = []

        W = project.normalized_width
        H = project.normalized_height

        total = len(project.frames)

        for index, (frame, box) in enumerate(

            zip(project.frames, project.bounds)

        ):

            if context.cancelled:
                return

            canvas = np.zeros(

                (H, W, 4),

                dtype=np.uint8

            )

            if box.width == 0:

                normalized.append(canvas)

                continue

            cropped = frame[
                box.y:box.y + box.height,
                box.x:box.x + box.width
            ]

            x = (W - box.width) // 2

            y = H - box.height

            canvas[
                y:y + box.height,
                x:x + box.width
            ] = cropped

            normalized.append(canvas)

            context.report(

                "Canvas",

                index + 1,

                total

            )

        project.frames = normalized

    def end(self, context):

        print("Canvas normalization completed.")