# oh boy gui time
from main import generate_visual_novel_from_wikipedia_url, generate_visual_novel_from_wikipedia_title
from nicegui import ui

dark = ui.dark_mode()
dark.enable
ui.label('Switch mode:')
ui.button('Dark', on_click=dark.enable)
ui.button('Light', on_click=dark.disable)


wikipedia_url = ui.input(label='Text', placeholder='start typing',
         validation={'Input too long': lambda value: len(value) < 1000})

def test():
    generate_visual_novel_from_wikipedia_title(wikipedia_url.value)

ui.button('Generate VN!', on_click=lambda: test())

ui.run()
