from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from polls.models import Question


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
				'latest_question_list':latest_question_list,
				'request':request, 
				'request_dir':dir(request)
	}
	return render(request, 'polls/index.html', context)

def dsp(request):
	return HttpResponse("""
			<!DOCTYPE html>
			<html lang="en">
			<head>
			  <title>Bootstrap 5 Website Example</title>
			  <meta charset="utf-8">
			  <meta name="viewport" content="width=device-width, initial-scale=1">
			  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
			  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
			  <style>
			  .fakeimg {
			    height: 200px;
			    background: #aaa;
			  }
			  </style>
			</head>
			<body>

			<div class="p-5 bg-primary text-white text-center">
			  <h1>My First Bootstrap 5 Page</h1>
			  <p>Resize this responsive page to see the effect!</p> 
			</div>

			<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
			  <div class="container-fluid">
			    <ul class="navbar-nav">
			      <li class="nav-item">
			        <a class="nav-link active" href="#">Active</a>
			      </li>
			      <li class="nav-item">
			        <a class="nav-link" href="http://localhost:8000/polls/">Polls</a>
			      </li>
			      <li class="nav-item">
			        <a class="nav-link" href="http://localhost:8000/">Main</a>
			      </li>
			      <li class="nav-item">
			        <a class="nav-link disabled" href="#">Disabled</a>
			      </li>
			    </ul>
			  </div>
			</nav>

			<div class="container mt-5">
			  <div class="row">
			    <div class="col-sm-4">
			      <h2>About Me</h2>
			      <h5>Photo of me:</h5>
			      <div class="fakeimg">Fake Image</div>
			      <p>Some text about me in culpa qui officia deserunt mollit anim..</p>
			      <h3 class="mt-4">Some Links</h3>
			      <p>Lorem ipsum dolor sit ame.</p>
			      <ul class="nav nav-pills flex-column">
			        <li class="nav-item">
			          <a class="nav-link active" href="#">Active</a>
			        </li>
			        <li class="nav-item">
			          <a class="nav-link" href="#">Link</a>
			        </li>
			        <li class="nav-item">
			          <a class="nav-link" href="#">Link</a>
			        </li>
			        <li class="nav-item">
			          <a class="nav-link disabled" href="#">Disabled</a>
			        </li>
			      </ul>
			      <hr class="d-sm-none">
			    </div>
			    <div class="col-sm-8">
			      <h2>TITLE HEADING</h2>
			      <h5>Title description, Dec 7, 2020</h5>
			      <div class="fakeimg">Fake Image</div>
			      <p>Some text..</p>
			      <p>Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p>

			      <h2 class="mt-5">TITLE HEADING</h2>
			      <h5>Title description, Sep 2, 2020</h5>
			      <div class="fakeimg">Fake Image</div>
			      <p>Some text..</p>
			      <p>Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p>
			    </div>
			  </div>
			</div>

			<div class="mt-5 p-4 bg-dark text-white text-center">
			  <p>Footer</p>
			</div>

			</body>
			</html>

		""")

def real_index(request):
	return HttpResponse("""
			<!DOCTYPE html>
				<html>
				<title>W3.CSS</title>
				<meta name="viewport" content="width=device-width, initial-scale=1">
				<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
				<body>

				<div class="w3-sidebar w3-bar-block w3-dark-grey w3-animate-left" style="display:none" id="mySidebar">
				  <button class="w3-bar-item w3-button w3-large"
				  onclick="w3_close()">Close &times;</button>
				  <a href="http://localhost:8000/polls/" class="w3-bar-item w3-button">Polls</a>
				  <a href="http://localhost:8000/polls/dsp/" class="w3-bar-item w3-button">DSP</a>
				  <a href="http://localhost:8000/admin/" class="w3-bar-item w3-button">Admin</a>
				</div>

				<div>
				  <button class="w3-button w3-white w3-xxlarge" onclick="w3_open()">&#9776;</button>
				  <div class="w3-container">
				    <h1>Animated Sidebar</h1>
				    <p>Click on the "hamburger menu" to slide in the side navigation.</p>
				    <p>W3.CSS provide the following animation classes if you want to experiment for yourself:</p>
				    <p>w3-animate-left, w3-animate-top, w3-animate-bottom, w3-animate-right, w3-animate-opacity, w3-animate-zoom</p>
				  </div>
				</div>

				<script>
				function w3_open() {
				    document.getElementById("mySidebar").style.display = "block";
				}
				function w3_close() {
				    document.getElementById("mySidebar").style.display = "none";
				}
				</script>
				     
				</body>
				</html> 

		""")

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	
	context = {
				'question_id':question_id
	}
	
	return render(request, 'polls/details.html', context)

def results(request, question_id):
	context = {
				'question_id':question_id
	}
	
	return render(request, 'polls/results.html', context)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)