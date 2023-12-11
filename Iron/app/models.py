from django.db import models

class Membro(models.Model):
    nome = models.CharField(max_length=50)
    ra = models.CharField(max_length=15)
    telefone = models.CharField(max_length=20)
    horario = models.TimeField(null=True)

    def __str__(self):
        return f'{self.nome}, {self.ra}, {self.telefone}, {self.horario}'
    
class Treinador(models.Model):
    nome = models.CharField(max_length=50)
    experiencia = models.CharField(max_length=60)
    cpf = models.CharField(max_length=25)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}, {self.experiencia}, {self.cpf}, {self.telefone}'
    
class GrupoMuscular(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'

class Exercicio(models.Model):
    nome = models.CharField(max_length=50)
    grupomuscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}, {self.grupomuscular}'

class Treinamento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return f'{self.nome}, {self.descricao}'

class Registroaula(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    treinamento = models.ForeignKey(Treinamento, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.membro}, {self.treinador}, {self.exercicio}, {self.treinamento}'
