from datetime import datetime
from my_app import models, db
from flask import current_app as app, jsonify, abort, request


@app.route("/users", methods=["GET"])
def page_users():
    users = db.session.query(models.User).all()
    return jsonify([user.serialize() for user in users])


@app.route("/users/<int:user_id>", methods=["GET"])
def page_user_by_id(user_id):
    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        abort(404)

    return jsonify(user.serialize())


@app.route("/orders", methods=["GET"])
def page_orders():
    orders = db.session.query(models.Order).all()
    return jsonify([order.serialize() for order in orders])


@app.route("/orders/<int:order_id>", methods=["GET"])
def page_order_by_id(order_id):
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if order is None:
        abort(404)

    return jsonify(order.serialize())


@app.route("/offers", methods=["GET"])
def page_offers():
    offers = db.session.query(models.Offer).all()
    return jsonify([offer.serialize() for offer in offers])


@app.route("/offers/<int:offer_id>", methods=["GET"])
def page_offer_by_id(offer_id):
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if offer is None:
        abort(404)

    return jsonify(offer.serialize())


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    db.session.add(models.User(**data))
    db.session.commit()

    return {}


@app.route("/users/<int:user_id>", methods=["PUT"])
def change_user(user_id):
    data = request.json

    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(data)
    db.session.commit()

    return {}


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    result = db.session.query(models.User).filter(models.User.id == user_id).delete()

    if result == 0:
        abort(404)
    db.session.commit()

    return {}


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    if 'start_date' in data:
        data['start_date'] = datetime.strptime(data['start_date'], '%m-%d-%Y').date()

    if 'end_date' in data:
        data['end_date'] = datetime.strptime(data['end_date'], '%m-%d-%Y').date()

    db.session.add(models.Order(**data))
    db.session.commit()

    return {}


@app.route("/orders/<int:order_id>", methods=["PUT"])
def change_order(order_id):
    data = request.json

    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if order is None:
        abort(404)

    db.session.query(models.Order).filter(models.Order.id == order_id).update(data)
    db.session.commit()

    return {}


@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):

    result = db.session.query(models.Order).filter(models.Order.id == order_id).delete()

    if result == 0:
        abort(404)
    db.session.commit()

    return {}

@app.route("/offers", methods=["POST"])
def create_offer():
    data = request.json

    db.session.add(models.Offer(**data))
    db.session.commit()

    return {}


@app.route("/offers/<int:offer_id>", methods=["PUT"])
def change_offer(offer_id):
    data = request.json

    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if offer is None:
        abort(404)

    db.session.query(models.Offer).filter(models.Offer.id == offer_id).update(data)
    db.session.commit()

    return {}


@app.route("/offers/<int:offer_id>", methods=["DELETE"])
def delete_offer(offer_id):

    result = db.session.query(models.Offer).filter(models.Offer.id == offer_id).delete()

    if result == 0:
        abort(404)
    db.session.commit()

    return {}

