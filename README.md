# [Python Quiz Game]

1. 프로젝트 개요 및 주제 선정 이유

객체 지향 설계를 적용하여 데이터 보존 및 예외 처리가 구현된 퀴즈 게임입니다.

간단한 야구 규칙이나 상식을 퀴즈를 통해 쉽고 재미있게 익히게 하고자 선정했습니다.

## 2. 실행 화면 (Screenshots)

2-1. 메뉴
<img width="295" height="238" alt="menu" src="https://github.com/user-attachments/assets/7dc6661b-c441-4a46-a233-046ed642aa83" />

2-2. 퀴즈
<img width="220" height="251" alt="quiz" src="https://github.com/user-attachments/assets/314ded86-ca0a-4564-9459-29a4b7de3a92" />

2-3. 최고 점수 저장
<img width="217" height="136" alt="max_score_save" src="https://github.com/user-attachments/assets/c3e12509-e099-49b1-9867-28b170e876a7" />

2-4. 일반종료
<img width="292" height="257" alt="init 0" src="https://github.com/user-attachments/assets/ec10b344-3071-47ae-a002-00b6732b9d94" />

2-5. 예외처리 종료
<img width="296" height="289" alt="C + c" src="https://github.com/user-attachments/assets/e69a2dac-9b1a-4945-aaae-ff056a0d41ee" />



3. 주요 기능
퀴즈 풀기: 등록된 문제 풀이 및 정답 확인

퀴즈 추가: 새로운 문제/보기/정답 입력 및 즉시 저장

목록 보기: 현재 등록된 전체 문제 리스트 확인

점수 확인: 역대 최고 정답 개수(Best Score) 출력

안전 종료: 5번 선택 혹은 Ctrl+C 종료 시 최신 상태 자동 저장

4. 파일 구조 및 데이터 설명
Class
 - Quiz
  - to_dict
  - from_dict(@classmethod)
 - QuizGame
  - load_state
  - save_state
  - Display_menu
  - list_quiz
  - max_score
  - play_quiz
  - add_quiz
  - run
