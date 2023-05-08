from metaflow import FlowSpec, step

# [페르소나 메타 테이블]에서 [멀티 페르소나 메타 테이블] 만드는 흐름
class Workflow3_mod1(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read DB (페르소나 메타 테이블)
        print('this step is read')
        self.next(self.preprocess)
    
    @step
    def preprocess(self):
        # combination by 페르소나 id
        # extract hashtags
        print('this step is preprocess')
        self.next(self.execute)
        
    @step
    def execute(self):
        # delete DB (멀티 페르소나 페르소나 매핑 테이블)
        print('this step is execute')
        self.next(self.write)
    
    @step
    def write(self):
        # write DB (멀티 페르소나 페르소나 매핑 테이블)
        print('this step is write')
        self.next(self.preprocess2)   
    
    @step
    def preprocess2(self):
        # prompt engineering
        print('this step is preprocess2')
        self.next(self.model)
        
    @step
    def model(self):
        # chatGPT -> make multi-persona name, story
        print('this step is model')
        self.next(self.execute2)
        
    @step
    def execute2(self):
        # delete DB (멀티 페르소나 메타 테이블)
        print('this step is execute2')
        self.next(self.write2)
    
    @step
    def write2(self):
        # write DB (멀티 페르소나 메타 테이블)
        print('this step is write2')
        self.next(self.end)  
        
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow3_mod1()