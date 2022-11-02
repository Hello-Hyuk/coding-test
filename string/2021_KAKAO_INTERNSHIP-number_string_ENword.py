num_dict = ["zero","one","two","three","four","five","six","seven","eight","nine"]
def solution(s):
    answer = s
    for num in enumerate(num_dict):
        answer = answer.replace(num[1],str(num[0]))
    return int(answer)

### my code
def my_solution(s):
    num_dict = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
    }
    answer = []
    tmp = ""
    ans = ""
    for i in s:
        try:
            answer.append(int(i))
        except ValueError:
            tmp += i
            if tmp in num_dict:
                answer.append(int(num_dict.get(tmp)))
                tmp = ""
    for i in answer:
        ans += str(i)

    return int(ans)