from playwright.sync_api import sync_playwright
import streamlit as st

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    st.write(page.title())
    browser.close()
