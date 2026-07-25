from dataclasses import dataclass
from time import perf_counter

from models.animation_project import AnimationProject


@dataclass
class PipelineContext:

    project: AnimationProject

    current_stage: str = ""

    progress: float = 0.0

    cancelled: bool = False

    start_time: float = 0.0

    def begin(self):

        self.start_time = perf_counter()

    def elapsed(self):

        return perf_counter() - self.start_time

    def report(self, stage, current, total):

        self.current_stage = stage

        if total > 0:
            self.progress = current / total

        if current % 10 == 0 or current == total:

            print(f"[{stage}] {current}/{total}")