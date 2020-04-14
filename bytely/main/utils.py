from bytely.models import Link
from bytely.utils import generate_random_string

def generate_anon_id():
    anon_id = f"anon_{generate_random_string(16)}"

    user_id = Link.query.filter_by(user_id=anon_id).first()

    if user_id:
        return generate_anon_id()
    
    return anon_id