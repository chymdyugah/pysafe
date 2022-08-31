from django.shortcuts import render, redirect, HttpResponse
from haven.models import Platform, Key
from django.views import generic
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cryptography.fernet import Fernet
from django.contrib.auth.hashers import make_password, check_password

User = get_user_model()
# Create your views here.


class Login(generic.View):
	template_name = 'login.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('haven:index')
		else:
			err = "Invalid username or password"
			return render(request, self.template_name, {'err': err})


class Register(generic.View):
	template_name = 'register.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		key = Fernet.generate_key()  # returns the byte string of the key generated
		key = key.decode()  # byte string should not be saved to db so we decode to normal string
		username = request.POST.get('username')
		password = request.POST.get('password')
		pin = request.POST.get('pin')  # pin input by user
		pin = make_password(pin, hasher='sha1')  # pin hashed with the sha1 algorithm

		# create user
		user = User(username=username)
		user.set_password(password)
		user.save()

		# save key, pin to db; authenticate user and login
		Key.objects.create(user=user, pin=pin, decrypt_key=key)
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('haven:index')
		else:
			err = "Invalid username or password"
			return render(request, self.template_name, {'err': err})


def logout_view(request):
	logout(request)
	return redirect('haven:login')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Index(generic.ListView):
	template_name = 'index.html'
	context_object_name = 'platforms'

	def get_queryset(self):
		return Platform.objects.filter(user=self.request.user)

	def post(self, request):
		url = request.POST.get('url')
		username = request.POST.get('username')
		password = request.POST.get('password')
		key = request.user.key.decrypt_key  # get key saved for the user in db
		fernet = Fernet(key.encode())  # instantiate fernet using the user's key
		password = fernet.encrypt(password.encode())  # returns byte string of encrypted password using key. password must be encoded to byte string before encryption
		password = password.decode()  # we don't want to save the byte string to db

		newplatform = Platform(user=request.user, username=username, password=password, url=url)
		newplatform.save()
		return super().get(request)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Ajx(generic.View):
	def post(self, request):
		pin = request.POST.get('key')  # get pin from user
		pword = request.POST.get('pword')
		if check_password(pin, request.user.key.pin):
			# if the pin user inputs is the same as the hashed pin in the db
			key = request.user.key.decrypt_key  # get key for the user
			fernet = Fernet(key.encode())
			password = fernet.decrypt(pword.encode()).decode()  # because string saved to db is not the encoded byte string we will encode before decrypting
			return HttpResponse(password)
		else:
			return HttpResponse("")
