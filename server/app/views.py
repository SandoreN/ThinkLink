from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from app import app, db
from app.models import User, Team, Message, Project, Draft, Resource, Task, Proposal, Publication

class CRUDView(MethodView):
    model = None

    def __init__(self, model=None):
        if model:
            self.model = model
    '''    
    def get(self, item_id=None):
        if item_id is None:
            if len(request.json) == 0:
                return jsonify([item.serialize() for item in self.model.query.all()])
            else:
                item = self.model.query.filter_by(**request.json).first()
                if not item:
                    return jsonify({'error': f'{self.model.__name__} not found'}), 404
                return jsonify(item.serialize())
        else:
            item = self.model.query.get(item_id)
            if not item:
                return jsonify({'error': f'{self.model.__name__} not found'}), 404
            return jsonify(item.serialize()) 
    '''
    # New method will return a json object by default, returns python object if serialized is False
    def get(self, item_id=None, serialized=True):
        query = self.model.query
        item = query.get(item_id) if item_id else query.filter_by(**request.json).first() if request.json else query.all()
        if not item:
            return jsonify({'error': f'{self.model.__name__} not found'}), 404
        return jsonify(item.serialize()) if serialized and hasattr(item, 'serialize') else item

    def post(self):
        data = request.json
        item = self.model(**data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise
        return jsonify(item.serialize()), 201

    def put(self, item_id):
        data = request.json
        item = self.model.query.get(item_id)
        if not item:
            return jsonify({'error': f'{self.model.__name__} not found'}), 404
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return jsonify(item.serialize())
    
    def patch(self, item_id):
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
        item = self.model.query.get(item_id)
        if not item:
            return jsonify({'error': f'{self.model.__name__} not found'}), 404
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': f'{self.model.__name__} deleted successfully'}), 200

models = [User, Team, Message, Project, Draft, Resource, Task, Proposal, Publication]

for model in models:
    view = type(f'{model.__name__}View', (CRUDView,), {'model': model}).as_view(f'{model.__name__.lower()}s')
    app.add_url_rule(f'/api/{model.__name__.lower()}s', view_func=view, methods=['GET', 'POST'])
    app.add_url_rule(f'/api/{model.__name__.lower()}s/<int:item_id>', view_func=view, methods=['GET', 'PUT', 'DELETE', 'PATCH'])