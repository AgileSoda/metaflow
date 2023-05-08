from metaflow import FlowSpec, step
from wkf3_mod1 import Workflow3_mod1
from wkf3_mod2 import Workflow3_mod2

# 페르소나 구축 파이프라인
class Workflow3(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'   
        self.next(self.wkf3_mod1)

    @step
    def wkf3_mod1(self):
        print('this step is wkf3_mod1')
        self.obj = Workflow3_mod1()
        self.next(self.wkf3_mod2)
        
    @step
    def wkf3_mod2(self):
        print('this step is wkf3_mod2')
        self.obj = Workflow3_mod2()
        # self.obj.start()
        self.next(self.end)
        
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow3()