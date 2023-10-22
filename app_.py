from shiny import App, ui
import pygwalker as pyg

from datasets import load_dataset

# load dataset
# dataset = load_dataset("gradio/NYC-Airbnb-Open-Data", split="train")
# df = dataset.to_pandas()

# Part 1: ui ----
app_ui = ui.page_fluid(
    "hello",
    # ui.HTML(pyg.to_html(df))
)

# Part 2: server ----
def server(input, output, session):
    ...

# Combine into a shiny app.
# Note that the variable must be "app".
app = App(app_ui, server)
