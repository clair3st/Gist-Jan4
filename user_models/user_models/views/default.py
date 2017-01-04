from pyramid.response import Response
from pyramid.view import view_config

from ..models import User

from pyramid.httpexceptions import HTTPFound


@view_config(route_name="home",
             renderer="../templates/home.jinja2")
def home_view(request):
    """A view of the home page."""
    return {}

@view_config(route_name='register', renderer='../templates/register.jinja2')
def new_entry(request):
    """View the new entry page."""
    if request.method == "POST":
        new_model = User(firstname=request.POST['firstname'],
                         lastname=request.POST['lastname'],
                         username=request.POST['username'],
                         email=request.POST['email'],
                         password=request.POST['password'],
                         food=request.POST['food']
                        )
        request.dbsession.add(new_model)
        return HTTPFound(location=request.route_url('home'))
    return {}


@view_config(route_name='profile', renderer='../templates/profile.jinja2')
def detail_page(request):
    """One entry for detail veiw."""
    data = request.dbsession.query(User).get(request.matchdict['user'])
    return {'users': data}
