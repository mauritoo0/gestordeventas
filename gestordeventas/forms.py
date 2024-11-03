from django import forms
from .models import Vendedores, Articulos, Clientes, Ventas
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class NuevoVendedor(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=20, widget=forms.TextInput())
    correo = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput())
    
    
class NuevoArticulo(forms.Form):
    articulo = forms.CharField(label="Artículo", max_length=30, widget=forms.TextInput())
    cantidad = forms.IntegerField(label="Cantidad", widget=forms.NumberInput())
    precio_s_iva = forms.FloatField(
        label="Precio sin IVA", 
        widget=forms.NumberInput(),
        
        
    )
   
    
class NuevaVenta(forms.Form):
    vendedor = forms.ModelChoiceField(queryset=Vendedores.objects.all(),label='Vendedor', empty_label='Seleccione un vendedor', widget=forms.Select(attrs={'class': 'form-select'}))
    cliente=forms.ModelChoiceField(queryset=Clientes.objects.all(), label='Cliente', empty_label='Seleccione un cliente', widget=forms.Select(attrs={'class': 'form-select'}))
    articulo = forms.ModelChoiceField(queryset=Articulos.objects.all(),label='Artículo', empty_label='Seleccione un artículo', widget=forms.Select(attrs={'class': 'form-select'}))
    cantidad = forms.IntegerField(label="Cantidad", min_value=1)
    fecha = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],  
    )
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        articulo = self.cleaned_data.get('articulo')
        
        if articulo and cantidad:
            if cantidad > articulo.cantidad: 
                raise forms.ValidationError(f'Stock de {articulo.articulo} insuficiente. Hay {articulo.cantidad} disponibles.')
            return cantidad
    
    
class NuevoCliente(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=20, widget=forms.TextInput())
    apellidos = forms.CharField(label="Apellidos", max_length=20, widget=forms.TextInput())
    direccion = forms.CharField(label="Dirección", max_length=50, widget=forms.TextInput())
    poblacion = forms.CharField(label="Población", max_length=20, widget=forms.TextInput())
    telefono = forms.CharField(label="Teléfono", widget=forms.TextInput(attrs={'pattern': '[0-9]*', 'inputmode': 'numeric'}),
)
    correo = forms.EmailField(label="Correo electrónico", required=False, widget=forms.EmailInput(), error_messages={
        'invalid': 'Correo electrónico inválido'
    })
    vendedor = forms.ModelChoiceField(queryset=Vendedores.objects.all(),label='Vendedor', empty_label='Seleccione un vendedor', widget=forms.Select(attrs={'class': 'form-select'}))


class EliminarVenta(forms.Form):
    eliminar = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class EliminarVendedor(forms.Form):
    eliminar = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class EliminarArticulo(forms.Form):
    eliminar = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    
class EliminarCliente(forms.Form):
    eliminar = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class EditarVendedor(forms.ModelForm):
    class Meta:
        model = Vendedores
        fields = ['nombre', 'correo']
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
        }
    
        widgets = {
            'nombre': forms.TextInput(attrs={'autocomplete': 'on'}),
            'correo': forms.EmailInput(attrs={'autocomplete': 'on'}),
        }


class EditarVenta(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['articulo', 'cliente', 'cantidad', 'vendedor', 'fecha']
        labels = {
            'articulo': 'Artículo',
            'cliente': 'Cliente',
            'cantidad': 'Cantidad',
            'vendedor': 'Vendedor',
            'fecha': 'Fecha'
        }
        widgets = {
            'articulo': forms.Select(attrs={'autocomplete': 'on'}),
            'cliente': forms.Select(attrs={'autocomplete': 'on'}),
            'cantidad': forms.NumberInput(attrs={'autocomplete': 'on'}),
            'vendedor': forms.Select(attrs={'autocomplete': 'on'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'autocomplete': 'on'}), 
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        articulo = self.cleaned_data.get('articulo')
        
        if articulo and cantidad:
            cantidad_disponible = articulo.cantidad
            
            if cantidad > cantidad_disponible:
                raise forms.ValidationError(f'Stock de {articulo.articulo} insuficiente. Hay {articulo.cantidad} disponibles.')
            return cantidad
            
   

class EditarCliente(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellidos', 'direccion', 'poblacion', 'telefono', 'correo', 'vendedor']
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Dirección',
            'poblacion': 'Población',
            'telefono': 'Teléfono',
            'correo': 'Correo electrónico',
            'vendedor': 'Vendedor',
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'autocomplete': 'on'}),
            'apellidos': forms.TextInput(attrs={'autocomplete': 'on'}),
            'direccion': forms.TextInput(attrs={'autocomplete': 'on'}),
            'poblacion': forms.TextInput(attrs={'autocomplete': 'on'}),
            'telefono': forms.TextInput(attrs={'pattern': '[0-9]*', 'inputmode': 'numeric', 'autocomplete': 'on'}),
            'correo': forms.EmailInput(attrs={'autocomplete': 'on'}),
            'vendedor': forms.Select(attrs={'autocomplete': 'on'}),
        }

            
   
class EditarArticulo(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['articulo', 'cantidad', 'precio_s_iva'] 
        labels = {
            'articulo': 'Artículo',
            'cantidad': 'Cantidad',
            'precio_s_iva': 'Precio sin IVA'
            
        }

        widgets = {
            'articulo': forms.TextInput(attrs={'autocomplete': 'on'}),
            'cantidad': forms.NumberInput(attrs={'autocomplete': 'on'}),
            'precio_s_iva': forms.NumberInput(attrs={'autocomplete': 'on'}),
        }
        
        
        
def validate_password_length(value):
        if len(value) < 8:
            raise ValidationError(('La contraseña debe tener un mínimo de 8 caracteres.'))
           
class FormularioPersonalizado(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(),
        error_messages={
            'required': 'El correo electrónico es obligatorio.',
            'invalid': 'Ingrese un correo electrónico válido.',
        })    
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'La contraseña es obligatoria.',
            'min_length': 'La contraseña debe tener al menos 8 caracteres.',
            'password_too_common': 'La nueva contraseña es muy común.',
        }
    )

    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Confirmar contraseña es obligatorio.',
            'password_mismatch': 'Las contraseñas no coinciden.',
        }
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
                       
        }
        
        error_messages = {
            'username': {
                'required': 'El nombre de usuario es obligatorio.',
                'unique': 'Este nombre de usuario ya está en uso.',
            
            },
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso.')
        return email
    
     
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['password1'].error_messages['required'] = 'La contraseña es obligatoria.'
        self.fields['password1'].error_messages['min_length'] = 'La contraseña debe tener al menos 8 caracteres.'
        self.fields['password1'].validators.append(validate_password_length)
        self.fields['password2'].validators.append(validate_password_length)
        
        self.fields['password2'].error_messages['required'] = 'Confirma tu contraseña.'
       
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2    
        
        
class LoginPersonalizado(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class':'form-input', 'placeholder':'Ingresa tu usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-input', 'placeholder':'Ingresa tu contraseña'})

    )
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password'].help_text = None
        
        self.error_messages = {
            'invalid_login': 'Nombre de usuario y/o contraseña incorrectos', 
            'inactive': 'Usuario está inactivo',
        }
    
    
class EditarPerfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']    
        labels = {
            
            'first_name':'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            
            
        }
        widgets = {
            
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            
        }
        
    def __init__(self, *args, **kwargs):
        super(EditarPerfil, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
    
            
class BuscarVendedor(forms.Form):
    nombre = forms.CharField(label='Buscar vendedor', max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'campo-busqueda', 'placeholder': 'Nombre del vendedor'}))
    
    
class BuscarArticulo(forms.Form):
    nombre_articulo = forms.CharField(label='Buscar artículo', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'campo-busqueda', 'placeholder': 'Nombre del artículo'}))


class BuscarVenta(forms.Form):
    b_venta = forms.CharField(label='Buscar venta', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'campo-busqueda', 'placeholder': 'Escribe algún indicio de la venta que buscas...'}))
    
    
class BuscarCliente(forms.Form):
    cliente = forms.CharField(label="Buscar cliente", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'campo-busqueda', 'placeholder': 'Escribe datos del cliente'}) )        