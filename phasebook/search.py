from flask import Blueprint, request

from .data.search_data import USERS
from collections import OrderedDict



bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    search_id = args.get('id')
    search_name = args.get('name', '').lower()
    search_age = args.get('age')
    search_occupation = args.get('occupation', '').lower()

    results = []

    # Create helper fucntion for matches
    def matches_name(user, name):
        return name in user['name'].lower()

    def matches_age(user, age):
        try:
            age = int(age)
            return age - 1 <= user['age'] <= age + 1
        except ValueError:
            return False

    def matches_occupation(user, occupation):
        return occupation in user['occupation'].lower()

    # Using searcing parameters to check each users.
    for user in USERS:
        match = False
        if search_id and user['id'] == search_id:
            match = True
        if search_name and matches_name(user, search_name):
            match = True
        if search_age and matches_age(user, search_age):
            match = True
        if search_occupation and matches_occupation(user, search_occupation):
            match = True

        if match:
            user_result = {
                "id": user["id"],
                "name": user["name"],
                "age": user["age"],
                "occupation": user["occupation"]
            }
            results.append(user_result)

    return results



