jury_number = int(input())
presentation = input()
final_eval = 0
presentation_count = 0
while presentation != 'Finish':

    presentation_count += 1
    eval_for_presentation = 0

    for i in range(jury_number):
        evaluation = float(input())
        eval_for_presentation += evaluation

    eval_for_presentation /= jury_number
    final_eval += eval_for_presentation
    print(f'{presentation} - {eval_for_presentation:.2f}.')
    presentation = input()

final_eval /= presentation_count
print(f"Student's final assessment is {final_eval:.2f}.")