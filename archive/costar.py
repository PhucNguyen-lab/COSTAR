import streamlit as st
import openai
import os
import json
import requests
import pandas as pd
import numpy as np
import time


if __name__ == "__main__":

  # Create a from with COSTAR framework
  st.title("COSTAR Framework")
  st.write("COSTAR is a handy template for structuring prompts")
  st.write("It considers all the key aspects that influence the effectiveness and relevance of an LLM’s response, leading to more optimal responses")
  st.write("Reference: https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41/?sk=6dcb54635c44afb6202c6e6d1f22c4ce")

  st.markdown("## Context")
  st.write("Provide background information on the task")
  context = st.text_area("Context")

  st.markdown("## Objective")
  st.write("Define what the task is that you want the LLM to perform")
  objective = st.text_area("Objective")


  st.markdown("## Style")
  st.write("Specify the writing style you want the LLM to use. Example: a professional")
  style = st.text_area("Style")
  # Multiple choice for tone with other option
  tone = st.selectbox("Tone", ["Formal", "Informal", "Persuasive", "Descriptive", "Narrative", "Empathetic", "Technical", "Conversational", "Humorous", "Serious", "Other"])
  if tone == "Other":
      # If 'Other' is selected, show a text input for the user to specify the tone
    other_tone = st.text_input("Other Tone", "sIf you selected 'Other', please specify the tone you want the LLM to use")
    if other_tone:
      tone = other_tone

  audience = st.text_area("Audience", "Identify who the response is intended for")
  response = st.text_area("Response", "Provide the response format")


  #Show the final prompt on the right side of the screen

  st.sidebar.markdown("## Final Prompt")
  st.sidebar.write("This is the final prompt that will be sent to the LLM")
  final_prompt = f"""
  Context: {context}
  Objective: {objective}
  Style: {style}
  Tone: {tone}
  Audience: {audience}
  Response: {response}
  """

  #Create a button to copy the final prompt to clipboard
  st.sidebar.code(final_prompt, language='python')