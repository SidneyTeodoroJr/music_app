import flet as ft

# And create circle avatar profile image
user_avatar = ft.CircleAvatar(
                foreground_image_url="https://avatars.githubusercontent.com/u/91035485?v=4"
            )

share = ft.IconButton(
            icon=ft.icons.SHARE, icon_color=ft.colors.WHITE, icon_size=30, tooltip="Share"
        )

more = ft.IconButton(
        icon=ft.icons.KEYBOARD_DOUBLE_ARROW_DOWN, 
        icon_color=ft.colors.WHITE, 
        icon_size=30, 
        tooltip="More", 
        offset=ft.Offset(x=0, y=-0.5)
    )

members_icon = ft.IconButton(
            icon=ft.icons.LIBRARY_MUSIC_OUTLINED, icon_color=ft.colors.WHITE, icon_size=30, tooltip="Share",
            offset=ft.Offset(x=0, y=0.3)
        )