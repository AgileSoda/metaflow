from metaflow import FlowSpec, step
from wkf5_mod1 import Workflow5_mod1
from wkf5_mod2 import Workflow5_mod2

# 고객 스토리와 상품 매핑 구축 파이프라인
class Workflow5(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'   
        self.next(self.wkf5_mod1)

    @step
    def wkf5_mod1(self):
        print('this step is wkf5_mod1')
        self.obj = Workflow5_mod1()
        self.next(self.wkf5_mod2)
        
    @step
    def wkf5_mod2(self):
        print('this step is wkf5_mod2')
        self.obj = Workflow5_mod2()
        # self.obj.start()
        self.next(self.end)
        
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow5()