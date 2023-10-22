from shiny import App, ui
import pygwalker as pyg

from datasets import load_dataset

# load dataset
dataset = load_dataset("gradio/NYC-Airbnb-Open-Data", split="train")
df = dataset.to_pandas()

app_ui = ui.page_fluid(
    ui.h1("Using pygwalker with Shiny"),
    ui.markdown("This is a demo of using [pygwalker](https://github.com/Kanaries/pygwalker) with Shiny."),
    ui.HTML(pyg.walk(df, spec="./viz-config.json", return_html=True, debug=False)),
)


def server(input, output, session):
    ...


app = App(app_ui, server)
