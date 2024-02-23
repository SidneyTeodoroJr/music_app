# import dependencies
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
                weight=ft.FontWeight.BOLD,
                text_align="LEFT",
                offset=ft.Offset(x=0.1, y=0.5)
            )

about_body = ft.Text(
                """ 
Linkin Park is an American rock band formed in Agoura Hills, California. The band's current lineup includes vocalist and multi-instrumentalist Mike Shinoda, guitarist Brad Delson, bassist Dave Farrell, DJ Joe Hahn and drummer Rob Bourdon, all founding members.

Linkin Park released their debut album, “Hibrid Theory,” in 2000, which became the best-selling album of 2001. It received a Grammy for Best Performance, as well as nominations for Best Rock Album and Best New Artist. Their second album, “Meteora” was ranked at the top of the Billboard 200 list. In 2003, the band was chosen by MTV2 as the sixth biggest of the music video era and also the third best band, after Oasis and Coldplay.
                """,
                size=17,
                weight=ft.FontWeight.W_500,
                text_align="JUSTIFY",
            )

members_title = ft.Text(
                "Members",
                size=25,
                color=ft.colors.SURFACE_VARIANT,
                weight=ft.FontWeight.BOLD,
                style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color=ft.colors.SURFACE_VARIANT),
                offset=ft.Offset(x=0.1, y=0.5)
            )

