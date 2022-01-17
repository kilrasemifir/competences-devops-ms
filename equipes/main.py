import os
from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson import ObjectId

MONGO_HOST=os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT=os.environ.get("MONGO_PORT", "27017")
DEBUG_MODE=os.environ.get("DEBUG_MODE", "True")

app = Flask("equipes")
client = MongoClient(host=MONGO_HOST, port=int(MONGO_PORT))
db = client["equipes"]
collection = db["equipes"]

@app.get("/equipes")
def retourner_equipes():
    # equipe_list = list(collection.find())
    equipe_list = []
    for data in collection.find():
        data["_id"] = str(data["_id"])
        equipe_list.append(data)
    
    return jsonify(equipe_list)

@app.get("/equipes/<id>")
def retourner_equipe_par_id(id:str):
    try:
        objectId = ObjectId(id)
    except:
        return Response(response="l'id doit coorespondre a un ObjectId", status=400)
    equipe = collection.find_one({"_id":objectId})
    if equipe:
        equipe["_id"] = str(equipe["_id"])
        return equipe
    else:
        return Response(response="Aucune equipe ne posséde l'id "+id, status=404)
    

@app.post("/equipes")
def sauvegarder_equipe():
    equipe = request.json
    collection.insert_one(equipe)
    equipe["_id"] = str(equipe["_id"])
    return equipe
    
@app.delete("/equipes/<id>")
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

@app.put("/equipes")
def remplacer():
    equipe:dict = request.json
    if not equipe.get("_id"):
        return Response("le document doit contenir un _id", status=400)
    try:
        objectId = ObjectId(equipe.get("_id"))
    except:
        return Response(response="l'id doit correspondre a un ObjectId", status=400)
    # str             ObjectId
    equipe["_id"]=objectId
    result = collection.replace_one({"_id":objectId}, equipe)
    if result.modified_count:
        return Response(status=202)
    else:
        return Response(status=404)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=bool(DEBUG_MODE))