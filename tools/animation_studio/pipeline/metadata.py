import json

from pipeline.stage import PipelineStage


class MetadataStage(PipelineStage):

    def begin(self, context):
        pass

    def process(self, context):

        project = context.project
        asset = project.asset

        metadata = {

            "name": asset.name,

            "fps": asset.fps,

            "frame_count": asset.frame_count,

            "canvas": {

                "width": asset.canvas_width,

                "height": asset.canvas_height

            },

            "frames": [

                path.name for path in asset.frame_paths

            ]

        }

        filename = project.output_folder / "metadata.json"

        with open(filename, "w") as f:

            json.dump(
                metadata,
                f,
                indent=4
            )

        context.report(
            "Metadata",
            1,
            1
        )

    def end(self, context):

        print("Metadata generated successfully.")