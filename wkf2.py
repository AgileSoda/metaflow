from metaflow import FlowSpec, step
from wkf2_mod1 import Workflow2_mod1
from wkf2_mod2 import Workflow2_mod2
from wkf2_mod3 import Workflow2_mod3

# 페르소나 구축 파이프라인
class Workflow2(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'   
        self.next(self.wkf2_mod1)

    @step
    def wkf2_mod1(self):
        print('this step is wkf2_mod1')
        self.obj1 = Workflow2_mod1()
        self.obj1.run()
        self.next(self.wkf2_mod2)
        
    @step
    def wkf2_mod2(self):
        print('this step is wkf2_mod2')
        self.obj2 = Workflow2_mod2()
        self.obj2.run()
        self.next(self.wkf2_mod3)
        
    @step
    def wkf2_mod3(self):
        print('this step is wkf2_mod3')
        self.obj3 = Workflow2_mod3()
        self.obj3.run()
        self.next(self.end)
        
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow2()