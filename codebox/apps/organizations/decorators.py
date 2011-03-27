from flask import abort, request
from functools import wraps

from codebox.apps.organizations.models import OrganizationMember

def can_view_org(f):
    @wraps(f)
    def decorated_function(org, *args, **kwargs):
        if not getattr(request, 'user', None) or \
           not OrganizationMember.objects.index_exists('org', org, g.user.id):
            abort(404)
        return f(org, *args, **kwargs)
    return decorated_function