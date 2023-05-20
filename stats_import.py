import numpy as np
import pandas as pd
import random
import itertools
import datetime

def meditation_phases_fromlist(path, sfreq, save_raw=True, save_summary=True):
    """
    Creates dataframe with meditation phases and corresponding time stamps and dataframe with phases relative counts in percent
    :param path: path to the txt file with meditation phases numbers
    :param sfreq: sampling frequency
    :param save_raw: whether to save dataframe with time stamps and meditation phases
    :param save_summary: whether to save dataframe with phases counts
    :return:
    df_meditation_states: dataframe containing meditation phases numbers and corresponding time stamps
    df_meditation_summary: dataframe containing percentage of the phases in the data
    """

    with open(path) as f:
        lines = f.readlines()

    states=[]
    for i in lines[0]:
        states.append(i)

    times=np.arange(1,len(states)+1)
    
    #TODO check time packets for which phases are return (now 35)
    times=(times)*35/(sfreq*60)
    
    df_meditation_states=pd.DataFrame(list(zip(times,states)),columns=['Time','States'])
    
    if save_raw:
        df_meditation_states.to_csv('df_meditation.csv',index=False)

    df_meditation_summary = df_meditation_states['States'].value_counts().rename_axis('States').reset_index(name='Counts')
    df_meditation_summary['Counts']=(df_meditation_summary['Counts']/df_meditation_summary['Counts'].sum())*100
    
    if save_summary:
        df_meditation_summary.to_csv('df_meditation_summary.csv',index=False)

    return df_meditation_states, df_meditation_summary


def meditation_phases(path, sfreq, save_raw=True, save_summary=True):
    """
    Creates dataframe with meditation phases and corresponding time stamps and dataframe with phases relative counts in percent
    :param path: path to the dataframe containing information from meditation session
    :param sfreq: sampling frequency
    :param save_raw: whether to save dataframe with time stamps and meditation phases
    :param save_summary: whether to save dataframe with phases counts
    :return:
    df_meditation_states: dataframe containing meditation phases numbers and corresponding time stamps
    df_meditation_summary: dataframe containing percentage of the phases in the data
    """
    df_states = pd.read_csv(path)
    
    # states = []
    # times = []
    # for i in range(len(df_states)):
    #     states = states+[df_states.meditation_quality_count[i]]*df_states.current_sample_len[i]
    #     times = np.arange(1,len(states)+1)
    # times=np.arange(1,len(states)+1)

    states = df_states.meditation_quality_count
    times = df_states.elapsed_time
    # times=(times)/(sfreq*60)
    
    df_meditation_states=pd.DataFrame(list(zip(times,states)),columns=['Time','States'])

    if save_raw:
        df_meditation_states.to_csv('df_meditation.csv',index=False)

    df_meditation_summary = df_meditation_states['States'].value_counts().rename_axis('States').reset_index(name='Counts')
    df_meditation_summary['Counts']=(df_meditation_summary['Counts']/df_meditation_summary['Counts'].sum())*100
    
    if save_summary:
        df_meditation_summary.to_csv('df_meditation_summary.csv',index=False)

    return df_meditation_states, df_meditation_summary


def simulate_year_phases(change_labels=True, save=True):
    """
    Returns simulated percentage of meditation phases per each month in a year based on states names
    :param df_meditation_summary: dataframe containing percentage of the phases in the data
    :param save: whether to save dataframe or not
    :return:
    df_meditation_month:n dataframe with simulated percentage of meditation phases per each month in a 2023 year
    """
    states_sum=[]
    for i in range(365):
        first_state=random.randrange(74,86)
        second_state=random.randrange(10,100-first_state-1)
        third_state=random.randrange(1,100-first_state-second_state)
        zero_state=100-first_state-second_state-third_state

        states=[first_state,second_state,third_state,zero_state]
        
        states_sum=states_sum+states
        # print(states_sum)

    states=['1','2','3','0']*365

    # initializing date
    test_date = datetime.datetime.strptime("01-1-2023", "%d-%m-%Y")
    
    # initializing K
    K = 365
    
    date_generated = pd.date_range(test_date, periods=K)
    dates=list(itertools.chain.from_iterable(itertools.repeat(x, 4) for x in list(date_generated.strftime("%d-%m-%Y"))))
    # dates=date_generated.strftime("%d-%m-%Y")


    df_meditation_month=pd.DataFrame(list(zip(dates,states,states_sum)),columns=['Dates','States','Counts'])
    
    if change_labels:
        df_meditation_month['States']=df_meditation_month['States'].map({'3':'3rd: Deep','2':'2nd: Medium','1':'1st: Weak','0':'0: None'})

    if save:
        df_meditation_month.to_csv('df_meditation_month_sessions_year.csv',index=False)

    return df_meditation_month



def simulate_year_stats(path, save=True):
    """
    Simulate Distraction, Focus, Wandering and Relax score for each day in a year

    :param path: path to Neurofeedback_scores_cl_norm_100.csv containing 4 stats score values for subjects from eegbci_data mne dataset
    :return:
    df_unmelted: dataframe containing simulated scores for Distraction, Focus, Wandering and Relax for each day in a year
    """
    
    test_date = datetime.datetime.strptime("01-1-2023", "%d-%m-%Y")
    K = 365
    date_generated = pd.date_range(test_date, periods=K)
    months=date_generated.strftime("%d-%m-%Y")

    df_scores_month=pd.read_csv(path)
    df_scores_month=df_scores_month.loc[df_scores_month.index.repeat(4)]
    df_scores_month=df_scores_month.iloc[20:385,:]
    df_scores_month['Dates']=months
    df_scores_month=df_scores_month.drop(columns=['subject'])
    df_scores_month=df_scores_month.reset_index(drop=True)
    df_scores_month=df_scores_month.melt(id_vars=['Dates'], var_name='Score')

    df_unmelted=df_scores_month.pivot(index='Score',columns='Dates')
    df_unmelted = df_unmelted['value'].reset_index()
    df_unmelted.Score=['Dis','Foc','Wan','Rel']
    df_unmelted.columns.name = None
    df_unmelted=df_unmelted.set_index('Score')

    if save:
        df_unmelted.to_csv('df_unmelted_year.csv')

    return df_unmelted

def simulate_year_entries(save=True):
    """
    Simulate entries (number of meditation sessions) each day in a year

    :return:
    df_time_month: dataframe containing simulated umber of times user meditated each day in a year
    """

    test_date = datetime.datetime.strptime("01-1-2023", "%d-%m-%Y")
    K = 365
    date_generated = pd.date_range(test_date, periods=K)
    months=date_generated.strftime("%d-%m-%Y")

    datas = np.round(np.random.lognormal(mean=0.2, sigma=0.5, size=365*7))
    indices_time=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    
    df_time_month = pd.DataFrame(np.array(datas).reshape(7,365),columns=list(months), index=indices_time) 
    df_time_month.index.name = 'Day'

    if save:
        df_time_month.to_csv('df_time_month_year.csv')


