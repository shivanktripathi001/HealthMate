import streamlit as st
from views.home import home
from views.login import render as login_render
from views.signup import render as signup_render
from views.symptom_checker import render as symptom_render
from views.remedies import render as remedy_render
from views.appointment import render as appointment_render
from views.feedback import render as dashboard_render
home()                                                               