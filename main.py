import flet as ft



def main(page: ft.Page):
    page.theme_mode = "dark"
    page.title = "calculator IGL"
    page.window_width = 450
    page.window_height = 350
    page.window_resizable = False
    
    
    author = ft.Container (
        ft.Text(value="By: Gygole"),
        height=50,
        width=100,
        
        
        )
    
    
    
    def numb1(e):
        
        entry.value = entry.value + num1.text
        
        page.update()
        
    def numb2(e):
        
        entry.value = entry.value + num2.text
        
        page.update()
        
    def numb3(e):
        
        entry.value = entry.value + num3.text
        
        page.update()
        
    def numb4(e):
        
        entry.value = entry.value + num4.text
        
        page.update()
    
    def numb5(e):
        
        entry.value = entry.value + num5.text
        
        page.update()
        
    def numb6(e):
        
        entry.value = entry.value + num6.text
        
        page.update()
        
    def numb7(e):
        
        entry.value = entry.value + num7.text
        
        page.update()
        
    def numb8(e):
        
        entry.value = entry.value + num8.text
        
        page.update()
        
    def numb9(e):
        
        entry.value = entry.value + num9.text
        
        page.update()
        
    def numb0(e):
        
        entry.value = entry.value + num0.text
        
        page.update()
        
    def addit(e):
        
        entry.value = entry.value + addition.text
        
        page.update()
        
    def sub(e):
        
        entry.value = entry.value + subtraction.text
        
        page.update()
        
    def mult(e):
        
        entry.value = entry.value + multiplication.text
        
        page.update()
        
    def div(e):
        
        entry.value = entry.value + division.text
        
        page.update()
        
    def equ(e):
        
        final = eval(entry.value)
        
        entry.value = final
        
        page.update()
        
        
        
    def deletenum(e):
        
        entry.value = ""
        
        page.update()
        
        
    def brack1(e):
        
        entry.value = entry.value + bracket1.text
        
        page.update()
        
    def brack2(e):
        
        entry.value = entry.value + bracket2.text
        
        page.update()

    def mode(e):
        
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        
        page.update()
            
    
        
        
        
        
        
    
    entry= ft.TextField(label="Пример", width=415 )
    
    num1 = ft.ElevatedButton(text="1", width=70, on_click=numb1)
    num2 = ft.ElevatedButton(text="2", width=70, on_click=numb2)
    num3 = ft.ElevatedButton(text="3", width=70, on_click=numb3)
    num4 = ft.ElevatedButton(text="4", width=70, on_click=numb4)
    num5 = ft.ElevatedButton(text="5", width=70, on_click=numb5)
    num6 = ft.ElevatedButton(text="6", width=70, on_click=numb6)
    num7 = ft.ElevatedButton(text="7", width=70, on_click=numb7)
    num8 = ft.ElevatedButton(text="8", width=70, on_click=numb8)
    num9 = ft.ElevatedButton(text="9", width=70, on_click=numb9)
    num0 = ft.ElevatedButton(text="0", width=70, on_click=numb0)
    
    addition = ft.ElevatedButton(text="+", width=70, on_click=addit)
    
    subtraction = ft.ElevatedButton(text="-", width=70, on_click=sub)
    
    multiplication = ft.ElevatedButton(text="*", width=70, on_click=mult)
    
    division = ft.ElevatedButton(text="/", width=70, on_click=div)
    
    equally = ft.ElevatedButton(text="=", width=150, on_click=equ)
    
    bracket1 = ft.ElevatedButton(text="(", width=70, on_click=brack1)
    
    bracket2 = ft.ElevatedButton(text=")", width=70, on_click=brack2)
    
    delete = ft.ElevatedButton(text="delete", width=150, on_click=deletenum)
    
    theme = ft.ElevatedButton(text="theme mode", width=150, on_click=mode)
    
    
        
    page.add (ft.Row ( 
        [
        entry
        ]
    )
    )
    
    page.add (ft.Row ( 
        [
        num1,
        num2,
        num3,
        delete
        
        ]
    )
    )
    
    page.add (ft.Row ( 
        [
        num4,
        num5,
        num6,
        addition,
        subtraction
        ]
    )
    )
    
    page.add (ft.Row ( 
        [
        num7,
        num8,
        num9,
        multiplication,
        division
        ]
    )
    )
    
    page.add (ft.Row ( 
        [
        num0,
        equally,
        bracket1,
        bracket2
        ]
    )
    )
    
    page.add (ft.Column ( 
        [
        theme,
        author
        ]
    )
    ) 
    
    
    
    
    
    
    
        
    
    
    page.update()
    
    
    
    
ft.app(target=main)