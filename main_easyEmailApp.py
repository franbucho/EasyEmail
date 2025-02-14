import resend

resend.api_key = "re_BAWe59Zi_AQnY4fo747YfCyG13pUNnWoK"

response = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": ["franciscovillahermosa@gmail.com"],
    "subject": "Hola desde Resend",
    "html": """
        <div style="font-family: Arial, sans-serif; text-align: center; padding: 20px; background-color: #f9f9f9;">
            <h1>🚀 ¡Correo Importante! (O tal vez no) 😂</h1>
            <p>¡Hola! Te escribo porque me dijeron que si no envío este email, 
            un programador en alguna parte del mundo escribirá código sin comentarios.</p>
            <p><strong>Y eso sería una tragedia. 😱</strong></p>
            <img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" alt="GIF gracioso" width="300"/>
            <p>Así que aquí estamos, salvando al mundo un correo a la vez. 🦸‍♂️</p>
            <p><em>(Responde a este mail si te reíste, de lo contrario, 
            pagarás con 10 años de debugging sin Stack Overflow.)</em> 😂</p>
            <p>Saludos,</p>
            <p><strong>Tu amigo que no quiere bugs 🐞</strong></p>
        </div>
    """
})

print(response)
