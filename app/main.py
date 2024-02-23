import flet as ft

# Importing the modules
from modulos.icons import *
from modulos.text import *
from modulos.membrs_list import *

def main(page:ft.Page):
    page.title="Container Collapse"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 5
    page.spacing = 10
    page.window_max_width=430 # Largura máxima
    page.window_max_height=1080 # Altura máxima
    page.scroll="auto"

    list_content = ft.Column(scroll="always")

    # And add data sample to "list_content"
    for x in range(0,25):
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
                user_avatar,
                share,
            ], alignment="spaceBetween"),
            ft.Row([
                song_list_title,
            ], alignment="center"),
            ft.Row([
                more,
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


    # Now i make collapse card container here
    about = ft.Container(
        height=300,
        padding=10,
        
        
        content=ft.Column([
            ft.Row([
                about_title
            ]),
            about_body
        ], scroll="auto")
    )

    members = ft.Container(
        bgcolor=ft.colors.BLACK,
        padding=10,
        height=900,
        
        content=ft.Column([
            ft.Row([
                members_title,
                members_icon
            ], alignment="center"),
            ft.Row([
                chester,
                mike
            ], alignment="spaceBetween"),
            ft.Row([
                kyle
            ], alignment="center"),
            ft.Row([
                joe,
                rob
            ], alignment="spaceBetween"),
            ft.Row([
                dave,
                brad
            ], alignment="center"),
            
            
        ], scroll="auto")
    )



    # Added containers
    page.add(
        ft.Column([
            ct_con
        ]),

        ft.Column([
            about
        ], scroll="auto"),

        ft.Column([
            members
        ], scroll="auto")
    )

    page.update()
ft.app(target=main)