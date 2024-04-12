from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CustomUserCreationForm

# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre_usuario']
            contraseña = form.cleaned_data['contraseña']
            usuario = authenticate(request, username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('welcome')  # Redirige a la página de bienvenida tras el inicio de sesión
            else:
                # Mensaje de error si la autenticación falla
                return render(request, 'mi_aplicacion/login.html', {'form': form, 'error': 'Nombre de usuario o contraseña incorrecta'})
    else:
        form = LoginForm()
    return render(request, 'mi_aplicacion/login.html', {'form': form})

# Vista de registro
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al inicio de sesión después de un registro exitoso
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'mi_aplicacion/register.html', {'form': form})

# Vista de bienvenida
def welcome(request):
    # Renderiza una página de bienvenida simple
    return render(request, 'mi_aplicacion/welcome.html')
