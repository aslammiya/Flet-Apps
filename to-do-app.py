import flet as ft

class ToDo(ft.UserControl):
    def build(self):
        self.Addtask = ft.TextField(hint_text="Add a new task", expand=True)
        self.task_viwe = ft.Column()

        return ft.Column(
            width=600,
            controls=[
            ft.Row(
                controls = [
                    self.Addtask,
                    ft.FloatingActionButton(icon=ft.icons.ADD,on_click=self.add_clicked),
                    ],
                ),
                self.task_viwe,
            ],
        )

    def add_clicked(self, e):
        self.task_viwe.controls.append(ft.Checkbox(label=self.Addtask.value))
        self.Addtask.value = ""
        self.update()

def main(page: ft.Page):
    page.title = "TO DO APP"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = ToDo()

    page.add(todo)




ft.app(target=main, view=ft.AppView.WEB_BROWSER)
