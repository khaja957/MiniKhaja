import cv2
import numpy as np

from pipeline.stage import PipelineStage


class ChromaKeyStage(PipelineStage):

    def begin(self, context):

        print("Removing green screen...")

    def process(self, context):

        project = context.project
        settings = project.chromakey

        kernel = np.ones(
            (
                settings.kernel_size,
                settings.kernel_size,
            ),
            np.uint8,
        )

        lower = np.array([
            settings.lower_h,
            settings.lower_s,
            settings.lower_v,
        ])

        upper = np.array([
            settings.upper_h,
            settings.upper_s,
            settings.upper_v,
        ])

        total = len(project.frames)

        for index, frame in enumerate(project.frames):

            if context.cancelled:
                return

            hsv = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2HSV
            )

            mask = cv2.inRange(
                hsv,
                lower,
                upper,
            )

            mask = cv2.morphologyEx(
                mask,
                cv2.MORPH_OPEN,
                kernel,
            )

            mask = cv2.morphologyEx(
                mask,
                cv2.MORPH_CLOSE,
                kernel,
            )

            alpha = cv2.bitwise_not(mask)

            if settings.feather_edges:

                alpha = cv2.GaussianBlur(
                    alpha,
                    (
                        settings.blur_size,
                        settings.blur_size,
                    ),
                    0,
                )

            rgba = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2BGRA,
            )

            rgba[:, :, 3] = alpha

            # Placeholder for future green despill
            if settings.despill:
                pass

            project.frames[index] = rgba

            context.report(
                "ChromaKey",
                index + 1,
                total,
            )

    def end(self, context):

        print("Chroma key completed.")