{% extends 'container.html' %}
{% block title %}<title>Register</title>{% endblock %}
{% block body %}
	<div class="col-xs-12 col-md-offset-3 col-md-6">
		<form method="post">
			<div class="col-xs-12 form-group">
				<label>Email</label>
				<input type="text" name="username" class="form-control" required>
			</div>
			<div class="col-xs-12 form-group">
				<label>Password</label>
				<input type="password" name="password" class="form-control" required>
			</div>
			<div class="col-xs-12 form-group">
				<input type="submit" name="submit" class="btn btn-default" value="Register">
			</div>
			
		</form>
	</div><br><br>
	<div class="col-xs-12 col-ms-offset-1">
		<center><a href="{% url 'haven:login' %}"><p>Login if you already have an account</p></a></center>
	</div>
{% endblock %}
