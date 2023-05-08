from metaflow import FlowSpec, step

# Prompt 입력되면 출력 화면이 나오도록 하는 전체 흐름 
class Workflow1(FlowSpec):

    @step
    def start(self):
        self.my_var = 'start'
        print(self.my_var)
        self.next(self.read)

    @step
    def read(self):
        # read prompt (ex. 서울시 광진구 구의동에 거주하는 29살 남자)
        # read DB (NER 메타 테이블)
        print('this step is read')
        self.next(self.model)
        
    @step
    def model(self):
        # TwinDOC 활용
        # NER 결과 -> 거주지 : 광진구, 나이 : 40대, 성별 : 남
        print('this step is model')
        self.next(self.preprocess)
        
    @step
    def preprocess(self):
        # 멀티 페르소나 id 추출하는 과정 
        # NER 메타테이블에서 filter total == 3
        print('this step is preprocess')
        self.next(self.read2)
        
    @step
    def read2(self):
        # read DB
        # 화면 출력을 위한 테이블읽기 (멀티 페르소나 메타, 멀티페르소나 페르소나 매핑, 페르소나 메타, 
        #                            고객스토리 멀티 페르소나, 고객 스토리 상품 매핑, 상품 메타)
        print('this step is read2')
        self.next(self.write)
        
    @step
    def write(self):
        # write DB
        # prompt 히스토리 저장
        print('this step is write')
        self.next(self.end)
        
    @step
    def end(self):
        print('the step is end')

if __name__ == '__main__':
    Workflow1()