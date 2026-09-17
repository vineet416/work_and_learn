import plotly.express as px
import numpy as np
from app.analysis import python_average, mathematics_average, data_science_average, overall_averages, names


# AVERAGE MARKS BY SUBJECT
def create_subject_average_chart():
    subjects = np.array(["Python", "Mathematics", "Data Science"])
    averages = np.array([python_average, mathematics_average, data_science_average])
    fig = px.bar(x=subjects, y=averages, title="Average Marks Across Subjects", labels={"x": "Subject","y": "Average Marks"},)
    return fig.to_html()


# TOP FIVE STUDENTS
def create_top_five_chart():
    top_five_indices = np.argsort(overall_averages)[-5:][::-1]
    top_five_names = names[top_five_indices]
    top_five_averages = overall_averages[top_five_indices]
    fig = px.bar(x=top_five_names, y=top_five_averages, title="Top Five Students by Overall Average", labels={"x": "Student", "y": "Overall Average"})
    return fig.to_html()