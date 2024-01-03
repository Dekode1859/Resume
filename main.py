import flet
from flet import (
    Page,
    Column,
    Text,
    )

def main(page: Page):
    page.bgcolor = 'red'
    page.title = "Portfolio Website"
    page.add(
        Column([
            Text("Hello World", weight="w500", size=16, color="#FFFFFF")
        ])

    )
    
    

flet.app(target=main)