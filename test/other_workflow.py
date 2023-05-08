from metaflow import FlowSpec, step

class OtherWorkflow(FlowSpec):
    @step
    def start(self):
        self.my_var = 'start'
        self.next(self.end)

    @step
    def end(self):
        print('the step is end')