import tkinter as tk
from tkinter import messagebox
import resend

# Configuración de la API de Resend
resend.api_key = "re_BAWe59Zi_AQnY4fo747YfCyG13pUNnWoK"

# Función para enviar el correo
def send_email():
    subject = subject_entry.get()
    body = body_text.get("1.0", "end-1c")

    try:
        # Determinar si es HTML o texto plano
        if use_html.get():
            body = f"""
                <div style="font-family: Arial, sans-serif; color: white; background-color: #1c1c1c; padding: 20px;">
                    <h1 style="color: #f1f1f1;">{subject}</h1>
                    <p style="color: #bbb;">{body}</p>
                </div>
            """

        response = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": ["franciscovillahermosa@gmail.com"],  # Cambia el destinatario si es necesario
            "subject": subject,
            "html": body if use_html.get() else body  # Mandar texto o HTML dependiendo de la opción
        })
        messagebox.showinfo("Éxito", "Correo enviado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al enviar el correo: {e}")

# Cambiar el modo de texto
def toggle_html():
    if use_html.get():
        body_text.config(state=tk.NORMAL, fg="black", bg="white")  # Habilitar texto HTML
    else:
        body_text.config(state=tk.NORMAL, fg="white", bg="#3A3F49")  # Habilitar texto plano

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Envío de Correos")
root.geometry("360x550")  # Ajustada para un tamaño más compacto
root.config(bg="#2C2F3D")  # Fondo oscuro

# Título
title_label = tk.Label(root, text="Envía tu correo", font=("Arial", 18), fg="white", bg="#2C2F3D")
title_label.pack(pady=20)

# Campo para el asunto
subject_label = tk.Label(root, text="Asunto:", font=("Arial", 12), fg="white", bg="#2C2F3D")
subject_label.pack(pady=5)

subject_entry = tk.Entry(root, font=("Arial", 12), width=40, bd=0, relief="flat", bg="#3A3F49", fg="white")
subject_entry.pack(pady=10)

# Campo para el cuerpo del correo
body_label = tk.Label(root, text="Cuerpo del correo:", font=("Arial", 12), fg="white", bg="#2C2F3D")
body_label.pack(pady=5)

body_text = tk.Text(root, font=("Arial", 12), width=40, height=6, bd=0, relief="flat", bg="#3A3F49", fg="white")
body_text.pack(pady=10)

# Botón para cambiar entre texto plano y HTML
use_html = tk.BooleanVar(value=False)  # Valor por defecto, texto plano

html_button = tk.Checkbutton(root, text="Modo HTML", variable=use_html, bg="#2C2F3D", fg="white", font=("Arial", 12), command=toggle_html)
html_button.pack(pady=5)

# Botón para enviar el correo
send_button = tk.Button(root, text="➡️", font=("Arial", 14), command=send_email, bg="#4CAF50", fg="white", relief="flat", width=10)
send_button.pack(pady=20)

# Iniciar la aplicación
root.mainloop()
