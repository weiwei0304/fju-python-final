
from quiz import tryQuiz

print("我該離職嗎？\n")
print("請依序回答問題，按照自身狀況填入數字1或2：\n")

totalScore = tryQuiz()

def load_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if (totalScore >= 2):
    print('別再撐了，離職吧！')
    data = load_text_file('quitYourJob.txt')
else:
    print('你正在遭遇轉型瓶頸，或許可以再多考慮一下～')
    data = load_text_file('betterToStay.txt')

print(data)

