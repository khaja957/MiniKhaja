import cv2

from pipeline.stage import PipelineStage
from models.bounding_box import BoundingBox


class BoundsStage(PipelineStage):

    def begin(self, project):

        project.bounds.clear()

    def process(self, project):

        max_width = 0

        max_height = 0

        for frame in project.frames:

            alpha = frame[:, :, 3]

            points = cv2.findNonZero(alpha)

            if points is None:

                project.bounds.append(
                    BoundingBox(0,0,0,0)
                )

                continue

            x, y, w, h = cv2.boundingRect(points)

            project.bounds.append(
                BoundingBox(x,y,w,h)
            )

            max_width = max(max_width, w)

            max_height = max(max_height, h)

        project.normalized_width = max_width

        project.normalized_height = max_height

    def end(self, project):

        print()

        print("Largest Canvas")

        print(project.normalized_width)

        print(project.normalized_height)