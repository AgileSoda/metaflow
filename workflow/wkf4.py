from metaflow import FlowSpec, step
from wkf4_case1_mod1 import Workflow4_case1_mod1
from wkf4_mod2 import Workflow4_mod2

# 상품 메타 구축 파이프라인
class Workflow4(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'   
        self.next(self.wkf4_mod1)

    @step
    def wkf4_mod1(self):
        print('this step is wkf4_mod1')
        obj = Workflow4_case1_mod1()
        obj.run()
        self.next(self.wkf4_mod2)
        
    @step
    def wkf4_mod2(self):
        print('this step is wkf4_mod2')
        obj = Workflow4_mod2()
        obj.run()
        # self.obj.start()
        self.next(self.end)
        
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow4()