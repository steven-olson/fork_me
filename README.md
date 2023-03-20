<h2> Extremely simple github forker</h2>

<h3>Problem we're solving</h3>
We want to have a service that, when called, will fork a gh repo to the current
user's account. We're limiting ourselves to solving the purely backend aspect of this,
although it would be super simple to throw together a react component 
that ajax (through axios) calls this, that would be out of scope.

<h3>How we're solving the problem</h3>
Literally just redirect to the project's fork page. There isn't
really an alternative here, we need to handle github overhead, ie make sure
user is logged in, is authorized etc.

<h3>Alternatives considered</h3>
It's kinda silly for this to be a python service, this could just as easily
be something purely static (a react component) but the requirements are to use python.

<h3>Deploying</h3>
I've included a docker file, you can alternatively just
**python -m pip install** and **flask run** 

<h3>Note</h3>
This forks the repo for this project be default, you can have it 
redirect to another project if you want by setting the TARGET_PROJECT env var.