import flet as ft

def main(page: ft.Page):
    def clicked(e):
        if textFeild.value != "":
            task_view.controls.append(ft.Checkbox(label=textFeild.value))
            textFeild.value = ""
            page.update()

    textFeild = ft.TextField(hint_text="Add new task", expand=True)
    task_view = ft.Column()
    viwe = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    textFeild,
                    ft.FloatingActionButton(icon=ft.icons.ADD,on_click=clicked),
                ],
            ),
            task_view,
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(viwe)


ft.app(target=main)
