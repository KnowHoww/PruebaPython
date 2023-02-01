import flet as ft
 
 
 
def main(page: ft.Page):
    
    
	page.vertical_alignment="center"
	page.bgcolor="#d4e6f1"
    


	def ganti(e):
		ctx.bgcolor = "white"
		ctx.height = 400 
		ctx.width = 400 
		ctx.border_radius = 20 		
 
		register_btn.value = "BOT ACTIVACION MOVIL"
		
 
		txt_box_register.visible = True 
 
 
		page.update()
 
	txt_box_register = ft.Container(
		content=ft.Column([
            ft.Text(value="BOT ACTIVACION MOVIL",
				color="black"
				),
			ft.TextField(label="User GAC",
				border_color="#81F7F3",
				color="white"
				),
			ft.TextField(label="Password GAC",
				border_color="#81F7F3",
				color="white"
				),
			ft.ElevatedButton("Ingresar",
				width=page.window_width,
				# on_click=ganti
 
				),
            ft.Text(value="C Atento RPA, Yamid Rodriguez",
				color="black"
				),
 
			])
 
		)
 
	txt_box_register.visible = False

	register_btn = ft.ElevatedButton("Ingresar",
		on_click=ganti,
 
		)
 
	ctx = ft.Container(
		border_radius=100,
		padding=20,
		width=200,
		alignment=ft.alignment.center,
		height=150,
		content=ft.Column([
			txt_box_register,
			register_btn
			])
		)
 
 
	page.add(
		ctx
		)
 
ft.app(target=main)