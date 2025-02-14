import tkinter as tk
from tkinter import messagebox
import resend

# Configuración de la API de Resend
resend.api_key = "API"

# Función para enviar el correo
def send_email():
    subject = subject_entry.get()
    body = body_text.get("1.0", "end-1c")

    try:
        response = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": ["franciscovillahermosa@gmail.com"],  # Cambia el destinatario si es necesario
            "subject": subject,
            "html": f"""
                <div style="font-family: Arial, sans-serif; color: white; background-color: #1c1c1c; padding: 20px;">
                    <h1 style="color: #f1f1f1;">{subject}</h1>
                    <p style="color: #bbb;">{body}</p>
                </div>
            """
        })
        messagebox.showinfo("Éxito", "Correo enviado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al enviar el correo: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Envío de Correos")
root.geometry("600x400")
root.config(bg="#1c1c1c")  # Fondo oscuro

# Título
title_label = tk.Label(root, text="Envía tu correo", font=("Arial", 20), fg="white", bg="#1c1c1c")
title_label.pack(pady=20)

# Campo para el asunto
subject_label = tk.Label(root, text="Asunto:", font=("Arial", 14), fg="white", bg="#1c1c1c")
subject_label.pack(pady=5)

subject_entry = tk.Entry(root, font=("Arial", 14), width=50)
subject_entry.pack(pady=10)

# Campo para el cuerpo del correo
body_label = tk.Label(root, text="Cuerpo del correo:", font=("Arial", 14), fg="white", bg="#1c1c1c")
body_label.pack(pady=5)

body_text = tk.Text(root, font=("Arial", 14), width=50, height=10)
body_text.pack(pady=10)

# Botón para enviar el correo
send_button = tk.Button(root, text="Enviar Correo", font=("Arial", 14), command=send_email, bg="#4CAF50", fg="white")
send_button.pack(pady=20)

# Iniciar la aplicación
root.mainloop()
