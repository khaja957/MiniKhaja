from abc import ABC


class PipelineStage(ABC):

    def begin(self, context):
        pass

    def process(self, context):
        pass

    def end(self, context):
        pass