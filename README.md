# AIHub_Chitchat_dataset_parser

AIHub에서 공개한 한국어 multi-turn 대화 데이터셋인 [소상공인 고객 주문 질의-응답 텍스트](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=102) 데이터셋을 single-turn으로 변환 후 저장합니다. 결과는 하위 폴더에 아래와 같은 형태로 저장됩니다.
```text
AIHub_Chitchat_dataset_parser/
            ├ run.py
            ├ ...
            ├ dialogue_chatbot.tsv
            └ result/
                 ├ train.tsv
                 ├ valid.tsv
                 └ test.tsv
```
- dialogue_chatbot.tsv : single-turn으로 변환된 전체 데이터가 저장된 파일
- train/valid/test.tsv : 9:0.5:0.5로 split된 데이터가 저장된 파일


## Preprocessing
- mult-turn 데이터를 single-turn 데이터로 나눕니다.
- 토크나이저를 사용하여 토큰의 개수가 3 이하인 데이터는 버립니다. 기본으로 사용되는 토크나이저는 KoBART 토크나이저 입니다.

## Usage
```shell
Usage : python run.py
Options : 
      --tok       사용할 토크나이저의 model path, default="gogamza/kobart-base-v2"
      --data-path AIHub에서 다운받은 데이터가 저장된 경로, default="한국어 대화"
      --mode      all이면 데이터 생성 후 생성된 데이터 중 100개를 샘플링하는 작업을 모두 수행, choice=["all", "make", "sample"]
```