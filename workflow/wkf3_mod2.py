from metaflow import FlowSpec, step

# [멀티 페르소나 메타 테이블]에서 [고객 스토리 멀티 페르소나 매핑 테이블] 만드는 흐름
class Workflow3_mod2(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read DB (멀티 페르소나 메타 테이블)
        print('this step is read')
        self.next(self.preprocess)
    
    @step
    def preprocess(self):
        # combination by 멀티페르소나 id
        print('this step is preprocess')
        self.next(self.execute)
        
    @step
    def execute(self):
        # delete DB (고객 스토리 멀티 페르소나 매핑 테이블)
        print('this step is execute')
        self.next(self.write)
    
    @step
    def write(self):
        # write DB (고객 스토리 멀티 페르소나 매핑 테이블)
        print('this step is write')
        self.next(self.end)
    
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow3_mod2()