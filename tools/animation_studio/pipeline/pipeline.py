class Pipeline:

    def __init__(self):

        self.stages = []

    def add_stage(self, stage):

        self.stages.append(stage)

    def execute(self, context):

        context.begin()

        for stage in self.stages:

            if context.cancelled:

                return

            stage.begin(context)

            stage.process(context)

            stage.end(context)

        print()

        print(
            f"Pipeline completed in "
            f"{context.elapsed():.2f}s"
        )