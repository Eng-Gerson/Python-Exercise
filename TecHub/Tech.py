import pandas as pd
import matplotlib.pyplot as plt
def Task1():
    #Tabular data
    data = {
        "name": ["Alice", "Bob", "Carol", "David"],
        "age": [21, 25, 23, 30],
        "city": ["Maputo", "Milan", "Maputo", "Lisbon"],
        "score": [8, 6, 9, 7]
    }
    df = pd.DataFrame(data)
    print(df)
    return df


def Task2():
    df = Task1()
    #Line plot
    days = [1,2,3,4,5]
    temperatures = [25,27,26,29,30]
    plt.plot(days, temperatures)
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.title("Temperature over time")
    plt.show()

    #Bar chart
    students = ["April","Brian","Charles","Daisy","David"]
    scores = [4,7.4,5,8,9]
    plt.bar(students, scores)
    plt.xlabel("Student")
    plt.ylabel("Score")
    plt.title("Student scores")
    plt.show()

    #Scatter plot
    hours_studied = [1,2,3,4,5,6]
    exam_scores = [4,5,6,7,8,9]
    plt.scatter(hours_studied, exam_scores)
    plt.xlabel("Hours studied")
    plt.ylabel("Exam score")
    plt.title("Study time and exam score")
    plt.show()

    #With pandas
    plt.bar(df["name"], df["score"])
    plt.xlabel("Student")
    plt.ylabel("Score")
    plt.title("Scores from a pandas DataFrame")
    plt.show()
Task2()
