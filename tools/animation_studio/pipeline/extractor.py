import cv2


class FrameExtractor:

    def extract(self, project):

        cap = cv2.VideoCapture(str(project.video_path))

        if not cap.isOpened():

            raise RuntimeError(
                f"Unable to open {project.video_path}"
            )

        project.fps = cap.get(cv2.CAP_PROP_FPS)

        project.frame_count = int(
            cap.get(cv2.CAP_PROP_FRAME_COUNT)
        )

        print(f"FPS    : {project.fps}")
        print(f"Frames : {project.frame_count}")

        while True:

            success, frame = cap.read()

            if not success:

                break

            project.frames.append(frame)

        cap.release()

        print(f"Loaded {len(project.frames)} frames.")