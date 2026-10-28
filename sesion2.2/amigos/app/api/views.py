from flask import request, abort, jsonify
from .. import db
from . import api
from ..models import Amigo


@api.route("/amigo/<int:id>")
def get_amigo(id):
    """
    Retorna JSON con información sobre el amigo cuyo id recibe como parámetro
    o un error 404 si no lo encuentra.
    """
    amigo = Amigo.query.get_or_404(id)
    amigodict = {
        'id': amigo.id,
        'name': amigo.name,
        'lati': amigo.lati,
        'longi': amigo.longi,
        'device': amigo.device
    }
    return jsonify(amigodict)


@api.route("/amigo/byName/<name>")
def get_amigo_by_name(name):
    """
    Busca el amigo por su nombre en la base de datos. Si no lo encuentra
    retorna un error 404. Si lo encuentra retorna el JSON con sus datos.
    """
    amigo = Amigo.query.filter_by(name=name).first()
    if not amigo:
        abort(404, "No se encuentra ningún amigo con ese nombre")

    amigodict = {
        'id': amigo.id,
        'name': amigo.name,
        'lati': amigo.lati,
        'longi': amigo.longi,
        'device': amigo.device
    }
    return jsonify(amigodict)


@api.route("/amigos")
def list_amigos():
    """
    Retorna un JSON con la lista de amigos. Cada amigo es un diccionario
    con los campos 'id', 'name', 'lati', 'longi' y 'device'.
    """
    amigos = Amigo.query.all()
    lista = []
    for amigo in amigos:
        lista.append({
            'id': amigo.id,
            'name': amigo.name,
            'lati': amigo.lati,
            'longi': amigo.longi,
            'device': amigo.device
        })
    return jsonify(lista)


@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):
    """
    Modifica en la base de datos el amigo cuyo id recibe como parámetro.
    Retorna el JSON con el amigo tras la modificación.
    """
    amigo = Amigo.query.get_or_404(id)

    if not request.json:
        abort(422, "No se ha enviado JSON")

    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")
    device = request.json.get("device")

    if name:
        amigo.name = name
    if lati:
        amigo.lati = lati
    if longi:
        amigo.longi = longi
    if device is not None:
        amigo.device = device

    if name or lati or longi or device is not None:
        db.session.commit()

    amigodict = {
        'id': amigo.id,
        'name': amigo.name,
        'lati': amigo.lati,
        'longi': amigo.longi,
        'device': amigo.device
    }
    return jsonify(amigodict)


@api.route("/amigo/<int:id>", methods=["DELETE"])
def delete_amigo(id):
    """
    Elimina un amigo cuyo id recibe como parámetro de la base de datos.
    """
    amigo = Amigo.query.get_or_404(id)
    db.session.delete(amigo)
    db.session.commit()
    return ('', 204)


@api.route("/amigos", methods=["POST"])
def new_amigo():
    """
    Añade un amigo a la base de datos con los datos recibidos en JSON.
    """
    if not request.json:
        abort(422, "No se ha enviado JSON")

    name = request.json.get("name")
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")

    amigo_existente = Amigo.query.filter_by(name=name).first()
    if amigo_existente:
        abort(422, "Ya existe un amigo con ese nombre")

    lati = request.json.get("lati", "0")
    longi = request.json.get("longi", "0")
    device = request.json.get("device")

    amigo = Amigo(name=name, lati=lati, longi=longi, device=device)
    db.session.add(amigo)
    db.session.commit()

    amigodict = {
        'id': amigo.id,
        'name': amigo.name,
        'lati': amigo.lati,
        'longi': amigo.longi,
        'device': amigo.device
    }
    return jsonify(amigodict)


@api.route("/devices")
def list_devices():
    """
    Retorna la lista de todos los device no nulos ni vacíos.
    """
    amigos = Amigo.query.filter(
        Amigo.device.isnot(None),
        Amigo.device != ""
    ).all()
    return jsonify([amigo.device for amigo in amigos])