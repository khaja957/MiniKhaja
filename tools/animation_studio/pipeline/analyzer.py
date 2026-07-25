import cv2

from pipeline.stage import PipelineStage
from models.bounding_box import BoundingBox


class AnimationAnalyzer(PipelineStage):

    def begin(self, context):

        context.project.bounds.clear()

    def process(self, context):

        project = context.project

        max_width = 0
        max_height = 0

        total = len(project.frames)

        for index, frame in enumerate(project.frames):

            if context.cancelled:
                return

            alpha = frame[:, :, 3]

            points = cv2.findNonZero(alpha)

            if points is None:

                project.bounds.append(
                    BoundingBox(0, 0, 0, 0)
                )

                continue

            x, y, w, h = cv2.boundingRect(points)

            project.bounds.append(
                BoundingBox(
                    x,
                    y,
                    w,
                    h
                )
            )

            max_width = max(max_width, w)
            max_height = max(max_height, h)

            context.report(
                "Analyzer",
                index + 1,
                total
            )

        project.normalized_width = max_width
        project.normalized_height = max_height

    def end(self, context):

        project = context.project

        print()

        print("Animation Analysis Complete")

        print(
            f"Normalized Canvas : "
            f"{project.normalized_width} x "
            f"{project.normalized_height}"
        )