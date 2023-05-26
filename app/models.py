from django.db import models
from django.contrib.auth.models import User

class UsuarioModel(models.Model):
    user = models.OneToOneField( #relacao em que um usuario e um cliente de 0,1
        User,
        related_name='usuarios',
        on_delete=models.CASCADE, #significa que se o User for deletado entao todos os clientes relacionados tambem serao
        blank=True, # torna opcional o relacionamento com um User tornando a relacao 0,1
        null=True, #torna possivel do objeto possuir um valor nulo, o que é diferente de None, pois caso não preenchido terá tal valor
    )
    # garagens_em_uso = models.ManyToManyField(
    #     'GaragemModel', 
    #     related_name='usuarios',
    #     blank=True,
    #     # null=True,
    # )
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
#   nome e email configurados segundo os padroes de USer do django  password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.estacionado_em:
            usuario = self.dono
            usuario.garagens_em_uso.add(self.estacionado_em)
        super().save(*args, **kwargs)

        if self.user:
            self.user.username = self.nome
            self.user.email = self.email

        super().save()
    # def save(self):  # Essa funçao funciona tanto na criaçao quanto na atualizaçao de um objeto, pois é a responsavel por escrever o mesmo na tabela sql
    #     if not self.user and self.nome and self.email:  # verifica se o nome e email foram informados
    #         try:
    #             user = User.objects.get(username=self.nome, email=self.email) # faz uma busca pelo objeto que possui as mesmas descriçoes e o traz
    #             self.user = user # por fim o adiciona, porem caso o get nao encontre um match, havera um exception (User.DoesNotExist) um classe de excecao do proprio django, que automaticamente parara a operacao e buscara o except, nao alterando assim o valor de self.User
    #         except User.DoesNotExist:
    #             pass  # Matching User object not found, leave self.user as None
        
    #     if self.user: # caso o Usuario tenha um user relacionado, toda alteraçao em suas informaçoes tambem serao alterados no objeto User do django
    #         self.user.username = self.nome
    #         self.user.email = self.email
        
    #     super().save() # nao pode ser self pois entraria em loop

    class Meta: # sao informaçoes para a tabela sql
        db_table = "usuarios" 
        # ordering = ['-created'] # ordena pela ordem de inclusao na tabela, porém de forma decrescente (-), em que o mais recente vai para o final da tabela e o mais antigo registrado se torna o primeiro

    def __str__(self): # é a forma como será nomeado quando salvo na memoria da maquina
        return self.nome

class GaragemModel(models.Model):
    numero = models.PositiveIntegerField()


    class Meta:
        db_table = "garagem"
        # ordering = ['-created']

    def __str__(self):
        return str(self.numero)


# class ClienteModel(models.Model): #testando renomeacao para o modelo
#     user = models.OneToOneField( #relacao em que um usuario e um cliente de 0,1
#         User,
#         on_delete=models.CASCADE, #significa que se o User for deletado entao todos os clientes relacionados tambem serao
#         blank=True, # torna opcional o relacionamento com um User tornando a relacao 0,1
#         null=True, #torna possivel do objeto possuir um valor nulo, o que é diferente de None, pois caso não preenchido terá tal valor
#     )
#     garagens_em_uso = models.ManyToManyField(
#         'GaragemModel', 
#         related_name='clientes',
#         blank=True,
#         null=True,
#     )
#     nome = models.CharField(max_length=254)
#     email = models.EmailField(max_length=254)
#     # frota = models.ForeignKey(        Não é possivel tao relacionamento pois para que um CarroModel seja deletado quando seu dono ("Cliente") for deletado, é necessario que o relacionamento seja criado na tabela de CarroModel
#     #     'CarroModel',
#     #     related_name='dono',
#     #     on_delete=models.CASCADE,
#     # )
#     def save(self):  # Essa funçao funciona tanto na criaçao quanto na atualizaçao de um objeto, pois é a responsavel por escrever o mesmo na tabela sql
#         if not self.user and self.nome and self.email:  # verifica se o nome e email foram informados
#             try:
#                 user = User.objects.get(username=self.nome, email=self.email) # faz uma busca pelo objeto que possui as mesmas descriçoes e o traz
#                 self.user = user # por fim o adiciona, porem caso o get nao encontre um match, havera um exception (User.DoesNotExist) um classe de excecao do proprio django, que automaticamente parara a operacao e buscara o except, nao alterando assim o valor de self.User
#             except User.DoesNotExist:
#                 pass  # Matching User object not found, leave self.user as None

#         super().save()

#     class Meta: # sao informaçoes para a tabela sql
#         db_table = "cliente" 
#         ordering = ['-created'] # ordena pela ordem de inclusao na tabela, porém de forma decrescente (-), em que o mais recente vai para o final da tabela e o mais antigo registrado se torna o primeiro

#     def __str__(self): # é a forma como será nomeado quando salvo na memoria da maquina
#         return self.nome

class CarroModel(models.Model):
    dono = models.ForeignKey(
        UsuarioModel,
        related_name='frota',
        on_delete=models.CASCADE, # apesar de que um ClienteModel possa ter mais de um objeto CarroModel, caso o ClienteModel seja apagado, todos os carros relacionados ao mesmo também serao
        blank=False, # especifica que o campo de dono é obrigatorio preenchimento
        null=True, # porém que é possível deixar como null 
    )
    estacionado_em = models.ForeignKey( # o carro pode estar em nenhuma ou uma garagem/ uma garagem pode ter nenhum ou x carros
        GaragemModel, # é necessario que a chave estrangeira seja criada em CarroModel porque é tal objeto que está limitado a 0 e/ou 1 relacionamentos possiveis 
        related_name='carros_estacionados',
        on_delete=models.SET_NULL, # caso a garagem relacionada seja deletada, o carro não sera e o o id da garagem relacionado sera mudado para null
        blank=True,
        null=True,
    )
    placa = models.CharField(max_length=254)
    modelo = models.CharField(max_length=254)
    cor = models.CharField(max_length=254)

    # def save(self):
    #     if self.estacionado_em:
    #         usuario = self.dono
    #         usuario.garagens_em_uso.add(self.estacionado_em)
    #     super().save()

    class Meta:
        db_table = "carro"
        # ordering = ['-created']

    def __str__(self):
        return self.placa


# As possiveis funções para preencher uma classe de molde:
# __str__(self): Não são necessários parâmetros para essa função. Normalmente, ela utiliza os campos do modelo para construir uma representação em formato de string do objeto.

# save(self, *args, **kwargs): A função save() aceita vários parâmetros opcionais:

# force_insert: Se True, força a criação de um novo registro no banco de dados.
# force_update: Se True, força a atualização de um registro existente no banco de dados.
# using: Especifica o alias do banco de dados a ser usado para salvar o objeto.
# update_fields: Uma lista de campos a serem atualizados. Somente esses campos serão salvos.
# exclude: Uma lista de campos a serem excluídos da operação de salvamento.
# delete(self, *args, **kwargs): A função delete() não requer nenhum parâmetro adicional.

# get_absolute_url(self): Não são necessários parâmetros para essa função. Ela deve retornar a URL como uma string.

# clean(self): Não são necessários parâmetros para essa função. Ela deve realizar a validação nos campos do modelo.

# full_clean(self, exclude=None): A função full_clean() aceita um parâmetro opcional:

# exclude: Uma lista de nomes de campos a serem excluídos da validação.
# validate_unique(self, exclude=None): A função validate_unique() aceita um parâmetro opcional:

# exclude: Uma lista de nomes de campos a serem excluídos da validação de unicidade.
# refresh_from_db(self, *args, **kwargs): A função refresh_from_db() aceita os seguintes parâmetros opcionais:

# using: Especifica o alias do banco de dados a ser usado para atualizar o objeto.
# fields: Uma lista de campos a serem atualizados.
# get_FOO_display(self): Não são necessários parâmetros para essa função. Ela é usada para campos com escolhas (choices).

# clean_fields(self, exclude=None): A função clean_fields() aceita um parâmetro opcional:

# exclude: Uma lista de nomes de campos a serem excluídos da validação.
# clean_<nome_do_campo>(self): Essa função não é chamada diretamente, mas é chamada para cada campo que requer validação. Não são necessários parâmetros.

# class UserModel(models.Model):
#     user = models.OneToOneField(
#         User,
#         related_name='usuarios',
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#     )
#     nome = models.CharField(max_length=254)
#     email = models.EmailField(max_length=254)

#     class Meta:
#         db_table = "user"
#         ordering = ["nome"]



#     def __str__(self):
#         return self.nome


# class CarroModel(models.Model):
#     dono = models.ForeignKey(
#         UserModel,
#         related_name='colecao',
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#     )
#     garagem = models.ForeignKey(
#         'GaragemModel',
#         related_name='estacionados',
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#     )
#     placa = models.CharField(max_length=254)
#     modelo = models.CharField(max_length=254)
#     cor = models.CharField(max_length=254)

#     class Meta:
#         db_table = "carro"
#         ordering = ["placa"]

#     def __str__(self):
#         return self.placa

# class GaragemModel(models.Model):
#     numero = models.PositiveIntegerField()

#     class Meta:
#         ordering = ["numero"]

#     def __str__(self):
#         return str(self.numero)
