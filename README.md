# acr-dont-edit

Extensao que verifica se um arquivo que não deve ser editado, foi editado, se sim adiciona um comentario personalizado
conforme o
configurado

Arquivo config.json

```json
{
  "stage": "static",
  "rules": [
    {
      "message": "Don't edit, please",
      "regexPath": [
        ".*\/example.sql"
      ]
    }
  ]
}
```
