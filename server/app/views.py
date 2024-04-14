from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models import User, Team, Message, Project, Draft, Resource, Task, Proposal, Publication, Token

class CRUDView(MethodView):
    """
    A class that provides CRUD (Create, Read, Update, Delete) operations for a given model.

    Attributes:
        model: The model class associated with the CRUD operations.
    """

    model = None

    def __init__(self, model=None):
        """
        Initializes the CRUDView instance.

        Args:
            model: The model class associated with the CRUD operations.
        """
        if model:
            self.model = model
 
    def get(self, item_id=None, filters=None, all_matches=False, serialized=True):
        """
        Retrieve an item or a list of items based on the provided parameters.

        Args:
            item_id (int): The ID of the item to retrieve. If provided, only a single item will be returned.
            filters (dict): A dictionary of filters to apply when querying the items. Only items that match the filters will be returned.
            all_matches (bool): If True, return all items that match the filters. If False, return only the first item that matches the filters.
            serialized (bool): If True, serialize the item(s) before returning. If False, return the item(s) as Python objects.

        Returns:
            If item_id is provided and an item with the specified ID exists, return the item.
            If filters are provided and at least one item matches the filters, return the item(s).
            If no item is found, return a JSON response with an error message and a 404 status code.

        Note:
            - If item_id is provided, filters will be ignored.
            - If all_matches is True, filters will be ignored and all items that match the filters will be returned.
            - If serialized is False, the item(s) will be returned as Python objects instead of serialized JSON.

        """
        query = self.model.query

        item = query.get(item_id) if item_id else [item for item in query.filter_by(**filters)] if filters and all_matches else query.filter_by(**filters).first() if filters else query.all()

        if not item:
            return jsonify({'error': f'{self.model.__name__} not found'}), 404

        return jsonify([i.serialize() for i in item]) if serialized and isinstance(item, list) and all(hasattr(i, 'serialize') for i in item) else item if isinstance(item, list) else jsonify(item.serialize()) if serialized and hasattr(item, 'serialize') else item

    def post(self):
        """
        Creates a new item in the database.

        Returns:
            If the item is created successfully, returns a JSON representation of the created item and status code 201.
            If there is an integrity error, rolls back the session and raises an exception.
        """
        data = request.json
        item = self.model(**data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': f'{self.model.__name__} already exists'}), 400
        return jsonify(item.serialize()), 201

    def put(self, item_id):
        """
        Updates an existing item in the database.

        Args:
            item_id: The ID of the item to update.

        Returns:
            If the item is found and updated successfully, returns a JSON representation of the updated item.
            If the item is not found, returns a JSON response with an error message and status code 404.
        """
        data = request.json
        item = self.model.query.get(item_id)
        if not item:
            return jsonify({'error': f'{self.model.__name__} not found'}), 404
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return jsonify(item.serialize())

    def patch(self, item_id):
        """
        Partially updates an existing item in the database.

        Args:
            item_id: The ID of the item to update.

        Returns:
            If the item is found and updated successfully, returns a JSON representation of the updated item.
            If the item is not found, returns a JSON response with an error message and status code 404.
        """
        data = request.json
        item = self.model.query.get(item_id)
        if not item:
            return jsonify({'error': f'{self.model.__name__} not found'}), 404
        for key, value in data.items():
            if hasattr(item, key):
                setattr(item, key, value)
        db.session.commit()
        return jsonify(item.serialize())

    def delete(self, item_id):
        """
        Deletes an existing item from the database.

        Args:
            item_id: The ID of the item to delete.

        Returns:
            If the item is found and deleted successfully, returns a JSON response with a success message and status code 200.
            If the item is not found, returns a JSON response with an error message and status code 404.
        """
        item = self.model.query.get(item_id)
        if not item:
            return jsonify({'error': f'{self.model.__name__} not found'}), 404
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': f'{self.model.__name__} deleted successfully'}), 200

models = [User, Team, Message, Project, Draft, Resource, Task, Proposal, Publication, Token]

for model in models:
    view = type(f'{model.__name__}View', (CRUDView,), {'model': model}).as_view(f'{model.__name__.lower()}s')
    app.add_url_rule(f'/api/{model.__name__.lower()}s', view_func=view, methods=['GET', 'POST'])
    app.add_url_rule(f'/api/{model.__name__.lower()}s/<int:item_id>', view_func=view, methods=['GET', 'PUT', 'DELETE', 'PATCH'])