import os
from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson import ObjectId

MONGO_HOST=os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT=os.environ.get("MONGO_PORT", "27017")
DEBUG_MODE=os.environ.get("DEBUG_MODE", "True")

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
    app.run(host="0.0.0.0", port=80, debug=bool(DEBUG_MODE))