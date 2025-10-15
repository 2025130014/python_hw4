def increase_fail_count(current_cnt, limit=5):
    current_cnt += 1
    if current_cnt >= limit:
        print("Fail")
        exit()  
    else:
        print("Check again")
        return current_cnt
def login_system(password="Aerospace"):
    fail_count = 0
    while True:
        user_input = input()
        if user_input == password:
            print("LOGIN")
            break
        else:
            fail_count = increase_fail_count(fail_count)
def main():
    login_system()
main()
