const express = require("express");

app = express();

app.get("/utilisateurs", (req, res)=>{
    res.send("Hello world")
})

app.listen(8888, ()=>console.log("Lancement de l'application utilisateurs"))