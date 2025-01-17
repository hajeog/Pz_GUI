
Python 기반 GUI를 이용한 >>독감 예측도 계산 프로그램<<

독감 양성 음성 진단 키트에서는 민감도, 특이도가 존재한다.
민감도 = 실제 병에 걸려있는 환자에게 양성이나오는 비율
특이도 = 병에 걸리지 않은 건강한 사람에게 음성이 나오는 비율
참고_ 국내 자가검진키드(민감도90/특이도99 이상)

하지만 민감도와 특이도는 실제 병에 걸려있는 상태, 혹은 병에 걸려있지 않은 상태인 것을 확신해야 하지만, 일반적인 상황에서는 의심 환자가 참고할 만한 수치는 아니다.

만약 몸이 아파서 자가검진키트로 '음성'이 나왔을시 해당 음성 비율을 신뢰할수 있는지에대한 의문이 생기기 쉽다. 반대의 경우도 마찬가지다.

우리는 이러한 문제점을 해결하기 위해 양성 예측(양성=실제 양성)/ 음성 예측(음성= 실제 음성)확률을 구하여 사용자들에게 확실한 수치를 보여주기 위함이다.

이를 위해서는 위에서 설명한 민감도, 특이도 수치가 필요하고 발생률 수치도 필요하다.


양성예측(ppv) : 검사결과 양성 -> 실제 환자
음성예측(NPV) : 검사결과 음성 -> 정상

1. 양성예측도
양성예측도의 조건부 확률을 이용한 수식은 이러하다

양성예측 = P(실제환자 | 검사결과 양성)
        = P(환자 ∩ 검사결과 양성)/P(검사결과 양성) *이때 통계의 전체확률 법칙을 이용하여 분자분모를 분해한다 (환자인데 양성일 확률 / 정상인데 양성일 확률)

        =P(환자) X P(검사결과 양성 | 환자) / P(환자) X P(검사결과 양성) + P(환자<여집합>) X P(검사결과 양성 | 환자<여집합>)

2. 음성예측도 
양성 예측과 동일한 방식으로 진행된다.

음성예측 = P(정상 | 검사결과 음성) 계산은 양성과 동일하다
        = P(1 - 유병률)*(특이도) / (1 - 유병률)*(특이도)+(유병율)(1 - 특이도)