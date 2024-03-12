from django.db import models

# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class TipoPessoa(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class TipoLogradouro(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Logradouro(models.Model):
    tipo_logradouro = models.ForeignKey(TipoLogradouro, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9)
    
    def __str__(self):
        return self.nome
    
class Uf(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)
    
    def __str__(self):
        return self.nome
    
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class Pessoa (models.Model):

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
    data_nasc = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    tipo_pessoa = models.ManyToManyField(TipoPessoa)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
class TipoImovel(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class TipoOferta(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Imovel(models.Model):
    nome = models.CharField(max_length=100)
    tipo_imovel = models.ForeignKey(TipoImovel, on_delete=models.CASCADE)
    descricao = models.TextField()
    areaConstruida = models.DecimalField(max_digits=10, decimal_places=2)
    numeroComodos = models.IntegerField()
    cor = models.CharField(max_length=100)
    numeroVagasGaragem = models.IntegerField()
    logradouro = models.ForeignKey(Logradouro, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    valorVendaAluguel = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_oferta = models.ForeignKey(TipoOferta, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    disponivelVenda = models.BooleanField()
    disponivelLocacao = models.BooleanField()
        
    def __str__(self):
        return self.numero
    
class RegistroVenda (models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='vendedor')
    comprador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='comprador')
    
    def __str__(self):
        return self.data
    
class RegistroAluguel (models.Model):
    data = models.DateField()
    dataFinal = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    locador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='locador')
    locatario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='locatario')
    
    def __str__(self):
        return self.data
    

