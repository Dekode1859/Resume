import flet
from flet import (
    Page,
    Column,
    Row,
    alignment,
    padding ,
    ResponsiveRow,
    border,
    Container ,
    Text,
    Icon,
    LinearGradient,
    PopupMenuButton,
    PopupMenuItem,)
import flet_fastapi

async def  main(page: Page):
    page.title = "Portfolio Website"
    
    def _change_text_color_on_hover(e):
        if e.control.content.color == "#FFFFFF":
            e.control.content.color = "#000000"
            e.control.content.update()
        else:
            e.control.content.color = "#FFFFFF"
            e.control.content.update()
    
    async def on_resize(e):
        # print(page.width)
        if page.width <=350:
            _nav_bar.controls[0].visible = False
            await _nav_bar.update_async()
            _min_nav.visible = True
            await _min_nav.update_async()
        else:
            _nav_bar.controls[0].visible = True
            await _nav_bar.update_async()
            _min_nav.visible = False
            await _min_nav.update_async()
    
    _nav_bar = Row(
        alignment="end",
        controls = [
            Container(
                padding = padding.only(left=20,right=20),
                border_radius= 10,
                bgcolor="#159FAF",
                # width=64,
                height=86,
                margin=-10,
                content=Row(
                    controls=[
                        Container(
                            content = Text(
                            "About Me",
                            size = 16,
                            weight="w500",
                            color="#FFFFFF",
                            ),
                            on_hover = lambda e: _change_text_color_on_hover(e),
                        ),
                        Container(
                            content = Text(
                            "Experience",
                            size = 16,
                            weight="w500",
                            color="#FFFFFF",
                            ),
                            on_hover = lambda e: _change_text_color_on_hover(e),
                        ),
                        Container(
                            content = Text(
                            "Projects",
                            size = 16,
                            weight="w500",
                            color="#FFFFFF",
                            ),
                            on_hover = lambda e: _change_text_color_on_hover(e),
                        ),
                        Container(
                            content = Text(
                            "Contact",
                            size = 16,
                            weight="w500",
                            color="#FFFFFF",
                            ),
                            on_hover = lambda e: _change_text_color_on_hover(e),
                        ),
                    ],
                ),
            ),
        ],
    )
    
    _min_nav = Row(
        visible=False,
        controls=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="About Me"),
                    PopupMenuItem(text="Experience"),
                    PopupMenuItem(text="Projects"), 
                    PopupMenuItem(text="Contact"),
                ],
            )
        ]
    )

    
    _title = ResponsiveRow(
        controls=[
            Container(
                col = {'xs':12,'sm':12,'md':12,'lg':12,'xl':12},
                alignment=alignment.top_center,
                padding=padding.only(top=30),
                content=Text(
                    "Hi, I'm Pratik Dwivedi",
                    size=46,    
                    weight="w500",
                    # color="#000000",
                    text_align="center",
                ),
            ),
        ],
    )
    
    _main_col = Column(horizontal_alignment="center")
    _main_col.controls.append(_nav_bar)
    _main_col.controls.append(_min_nav)
    _main_col.controls.append(_title)
    # bg container
    _background = Container(
        expand=True,
        height=page.height,
        margin=-10,
        gradient=LinearGradient(
            begin = alignment.top_left,
            end = alignment.bottom_right,
            colors = ["#1E90FF","#FFFFFF"],
        ),
        content=_main_col,
    )
    
    await page.add_async(_background)
    page.on_resize = on_resize


# if __name__ == "__main__":
    # flet_fastapi.app(main)
app = flet_fastapi.app(main)
    # flet.app(main, view=flet.AppView.WEB_BROWSER, port=5000)