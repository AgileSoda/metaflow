from metaflow import FlowSpec, step

# 추천상품을 [고객 스토리-상품 매핑 테이블]에 넣는 흐름
class Workflow5_mod1(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read DB (스토리-멀티페르소나 매핑, 멀티페르소나-페르소나 매핑, 페르소나 메타, 상품 메타)
        # merge 해서 페르소나 해시태그 추출 해서 가져옴
        print('this step is read')
        self.next(self.preprocess)
    
    @step
    def preprocess(self):
        print('this step is preprocess')
        self.next(self.model)
        
    @step
    def model(self):
        # TwinDoc -> 스토리id별 상품 id 추출
        print('this step is model')
        self.next(self.execute)
        
    @step
    def execute(self):
        # delete DB (스토리 - 상품 매핑 테이블)
        print('this step is execute')
        self.next(self.write)
    
    @step
    def write(self):
        # write DB (스토리 - 상품 매핑 테이블)
        print('this step is write')
        self.next(self.end)  
        
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow5_mod1()