from django.db import models
from django.contrib.auth.models import User

class Topic (models.Model):
    """Um tópico que o usuário esta aprendendo"""
    text = models.CharField(max_length=200)
    #armazena uma quantidade de texto, e informa ao django quanto espaço de ser reservado no banco de dados
    date_added = models.DateTimeField(auto_now_add=True)
    #armazena automaticamente a data e hora exata da criação de um novo topico
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #estabele uma relação de chave estrangeira com o usuario
    def __str__(self):
        """retorna uma representação de string do modelo"""
        return self.text
    
class Entry (models.Model):
    """algo especifico aprendido sobre um topico"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """retorna string simples representando a entrada"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"