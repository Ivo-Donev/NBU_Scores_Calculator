import os
from prettytable import PrettyTable


def prioritize_subjects(subjects_scores):
    # Sort subjects based on scores in ascending order
    sorted_subjects = sorted(subjects_scores.items(), key=lambda x: x[1])

    # Get the three subjects with the lowest scores
    lowest_subjects = [subject for subject, score in sorted_subjects[:3]]
    return lowest_subjects


def write_to_score_file(file_number, nbu_test_score, matura_1_score, matura_2_score, final_score, needed_top_score, subjects_scores, prioritized_subjects):
    new_filename = f"Scores_{file_number}.txt"
    with open(new_filename, "w", encoding="utf-8") as file:
        file.write("Scores and Information:\n")
        file.write(f"Top Test Score: {nbu_test_score}\n")
        file.write(f"Matura 1 Score: {matura_1_score}\n")
        file.write(f"Matura 2 Score: {matura_2_score}\n")
        file.write(f"Final Score For Entering NBU: {final_score}\n")
        file.write(f"Points needed next time for the Top Test: {needed_top_score}\n")

        file.write("\nScores for Subjects:\n")
        for subject, score in subjects_scores.items():
            file.write(f"{subject}: {score}\n")

        file.write("\nSubjects that need improvement:\n")
        file.write(", ".join(prioritized_subjects))

    print(f"File '{new_filename}' created successfully.")


def nbu_calculator():
    print("Welcome to NBU score calculator, please prepare your NBU TOP score and matura grades.")

    nbu_test_score = float(input("How many points did you get at the TOP test? "))
    matura_1_score = float(input("What grade did you get at the first matura test? "))
    matura_2_score = float(input("What grade did you get at the second matura test? "))

    matura_score = ((matura_1_score + matura_2_score) / 2) - 2
    matura_score_for_nbu = (75 * matura_score)
    final_score = round((7 * nbu_test_score) + matura_score_for_nbu)

    score_table = PrettyTable()
    score_table.add_column("Top Test Score", [nbu_test_score])
    score_table.add_column("Matura 1 Score", [matura_1_score])
    score_table.add_column("Matura 2 Score", [matura_2_score])
    score_table.add_column("Final Score For Entering NBU", [final_score])

    print(score_table)

    answer = input("Are you satisfied with your scores? Will it be enough? ").lower()

    if answer == "no":
        needed_score = int(input("And how many overall points do you need/want to have? "))
        points_after_calculation = (needed_score - matura_score_for_nbu)
        needed_top_score = int(points_after_calculation / 7)

        score_table.add_column("Points you need next time you do the Top Test", [needed_top_score])
        print(score_table)

        subjects = ["Бълг.", "Лит.", "Ист.", "Георг.", "Матем.", "Физ.", "Хим.", "Биол.", "Разс.", "Сем."]
        subjects_scores = {}

        for subject in subjects:
            subject_score = input(f"Enter the score for {subject}: ")
            subjects_scores[subject] = subject_score

        prioritized_subjects = prioritize_subjects(subjects_scores)
        print(f"Prioritize studying the following subjects: {', '.join(prioritized_subjects)}")

        # Find the latest numbered Scores file in the directory
        current_dir = os.getcwd()
        existing_files = [f for f in os.listdir(current_dir) if f.startswith("Scores_") and f.endswith(".txt")]

        if existing_files:
            latest_number = max(int(file.split("_")[1].split(".")[0]) for file in existing_files)
            new_file_number = latest_number + 1
        else:
            new_file_number = 1

        # Write scores and information to the file
        write_to_score_file(new_file_number, nbu_test_score, matura_1_score, matura_2_score, final_score, needed_top_score, subjects_scores, prioritized_subjects)

    else:
        print("Have a great time in NBU next year then!")


# Run the program
nbu_calculator()
input()
