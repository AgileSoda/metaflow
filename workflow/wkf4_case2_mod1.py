from metaflow import FlowSpec, step

# 상품정보 테이블/상품요약서에서 상품 메타 테이블 만드는 흐름
class Workflow4_case2_mod1(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read file (상품요약서, 약관서, etc..)
        print('this step is read')
        self.next(self.preprocess)
    
    @step
    def preprocess(self):
        # extract from file
        # 해시태그 추출을 위한 prompt engineering
        print('this step is preprocess')
        self.next(self.model)
        
    @step
    def model(self):
        # chatGPT -> 상품 해시태그 추출
        print('this step is model')
        self.next(self.execute)
        
    @step
    def execute(self):
        # delete DB (상품 메타 테이블)
        print('this step is execute')
        self.next(self.write)
    
    @step
    def write(self):
        # write DB (상품 메타 테이블)
        print('this step is write')
        self.next(self.end)  
        
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow4_case2_mod1()