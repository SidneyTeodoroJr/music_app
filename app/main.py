import flet as ft

# Importing the modules
from modulos.functions import *

def main(page:ft.Page):
    page.title="Container Collapse "
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 5
    page.spacing = 10
    page.scroll = "auto"

    list_content = ft.Column(scroll="always")

    # And add data sample to "list_content"
    for x in range(0,15):
        list_content.controls.append(
            # Add listile
            ft.ListTile(
                title=ft.Text("Linkin Park", color=ft.colors.WHITE),
                subtitle=ft.Text("Alternative rock", color=ft.colors.WHITE),
                leading=ft.CircleAvatar(
                    foreground_image_url="https://w7.pngwing.com/pngs/979/599/png-transparent-linkin-park-logo-linkin-park-logo-music-band-miscellaneous-angle-emblem.png"
                ),
            ),
            # And add circle image profile
        )

    def full_mode(e):
        # And now add effect container her
        # This for full screen mode
        e.control.height = page.window_height
        e.control.width = page.window_width
        e.control.border_radius = 0

        # And show you back arrow left button here
        e.control.content.controls[0].controls[0].visible = True
        e.control.content.controls[3].visible = True

        # And hide FloatingActionButton
        e.control.content.controls[1].controls[1].visible = False
        # And you circle image position to center
        e.control.content.controls[1].alignment="center"

        # Remove Padding page and spacing
        page.padding = 0
        page.spacing = 0

        page.update()

    def back_again(e):
        # And now fo back button
        ct_con.height = 250
        ct_con.width = page.window_width
        ct_con.border_radius = 30
        ct_con.content.controls[0].controls[0].visible = False
        ct_con.content.controls[1].controls[1].visible = True
        ct_con.content.controls[1].alignment="spaceBetween"

        page.padding = 10
        page.spacing = 10

        page.update()


    # Now i make collapse card container here
    ct_con = ft.Container(
        padding=10,
        bgcolor=ft.colors.BLACK,
        border_radius=30,
        height=300,
        on_click=full_mode,

        # And add event click fif you click this container

        animate=ft.animation.Animation(500, "easeInOut"), # You can add animation this container here
        content=ft.Column([
            ft.Row([
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                    icon_size=30,
                    icon_color=ft.colors.WHITE,
                    # And button click to back
                    on_click=back_again,
                    visible=False, # And hire this button back
                )
            ]),
            ft.Row([
                # And create circle avatar profile image
                ft.CircleAvatar(
                    foreground_image_url="https://avatars.githubusercontent.com/u/91035485?v=4"
                ),
                ft.Markdown()
            ], alignment="spaceBetween"),
            ft.Row([
                ft.Text("Your Playlist", color=ft.colors.WHITE, size=25, weight=ft.FontWeight.BOLD, offset=ft.Offset(x=0, y=-0.3)),
            ], alignment="center"),
            ft.Row([
                ft.IconButton(icon=ft.icons.KEYBOARD_DOUBLE_ARROW_DOWN, icon_color=ft.colors.WHITE, icon_size=30, tooltip="More", offset=ft.Offset(x=0, y=-0.5)),
            ], alignment="center"),

            # And show you list title here
            ft.Row([
                ft.Container(
                    padding=10,
                    content=ft.Column([
                        list_content,
                    ], scroll="auto")
                )
            ])
        ], scroll="auto")
    )

    page.add(
        ft.Column([
            ct_con
        ], scroll="auto"),
    )


    page.update()
ft.app(target=main)