from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models import User, Team, Message, Project, Draft, Resource, Task, Proposal, Publication, Token

class CRUDView(MethodView):
    """
    A class that provides CRUD (Create, Read, Update, Delete) operations for a given model (Python representation of SQL database table).
    """

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
        Retrieves an item from the database based on the provided parameters.

        Args:
            item_id (int): The ID of the item to retrieve. If provided, only the item with the matching ID will be returned.
            filters (dict): A dictionary of filters to apply when retrieving the item(s). Each key-value pair represents a filter condition.
            all_matches (bool): If True, returns all items that match the provided filters. If False, returns only the first matching item.
            serialized (bool): If True, serializes the retrieved item(s) before returning them. If False, returns the item(s) as is.

        Returns:
            tuple: A tuple containing the retrieved item(s) and the HTTP status code.

        Raises:
            Exception: If an error occurs during the retrieval process.

        """
        query = self.model.query
        #try:
        if item_id is not None:
            item = query.get(item_id)
        elif filters:
            if all_matches:
                item = query.filter_by(**filters).all()
            else:
                item = query.filter_by(**filters).first()
        else:
            item = query.all()

        if not item:
            return (None, 200) if not serialized else (jsonify({}), 200)

        if isinstance(item, list):
            return (jsonify([i.serialize() for i in item]), 200) if serialized and all(hasattr(i, 'serialize') for i in item) else (item, 200)
        else:
            return (jsonify(item.serialize()), 200) if serialized and hasattr(item, 'serialize') else (item, 200)
        #except Exception as e:
        #    print(f"Error in get method: {e}")
        #    return jsonify({"message": "Internal server error"}), 500
        
    def post(self, request_data=None):
        """
        Handle HTTP POST requests.

        Args:
            request_data (dict): Optional request data. If provided, it will be used as the data for creating the item.

        Returns:
            Response: JSON response containing the serialized item if successful, or an error message if the item already exists.

        """
        if request_data:
            data = request_data
        else:
            data = request.json
        item = self.model(**data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': f'{self.model.__name__} already exists'}), 400
        return jsonify(item.serialize()), 201

    def put(self, item_id, request_data=None):
            """
            Updates an item in the database.

            Args:
                item_id (int): The ID of the item to be updated.
                request_data (dict, optional): The data to update the item with. Defaults to None.

            Returns:
                dict: A JSON response containing the updated item.
            """
            if request_data:
                data = request_data
                item = self.model(**data)
            else:
                data = request.json
                item = self.model.query.get(item_id)
            if not item:
                return jsonify({'error': f'{self.model.__name__} not found'}), 404
            for key, value in data.items():
                setattr(item, key, value)
            db.session.commit()
            return jsonify(item.serialize())

    def patch(self, item_id, request_data=None):
            """
            Update an item with the given item_id using the provided request_data.

            Args:
                item_id (int): The ID of the item to be updated.
                request_data (dict, optional): The data to update the item with. Defaults to None.

            Returns:
                dict: A JSON response containing the serialized updated item.

            Raises:
                404: If the item with the given item_id is not found.
            """
            if request_data:
                data = request_data
                item = self.model(**data)
            else:
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