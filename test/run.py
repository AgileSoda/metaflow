from metaflow import FlowSpec, step
from other_workflow import OtherWorkflow

class MainWorkflow(FlowSpec):
    @step
    def start(self):
        self.my_var = 'start'
        print('start')
        self.next(self.run_other_workflow)


    @step
    def run_other_workflow(self):
        obj = OtherWorkflow()
        obj.run()
        print('run_other_workflow')
        self.next(self.end)


    @step
    def end(self):
        print('the step is end')