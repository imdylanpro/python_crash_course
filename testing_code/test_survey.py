# Dylan Nelson
# June 02, 2024
# test_survey.py

from survey import AnonymousSurvey

def test_store_single_response():
    '''Test that a single response to the survey is stored properly.'''
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
    
