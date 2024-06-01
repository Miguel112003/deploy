from streamlit.web import bootstrap

script_real = "app.py"

bootstrap.run(script_real, f'run.py {script_real}', [], {})