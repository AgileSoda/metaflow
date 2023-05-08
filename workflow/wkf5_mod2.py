from metaflow import FlowSpec, step

# 이력상품을 [고객 스토리-상품 매핑 테이블]에 넣는 흐름
class Workflow5_mod2(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read DB for 멀티 페르소나 id 추출
        # (고객상품집계 테이블, NER 메타 테이블)
        # read DB for 스토리 id, 상품 id 추출
        # 스토리 – 멀티페르소나 매핑, 멀티페르소나 – 페르소나 매핑, 페르소나 메타, 상품 메타)
        print('this step is read')
        self.next(self.execute)
    
    @step
    def execute(self):
        # delete DB (고객상품가입이력 테이블)
        print('this step is execute')
        self.next(self.write)
    
    @step
    def write(self):
        # write DB (고객상품가입이력 테이블)
        print('this step is write')
        self.next(self.read2)  
    
    @step
    def read2(self):
        # read DB (고객상품가입이력 테이블)
        print('this step is read2')
        self.next(self.execute2)
    
    @step
    def execute2(self):
        # delete DB (스토리 - 상품 매핑 테이블)
        print('this step is execute2')
        self.next(self.write2)
    
    @step
    def write2(self):
        # write DB (스토리 - 상품 매핑 테이블)
        print('this step is write2')
        self.next(self.end)  
    
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow5_mod2()