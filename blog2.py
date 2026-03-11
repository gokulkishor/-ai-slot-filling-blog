from flask import Flask, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html>
<head>
<title>AI Blog - Slot Filling</title>

<style>

body{
font-family: Arial, sans-serif;
margin:0;
background: linear-gradient(120deg,#0f2027,#203a43,#2c5364);
color:white;
}

/* Header animation */

header{
text-align:center;
padding:60px;
animation: fadeIn 2s ease-in;
}

header h1{
font-size:50px;
color:#00eaff;
}

header p{
font-size:20px;
}

/* Blog section */

.container{
width:80%;
margin:auto;
padding:20px;
}

.blog-card{
background:rgba(255,255,255,0.1);
padding:30px;
border-radius:15px;
margin-bottom:30px;
backdrop-filter: blur(10px);
transition: transform 0.4s;
animation: slideUp 1.5s ease;
}

.blog-card:hover{
transform: scale(1.05);
}

h2{
color:#00ffd5;
}

/* animation */

@keyframes fadeIn{
from{opacity:0;}
to{opacity:1;}
}

@keyframes slideUp{
from{
transform: translateY(100px);
opacity:0;
}
to{
transform: translateY(0);
opacity:1;
}
}

footer{
text-align:center;
padding:20px;
color:#aaa;
}

</style>

</head>

<body>

<header>
<h1>Slot Filling Techniques in Conversational Agents</h1>
<p>Understanding how AI chatbots extract user information</p>
</header>

<div class="container">

<div class="blog-card">
<h2>Introduction</h2>
<p>
Conversational agents like chatbots and voice assistants are widely used
in customer support, booking systems, and smart devices.
A key technology that helps these systems understand user requests is
<b>slot filling</b>.
</p>
</div>

<div class="blog-card">
<h2>What is Slot Filling?</h2>
<p>
Slot filling is a Natural Language Processing technique used to extract
important information from a user's sentence so that the system can
complete a task.
</p>

<p>
Example: “Book a flight from Chennai to Delhi tomorrow”
</p>

<p>
Source → Chennai <br>
Destination → Delhi <br>
Date → Tomorrow
</p>

</div>

<div class="blog-card">
<h2>Techniques Used</h2>

<ul>
<li>Rule Based Extraction</li>
<li>Named Entity Recognition (NER)</li>
<li>Machine Learning Models</li>
<li>Deep Learning (LSTM, BERT)</li>
</ul>

</div>

<div class="blog-card">
<h2>Applications</h2>

<p>
Slot filling is used in:
</p>

<ul>
<li>Flight Booking Assistants</li>
<li>Food Ordering Bots</li>
<li>Customer Service Chatbots</li>
<li>Smart Home Assistants</li>
<li>Banking AI Systems</li>
</ul>

</div>

</div>

<footer>
<p>Created with Python Flask | AI Blog Project</p>
</footer>

</body>
</html>

"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)