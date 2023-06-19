"""Numbers Controller"""

from flask.views import MethodView
from flask_smorest import Blueprint

from schemas.table import (
    NumbersViewSchema,
)
from services.google_sheets import (
    get_info_as_list
)

blp = Blueprint('numbers', __name__, description = 'Operations on numbers.')

@blp.route('/numbers')
class Numbers(MethodView):
    """Controllers for numbers in Google Sheets table"""

    @blp.response(200, NumbersViewSchema(many=True))
    def get(self):
        """
        Get all Numbers and its values for sold.

        :return list: List of numbers.
        """

        return get_info_as_list()
