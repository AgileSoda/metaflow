from metaflow import FlowSpec, step

# 고객상품 집계 테이블에서 상품 메타 테이블 만드는 흐름
class Workflow4_mod2(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read DB (상품 정보 테이블)
        print('this step is read')
        self.next(self.preprocess)
    
    @step
    def preprocess(self):
        # select 상품명, 고객 프로파일 groupby 상품명
        print('this step is preprocess')
        self.next(self.execute) 
        
    @step
    def write2(self):
        # write file (상품 특징 추출 자료)
        print('this step is write2')
        self.next(self.end)  
        
    @step
    def execute(self):
        # delete DB (상품 특징 추출 자료/상품 메타 테이블)
        print('this step is execute')
        self.next(self.write)
    
    @step
    def write(self):
        # write DB (상품 특징 추출 자료/상품 메타 테이블)
        print('this step is write')
        self.next(self.write2) 

    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow4_mod2()