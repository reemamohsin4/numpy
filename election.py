import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print total_ceballos

percentage_ceballos = 100*total_ceballos/len(survey_responses)
print percentage_ceballos

possible_surveys = 1.0*np.random.binomial(len(survey_responses),0.54,size=10000)/len(survey_responses)

plt.hist(possible_surveys,range=(0,1),bins=20)
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys<0.5)
print ceballos_loss_surveys

large_survey = 1.00*np.random.binomial(7000,0.54,size=10000)/7000.0

ceballos_loss_new = np.mean(large_survey<0.5)
print ceballos_loss_new
#This experiment shows that a larger survey would yield results more true to reality i.e. Ceballos would win in the survey polls as well
#I would advise my supervisors that in order to get a more accurate prediction of election results, a survey of a larger sample of the population is necessary. 

