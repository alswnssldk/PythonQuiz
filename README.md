# [Python Quiz Game]

1. 프로젝트 개요 및 주제 선정 이유
객체 지향 설계를 적용하여 데이터 보존 및 예외 처리가 구현된 퀴즈 게임입니다.
간단한 야구 규칙이나 상식을 퀴즈를 통해 쉽고 재미있게 익히게 하고자 선정했습니다.

## 2. 실행 화면 (Screenshots)

[메인 메뉴가 띄워진 이미지]
[정답/오답을 맞추는 화면]
[기록이 갱신되는 화면]

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