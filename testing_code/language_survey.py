# Dylan Nelson
# June 2, 2024
# language_survey.py

from survey import AnonymousSurvey

# Define a question then make a survey using the AnonymousSurvey class from 
# "survey.py".
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question and store responses to the question.
language_survey.show_question()
print('Enter "q" at any time to quit.')
while True:
    response = input(f"Language: ")
    if response.lower() == 'q':
        break
    language_survey.store_response(response)

# Show the results of the survey
print("\nThank you to everyone that participated in the survey.")
language_survey.show_results()
