"""Numbers Controller"""

from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request

from schemas.table import (
    NumbersViewSchema,
)
from schemas.seller import (
    SellerSchema,
)
from services.google_sheets import (
    get_info_as_list,
    get_personal_message,
    get_seller,
)

blp = Blueprint('numbers', __name__, description = 'Operations on numbers.')

@blp.route('/numbers')
class Numbers(MethodView):
    """Controllers for numbers in Google Sheets table."""

    @blp.response(200, NumbersViewSchema(many=True))
    def get(self):
        """
        Get all Numbers and its values for sold.

        :return list: List of numbers.
        """

        return get_info_as_list()


@blp.route('/numbers/<string:seller_name>')
class PersonalNumbers(MethodView):
    """Controllers for personal numbers in Google Sheets table."""

    @blp.response(200, SellerSchema)
    def get(self, seller_name: str):
        """
        Get numbers, quantity of sold and non-sold number and seller name.

        :return SellerSchema: Seller info..
        """

        return get_seller(seller_name)


@blp.route('/my_numbers')
class MyNumbers(MethodView):
    """Controllers for personal messages in Google Sheets table."""

    @blp.doc(
        params={
            'name': {'description': 'Seller name', 'in': 'query', 'type': 'string'}
        }
    )
    def get(self):
        """
        Get all Numbers and its values for sold.

        :return list: List of numbers.
        """

        seller_name = request.args.get('name')

        return get_personal_message(seller_name)
