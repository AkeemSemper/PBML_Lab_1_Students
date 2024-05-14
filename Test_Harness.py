import pandas as pd
import user_input_file
import pytest

correct_url = "https://github.com/AkeemSemper/Programming_Basics_for_ML/raw/main/course_material/labs/lab1/SAMP_SOL_responses.csv"
df_correct = pd.read_csv(correct_url)
#df_correct = pd.read_csv("SAMP_SOL_responses.csv")

#Q1
test_list_1 = df_correct[df_correct["Question"] == 1]
tests_1 = []
for index, row in test_list_1.iterrows():
    test_input = row["Input"]
    expected = row["Expected_Output"]
    tests_1.append((test_input, expected))

@pytest.mark.parametrize("test_input, expected", tests_1, ids=[f"Test {i+1}" for i in range(len(tests_1))])
def test_lab1Question1(test_input, expected):
    assert user_input_file.lab1Question1(test_input) == expected

#Q2
test_list_2 = df_correct[df_correct["Question"] == 2]
tests_2 = []
for index, row in test_list_2.iterrows():
    test_input = row["Input"]
    expected = row["Expected_Output"]
    tests_2.append((test_input, expected))

@pytest.mark.parametrize("test_input, expected", tests_2)
def test_lab1Question2(test_input, expected):
    assert user_input_file.lab1Question2(test_input) == expected