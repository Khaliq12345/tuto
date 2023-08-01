from playwright.sync_api import sync_playwright
import streamlit as st
import os
os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('sudo dpkg -i google-chrome-stable_current_amd64.deb')


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    st.write(page.title())
    browser.close()
