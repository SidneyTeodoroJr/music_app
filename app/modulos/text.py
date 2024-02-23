import flet as ft

song_list_title = ft.Text(
                    "Your Playlist", 
                    size=25,
                    color=ft.colors.WHITE,  
                    weight=ft.FontWeight.BOLD, 
                    offset=ft.Offset(x=0, y=-0.3)
                )

about_title = ft.Text(
                "About the band",
                size=25,
                style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color=ft.colors.GREY),
                color=ft.colors.BLACK,
                weight=ft.FontWeight.BOLD,
                text_align="LEFT",
                offset=ft.Offset(x=0.1, y=0.5)
            )

about_body = ft.Text(
                """ 
Linkin Park is an American rock band formed in Agoura Hills, California. The band's current lineup includes vocalist and multi-instrumentalist Mike Shinoda, guitarist Brad Delson, bassist Dave Farrell, DJ Joe Hahn and drummer Rob Bourdon, all founding members.
                """,
                size=17,
                color=ft.colors.BLACK45,
                weight=ft.FontWeight.W_500,
                text_align="JUSTIFY",
            )

members_title = ft.Text(
                "Members",
                size=25,
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
                style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color=ft.colors.WHITE),
                offset=ft.Offset(x=0.1, y=0.5)
            )

