from rest_framework import serializers
from app.models import CarroModel, GaragemModel, UsuarioModel
from django.contrib.auth.models import User

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarroModel
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    frota = CarroSerializer(many=True, required=False)
#   garagens_em_uso = GaragemSerializer(many=True, required=False)

    class Meta:
        model = UsuarioModel
        fields = '__all__'

# class ClienteSerializer(serializers.ModelSerializer):
#     frota = CarroSerializer(many=True, required=False)
#     garagens_em_uso = GaragemSerializer(many=True, required=False)

#     class Meta:
#         model = ClienteModel
#         fields = '__all__'

class GaragemSerializer(serializers.ModelSerializer):
    carros_estacionados = CarroSerializer(many=True, required=False) # aqui é que especifica que a garagem pode ter 0 ou x carros atraves do many=True
    usuarios = UsuarioSerializer(many=True, required=False)
# o required=False é necessario pois ao atualizar ou criar um objeto e a informaçao for serializada ao tornar False, a serializaçao nao sofrera de risco de apitar algum Error pois required=False permite que haja valores null e None
    class Meta:
        model = GaragemModel
        fields = '__all__' # por padrao os campos comuns são sempre required=True, porém não é necessario alterar para False, pois os mesmos sempre estarão preenchidos devido a necessidade para criaçao do objeto, pois representam as informaçoes unicas do objeto

class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = '__all__'

# class CustomSerializer(serializers.ModelSerializer): # é possivel adicionar uma nova coluna ao USer providenciado pelo django, sem mexer de fato no modelo
#     usuarios = UsuarioSerializer(many=False, required=False)

#     class Meta: # nao é necessario repassar fields dentro do meta pois ja estao definidos do Serializer original de User do django
#         model = User

# Todas as formas de interação com os objetos de class Model:
# Model.objects.get(**kwargs): Retrieves a single object that matches the given lookup parameters specified in kwargs. The parameters can be field names and their corresponding values. For example: Model.objects.get(id=1) retrieves an object with the id field equal to 1.

# Model.objects.filter(**kwargs): Retrieves a queryset of objects that match the given lookup parameters specified in kwargs. Multiple parameters can be chained together using the & operator to apply an AND condition. For example: Model.objects.filter(name='John', age=25) retrieves objects with the name 'John' and age 25.

# Model.objects.all(): Retrieves all objects of the model. This method doesn't require any parameters.

# Model.objects.create(**kwargs): Creates a new object with the provided field values specified in kwargs and saves it to the database. The parameters should correspond to the fields of the model. For example: Model.objects.create(name='John', age=25) creates a new object with name 'John' and age 25.

# model_instance.save(): Saves the changes made to an existing model instance to the database. This method is called on an instance of a model object and doesn't require any parameters.

# model_instance.delete(): Deletes the model instance from the database. This method is called on an instance of a model object and doesn't require any parameters.

# model_instance.update(**kwargs): Updates the field values of a model instance with the provided values specified in kwargs and saves the changes to the database. This method is called on an instance of a model object. The parameters should correspond to the fields of the model. For example: model_instance.update(name='John', age=30) updates the name and age fields of the model instance.

# model_instance.field_name: Accesses the value of a specific field in a model instance. This is done by directly accessing the field name as an attribute of the model instance. For example: model_instance.name retrieves the value of the 'name' field.

# model_instance.field_name = new_value: Sets a new value for a specific field in a model instance. This is done by assigning a new value to the field name as an attribute of the model instance. For example: model_instance.name = 'Jane' sets the value of the 'name' field to 'Jane'.

# model_instance.related_set.all(): Retrieves all related objects from a related model using a reverse relation. This is used when dealing with related models through a foreign key or a many-to-many relationship. For example: user_instance.book_set.all() retrieves all books related to a user.

# model_instance.related_field: Accesses the related field of a related model. This is used to access a specific related object from a related model. For example: book_instance.author retrieves the author object related to a book.

# Model.objects.get_or_create(**kwargs): Retrieves an object that matches the given lookup parameters specified in kwargs or creates a new object if it doesn't exist. The parameters should correspond to the fields of the model. For example: Model.objects.get_or_create(name='John', age=25) retrieves an existing object with the provided values or creates a new object if it doesn't exist.
# class CarroSerializer(serializers.ModelSerializer):
#     # CarroSerializer implementation

#     class Meta:
#         model = CarroModel
#         fields = '__all__'

# class UserModelSerializer(serializers.ModelSerializer):
#     colecao = CarroSerializer(many=True, required=False)

#     class Meta:
#         model = UserModel
#         fields = '__all__'


# class GaragemSerializer(serializers.ModelSerializer):
#     estacionados = CarroSerializer(many=True, required=False)

#     class Meta:
#         model = GaragemModel
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     usuario = UserModelSerializer(required=False)  # Serializer for the one-to-one relationship

#     class Meta:
#         model = User
#         fields = '__all__'