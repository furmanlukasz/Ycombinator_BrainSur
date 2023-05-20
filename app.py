import base64
import requests
import streamlit as st
import pandas as pd
import plost
from PIL import Image
import plotly.express as px
from scipy.stats import percentileofscore
from stats_import import meditation_phases


# set page to wide mode and dark theme
# st.set_page_config(layout="wide", page_title="BrainSur", page_icon=":brain:")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def autoplay_audio(file_path: str):
    # duration_seconds = librosa.get_duration(filename=file_path)

    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )
    # if delay:
    #     time.sleep(duration_seconds + 1.5)

def add_bg_from_url(image_url):
    # Download the image from the URL
    response = requests.get(image_url)
    image_data = response.content

    # Encode the image data using base64
    encoded_string = base64.b64encode(image_data)

    # Set the background image using the encoded string
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

add_bg_from_url('https://i.ibb.co/w4M8rTh/macos-big-sur.jpg')
st.title("BrainSur :brain:")

# 3 buttons in a row
col1, col2, col3, col4 = st.columns(4)

st.write("---")

if col1.button("Gallery"):
    img1, img2, img3, img4 = st.columns(4)
    img1.image('https://i.ibb.co/z52MN1r/336521860-767667991223026-3716096178740033935-n.jpg')
    img2.image('https://i.ibb.co/59tmg47/336591774-935879294120196-1810085195217107535-n.jpg')
    img3.image('https://i.ibb.co/qRwBWK2/336595154-599597758427683-5319373594229108266-n.jpg')
    img4.image('https://i.ibb.co/0qjfybc/336617838-1928161714213923-3015425846256950520-n.jpg')

    img5, img6, img7, img8 = st.columns(4)
    img5.image('https://i.ibb.co/RgcCHFH/336619576-167900139406201-2150038040840111361-n.jpg')
    img6.image('https://i.ibb.co/wcyWrWm/336623287-158443167108591-5221780258192442617-n.jpg')
    img7.image('https://i.ibb.co/d43KhBT/336637396-6307110886039515-6517113633736493418-n.jpg')
    img8.image('https://i.ibb.co/3sNNWz3/336650437-222764600412548-4863298622138483421-n.jpg')

    img9, img10, img11, img12 = st.columns(4)
    img9.image('https://i.ibb.co/wWdLZDM/IMG-1397.jpg')
    img10.image('https://i.ibb.co/sHVLvJq/IMG-1399.jpg')
    img11.image('https://i.ibb.co/tcxzMtG/IMG-1401.jpg')
    img12.image('https://i.ibb.co/YDFd9ch/IMG-1403.jpg')

    img13, img14, img15, img16 = st.columns(4)
    img13.image('https://i.ibb.co/VvKg7BT/photo-2023-03-23-21-24-10.jpg')
    img14.image('https://i.ibb.co/ZYc9PXq/photo-2023-03-23-21-24-14.jpg')
    img15.image('https://i.ibb.co/j3twH41/photo-2023-03-23-21-24-17.jpg')
    img16.image('https://i.ibb.co/W2F8G16/photo-2023-03-23-21-24-19.jpg')


if col2.button("Movies"):

    st.video('https://youtu.be/RyNUUMeZgV0')
    st.video('https://youtu.be/c6yFWVkHYZk')
    st.video('https://youtu.be/GnWIMP4iLDU')

if col3.button("About"):
    # st.video('https://youtu.be/z34Q0KDRwdk')
    st.header("About Us")
    st.markdown("BrainSur is a subscription-based app that delivers measurements, progress tracking, and clinically proven trainings for key aspects of mind functioning:")
    st.markdown("- Focus")
    st.markdown("- Stress")
    st.markdown("- Relaxation")
    st.markdown("- Mindfulness")
    st.markdown("- Happiness")

    st.markdown("We specialize in fast EEG signal analysis (under 150ms neurofeedback required for measurable results) to provide actionable insights, trainings, and progress tracking for meditation, mood improvement, and brain performance.")
    st.markdown("The wearable we use in the initial phase is an EEG cap by gtech, a Microsoft hardware partner.")

    st.header("Who We Serve")
    st.markdown("BrainSur is dedicated to a wide audience of people striving to sharpen their mental performance and improve their mental state by combating depression and stress.")
    st.markdown("For the first time, users get tangible data to answer questions like:")
    st.markdown("- Am I meditating the right way?")
    st.markdown("- Are my efforts to improve my brain work making me any better?")
    st.markdown("- Why am I feeling unhappy?")

    st.markdown("Even more importantly, BrainSur delivers recommendations and trainings where results can be measured.")
    st.markdown("To enable this, we have adapted clinically proven effective neurofeedback practices to increase focus, relaxation ability, mindfulness, and resilience to a mobile app format that can be used at home.")

    st.header("Integration and Partnerships")
    st.markdown("We aim to become a part of the health apps ecosystem.")
    st.markdown("Hence, the BrainSur app will be integrated with other important health apps to increase usability and leverage health data from:")
    st.markdown("- Apple Health")
    st.markdown("- Whoop")
    st.markdown("- Oura")
    st.markdown("- Garmin")
    st.markdown("Additionally, we will integrate with mindfulness apps such as Headspace and Calm to enable measurements for users' favorite trainings.")



bot_message = '''NeuroGPT: Hello! I hope you're doing well. Let's take a look at the results of your recent Focused Meditation neurofeedback training session.

You had a total of 60 entries in your session, with a meditation quality ranging from 0 (no meditation) to 3 (very deep focus). Here are some interesting insights and statistics from your session, as well as some advice on how to improve your meditation quality.

Overall, you demonstrated a good level of focus during your session. You reached the highest level of deep focus (3) in 9 consecutive entries, spanning from elapsed time 1.01 to 1.54 minutes.
After these deep focus moments, your meditation quality dropped to level 2 (focused) for 11 entries, followed by level 1 (a bit focused) for 5 entries. This could indicate a gradual loss of concentration, which is completely normal in meditation practice.
You then went through a period of no meditation (level 0) for 7 consecutive entries, starting from elapsed time 2.67 minutes. It's important to recognize when your mind wanders and gently bring it back to a more focused state.
During the second half of your session, you managed to improve your focus, transitioning between level 1 and 2. Toward the end, you reached level 2 in 12 consecutive entries, another great accomplishment!
To improve your meditation quality, consider trying the following suggestions:

When you notice your focus slipping, gently bring your attention back to your breath or chosen meditation object.
Try setting regular meditation intervals (e.g., every 5 minutes) to remind yourself to check in with your focus and mindfulness.
To sustain deep levels of focus, gradually increase the length of your meditation sessions, allowing your mind more time to settle into a concentrated state.
Experiment with different meditation techniques or environments to find the best fit for your personal preferences and style.
Use these insights to motivate you and remember that meditation is a skill that requires practice and patience. Keep up the good work, and you'll continue to see improvements in your ability to focus during meditation sessions. Happy meditating!'''

if col4.button("Report"):

    images = ['https://i.ibb.co/K9wszRX/bs-01.jpg',
              'https://i.ibb.co/vVQg1yk/bs-02.jpg',
              'https://i.ibb.co/QrfHgMb/bs-03.jpg',
              'https://i.ibb.co/gVmSQHj/bs-04.jpg',
              'https://i.ibb.co/ZhhqVMj/bs-05.jpg',
              'https://i.ibb.co/rGJ8v71/bs-06.jpg',
              'https://i.ibb.co/NsTCGc4/bs-07.jpg',
              'https://i.ibb.co/zXBXLTJ/bs-08.jpg',
              'https://i.ibb.co/JCVM8C3/bs-09.jpg',
              'https://i.ibb.co/dQRWjPM/bs-10.jpg',
              'https://i.ibb.co/M2bNKK3/bs-11.jpg']


    df_meditation_month = pd.read_csv('data_test/df_meditation_month_year.csv')
    df_unmelted = pd.read_csv('data_test/df_unmelted_year.csv')
    df_time_month = pd.read_csv('data_test/df_time_month_year.csv')
    df_unmelted = df_unmelted.set_index('Score')
    df_time_month = df_time_month.set_index('Day')
    a1, a2 = st.columns(2)
    a1.image(Image.open('data_test/profile_2.png'), width=350)
    # a2.markdown("""### Name: <font size="5">AWatts</font>\n #### Points: <span style='color:red'>325</span>\n  #### Bonus for daily meditation: <span style='color:red'>x5</span>""", unsafe_allow_html=True)
    a2.markdown("""#### Name: <span style='color:red'>Jan Kowalski</span> """, unsafe_allow_html=True)

    months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months_nums = ['-01-', '-02-', '-03-', '-04-', '-05-', '-06-', '-07-', '-08-', '-09-', '-10-', '-11-', '-12-']
    st.markdown('#### Daily statistics')

    sub_id = 1
    df_scores = pd.read_csv('data_test/Neurofeedback_scores_cl_norm_100.csv')
    focus_percentile = round(percentileofscore(df_scores.Focus, df_scores.loc[sub_id - 1, 'Focus'], kind='strict'))
    relax_percentile = round(percentileofscore(df_scores.Relax, df_scores.loc[sub_id - 1, 'Relax'], kind='strict'))
    mind_wandering_percentile = round(percentileofscore(df_scores.Mind_Wandering, df_scores.loc[sub_id - 1, 'Mind_Wandering'], kind='strict'))
    distraction_percentile = round(percentileofscore(df_scores.Distraction, df_scores.loc[sub_id - 1, 'Distraction'], kind='strict'))

    meditation_phases('conf_stats_all_data.csv', 512)
    df_meditation = pd.read_csv('data_test/df_meditation.csv', dtype={'States': str})
    # take all the data from dataframe instead first 100 rows
    df_meditation = df_meditation[40:]
    # df_meditation.Time=round(df_meditation.Time,2)
    df_meditation_summary = pd.read_csv('df_meditation_summary.csv', dtype={'States': str})

    # Row B
    b1, b2, b3, b4 = st.columns(4)  # add stars :star::star::star:
    b1.metric("Focus", str(round(df_scores.loc[sub_id - 1, 'Focus'])), '5', help="You scored higher than " + str(focus_percentile) + "% of users")
    b2.metric("Relax", str(round(df_scores.loc[sub_id - 1, 'Relax'])), '3', help="You scored higher than " + str(relax_percentile) + "% of users")
    b3.metric("Mind Wandering", str(round(df_scores.loc[sub_id - 1, 'Mind_Wandering'])), '-7', help="You scored higher than " + str(mind_wandering_percentile) + "% of users")
    b4.metric("Distraction", str(round(df_scores.loc[sub_id - 1, 'Distraction'])), '-3', help="You scored higher than " + str(distraction_percentile) + "% of users")

    metric_value = 42
    metric_label = "Metric Label"
    metric_text_color = "red"

    # Row C
    st.markdown('#### Meditation phases')
    c1, c2 = st.columns((7, 3))

    with c1:
        plost.event_chart(
            data=df_meditation,
            x='Time',
            y='States',
            color='States',
            legend=None, height=300)

    with c2:
        plost.pie_chart(  # donut_chart
            data=df_meditation_summary,
            theta='Counts',
            color='States', legend='right', height=300)

    # with c1:
    month_selected = 'Jan' #st.selectbox('Month', options=months)
    if month_selected:
        # filter the dfs
        idx = months.index(month_selected)
        # df_meditation_month= df_meditation_month[pd.to_datetime(df_meditation_month['Dates']).dt.month == idx+]
        tmp_df_meditation_month = df_meditation_month[df_meditation_month['Dates'].str.contains(months_nums[idx])]
        tmp_df_unmelted = df_unmelted.filter(regex=months_nums[idx])
        tmp_df_time_month = df_time_month.filter(regex=months_nums[idx])

        # shuffle the variables values
        tmp_df_unmelted = tmp_df_unmelted.sample(frac=1).reset_index()
        tmp_df_unmelted = tmp_df_unmelted.set_index('Score')
        tmp_df_time_month = tmp_df_time_month.sample(frac=1).reset_index()
        tmp_df_time_month = tmp_df_time_month.set_index('Day')

        st.markdown('##### Meditation phases')
        plost.bar_chart(
            data=tmp_df_meditation_month,
            bar='Dates',
            value='Counts', color='States', use_container_width=True
        )

        # st.markdown("##### Performance scores")
        fig = px.imshow(tmp_df_unmelted)
        config = {'displayModeBar': False}
        fig.update_xaxes(tickangle=270)
        fig.update_layout(height=180,
                          margin=dict(t=0, b=0, l=0, r=0),
                          )
        fig.update_coloraxes(colorbar={'y': 0.43})  # 'orientation':'h',
        # fig.update_coloraxes(showscale=False)
        # st.plotly_chart(fig, use_container_width=True, config=config)

        st.markdown("##### Number of daily meditations")
        fig = px.imshow(tmp_df_time_month, color_continuous_scale=px.colors.sequential.Reds)
        config = {'displayModeBar': False}
        fig.update_xaxes(tickangle=270)
        fig.update_layout(height=200,
                          margin=dict(t=0, b=0, l=0, r=0),
                          )
        fig.update_coloraxes(colorbar={'y': 0.5})
        # fig1.update_coloraxes(colorbar={'orientation':'h','y': -1.8})

        st.plotly_chart(fig, use_container_width=True, config=config)





        st.title("NeuroBot")
        st.audio('ElevenLabs_2023-05-20T10_27_53.000Z_Bella_NqBIPWYc6HSdl8RLetU8.mp3')
        # autoplay_audio('ElevenLabs_2023-05-20T10_27_53.000Z_Bella_NqBIPWYc6HSdl8RLetU8.mp3')
        st.write("NeuroGPT:", bot_message)
        for img in images:
            st.image(img, width=700, caption='NeuroGPT')
