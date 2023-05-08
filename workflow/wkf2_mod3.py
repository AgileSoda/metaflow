from metaflow import FlowSpec, step, project

# 저장된 페르소나 특성을 불러와 페르소나 id별 해시태그 생성
class Workflow2_mod3(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read file (cluster features)
        print('this step is read')
        self.next(self.preprocess)
        
    @step
    def preprocess(self):
        # prompt engineering
        print('this step is preprocess')
        self.next(self.model)
        
    @step
    def model(self):
        # chatGPT -> 페르소나 id별 해시태그 생성
        print('this step is preprocess2_model')
        self.next(self.execute)
        
    @step
    def execute(self):
        # delete DB (페르소나 메타 테이블)
        print('this step is execute')
        self.next(self.write)
    
    @step
    def write(self):
        # write DB (페르소나 메타 테이블)
        print('this step is write')
        self.next(self.end)   
            
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow2_mod3()