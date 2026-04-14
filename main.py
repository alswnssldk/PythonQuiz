import json

class Quiz:
    def __init__(self, question, options, answer_idx):
        self.question = question
        self.options = options
        self.answer_idx = answer_idx

    def to_dict(self):
        return {
            "question":self.question, 
            "options":self.options, 
            "answer_idx":self.answer_idx
            }
            
    @classmethod
    def from_dict(cls, data):
        return cls(data['question'], data["options"], data["answer_idx"])

def create_defult_quizzes():
    return [
        Quiz("~~~~",["-","-","-"], 2),
        Quiz("~~~~",["-","-","-"], 2),
        Quiz("~~~~",["-","-","-"], 2),
        Quiz("~~~~",["-","-","-"], 2),
        Quiz("~~~~",["-","-","-"], 2)
    ]

class QuizGame:
    def __init__(self, file_path="state.json"):
        self.file_path = file_path
        self.quizzes = self.load_state()

    def load_state(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data_list = json.load(f)
                return [Quiz.from_dict(d) for d in data_list]

        except (FileNotFoundError, json.JSONDecodeError):
            #파일 없음 / JSON오류
            default_quizzes = create_defult_quizzes()
            self.save_state(default_quizzes)
            return default_quizzes


    def save_state(self, quizzes=None):
        target_data = quizzes if quizzes is not None else self.quizzes
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                #Quiz객체를 -> dict로 변경
                json_data = [q.to_dict() for q in target_data]         
                json.dump(json_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"save error: {e}")

# 코드 동작 테스트
if __name__ == "__main__":
    game = QuizGame()
    print(f"현재 로드된 퀴즈 수: {len(game.quizzes)}개")
    for idx, q in enumerate(game.quizzes, 1):
        print(f"{idx}. {q.question}")    

# Quiz
# - Quiz 객체
# -   
# QuizMaster
# QuizGame
