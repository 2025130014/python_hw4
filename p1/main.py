def increase_fail_count(current_cnt, limit=5):
    current_cnt += 1
    if current_cnt >= limit:
        print("Fail")
        exit()
    else:
        print("Check again")
        return current_cnt
PASSWORD = "Aerospace"
fail_count = 0

while True:
    user_input = input()
    if user_input == PASSWORD:
        print("LOGIN")
        break
    else:
        fail_count = increase_fail_count(fail_count)
