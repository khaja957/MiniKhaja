from pipeline.pipeline import Pipeline
from pipeline.chromakey import ChromaKeyStage
from pipeline.exporter import ExportStage
from pipeline.bounds import BoundsStage
from pipeline.canvas import CanvasStage
from pipeline.analyzer import AnimationAnalyzer


class StudioPipelineBuilder:

    def build(self):

        pipeline = Pipeline()

        pipeline.add_stage(

    ChromaKeyStage()

)

        pipeline.add_stage(

    AnimationAnalyzer()

)

        pipeline.add_stage(

    CanvasStage()

)

        pipeline.add_stage(

    ExportStage()

)


        return pipeline