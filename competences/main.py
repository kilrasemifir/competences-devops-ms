import os
import requests

from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson import ObjectId
from consul import Consul
MONGO_HOST=os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT=os.environ.get("MONGO_PORT", "27017")
DEBUG_MODE=os.environ.get("DEBUG_MODE", "True")
EQUIPE_HOST=os.environ.get("EQUIPE_HOST", "localhost")
EQUIPE_PORT=os.environ.get("EQUIPE_PORT", "9001")
SERVER_PORT=os.environ.get("SERVER_PORT", "80")
SERVER_HOST=os.environ.get("SERVER_HOST", "0.0.0.0")
CONSUL_HOST=os.environ.get("CONSUL_HOST", "localhost")
CONSUL_PORT=os.environ.get("CONSUL_PORT", "9500")

clientC = Consul(host="localhost", port=int(CONSUL_PORT))
clientC.agent.service.register("competences", address="competences")
app = Flask("competences")
client = MongoClient(host=MONGO_HOST, port=int(MONGO_PORT))
db = client["competences"]
collection = db["competences"]

@app.get("/competences")
def retourner_competences():
    # competence_list = list(collection.find())
    competence_list = []
    for data in collection.find():
        data["_id"] = str(data["_id"])
        competence_list.append(data)
    
    return jsonify(competence_list)

@app.get("/competences/<id>")
def retourner_competence_par_id(id:str):
    try:
        objectId = ObjectId(id)
    except:
        return Response(response="l'id doit coorespondre a un ObjectId", status=400)
    competence = collection.find_one({"_id":objectId})
    if competence:
        competence["_id"] = str(competence["_id"])
        return competence
    else:
        return Response(response="Aucune competence ne posséde l'id "+id, status=404)
    

@app.post("/competences")
def sauvegarder_competence():
    competence = request.json
    if not competence.get("equipeId"):
        return Response("Vous devez definir l'id de l'equipe lié a cette competence", status=400)
    equipeId = competence["equipeId"]
    
    response = requests.get(f"http://{EQUIPE_HOST}:{EQUIPE_PORT}/equipes/{equipeId}")
    if response.status_code in (400, 404):
        return Response("equipeId invalide", status=404)
    
    collection.insert_one(competence)
    competence["_id"] = str(competence["_id"])
    return competence
    
@app.delete("/competences/<id>")
def supprimer_par_id(id:str):
    try:
        objectId = ObjectId(id)
    except:
        return Response(response="l'id doit coorespondre a un ObjectId", status=400)
    result = collection.delete_one({"_id":objectId})
    if result.deleted_count:
        return Response(status=202)
    else:
        return Response(status=404)

@app.put("/competences")
def remplacer():
    competence:dict = request.json
    if not competence.get("_id"):
        return Response("le document doit contenir un _id", status=400)
    try:
        objectId = ObjectId(competence.get("_id"))
    except:
        return Response(response="l'id doit correspondre a un ObjectId", status=400)
    # str             ObjectId
    competence["_id"]=objectId
    result = collection.replace_one({"_id":objectId}, competence)
    if result.modified_count:
        return Response(status=202)
    else:
        return Response(status=404)
    
@app.patch("/competences/<id>")
def update(id):
    competence:dict = request.json
    try:
        objectId = ObjectId(id)
    except:
        return Response(response="l'id doit correspondre a un ObjectId", status=400)
    result = collection.update_one({"_id":objectId}, {"$set":competence})
    if result.modified_count:
        return Response(status=202)
    else:
        return Response(status=404)
if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=int(SERVER_PORT), debug=bool(DEBUG_MODE))