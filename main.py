import task_one
import task_two
import task_three
import task_four
import task_five
import task_six


def __checking_for_number__(message):
    while True:
        answer = input(message)
        try:
            return int(answer)
        except Exception:
            print("Введен не верный формат данных, попробуйте еще раз.")


if __name__ == '__main__':
    task_one.__task_one__()
    task_two.__task_two__()
    task_three.__task_three__()
    task_four.__task_four__()
    task_five.__task_five__()
    task_six.__task_six__()

