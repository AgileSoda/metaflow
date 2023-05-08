from metaflow import FlowSpec, step

# ready-made 페르소나 구축을 위해 각 페르소나별 특성 저장
class Workflow2_mod1(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read file (age, sex, job, address, etc..)
        print('this step is read')
        self.next(self.preprocess)
        
    @step
    def preprocess(self):
        # scaling
        print('this step is preprocess')
        self.next(self.preprocess2_model, self.skip)
        
    @step
    def preprocess2_model(self):
        # 군집화 필요한 변수 선택 ( select address )
        # k-means clustering
        print('this step is preprocess2_model')
        self.x = 'preprocess2_model_var'
        self.next(self.join)
        
    @step
    def skip(self):
        # metaflow 작동을 위해 추가됨
        print('this step is skip')
        self.x = 'skip_var'
        self.next(self.join)
        
    @step
    def join(self,inputs):
        # metaflow 작동을 위해 추가됨
        print('this step is skip')
        print(inputs.preprocess2_model.x)
        print(inputs.skip.x)
        self.next(self.execute)
    
    @step
    def write(self):
        # write file (cluster features)
        print('this step is write')
        self.next(self.end)   
            
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow2_mod1()