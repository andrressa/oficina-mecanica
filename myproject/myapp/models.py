from djongo import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"

class OrdemServico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    descricao = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"OS {self.id} - {self.status}"
