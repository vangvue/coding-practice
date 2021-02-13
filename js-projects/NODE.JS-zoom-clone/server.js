const express = require("express");
const app = express();
const server = require("http").Server(app);
const io = require("socketio")(server)
const { v4: uuidv4 } = require("uuid"); // Generates Unique ID
app.set("view engine", "ejs");
app.use(express.static("public"));

app.get("/", (req, res) => {
    res.redirect(`/${uuidv4()}`)
})

app.get("/:room", (req, res) => {
    res.render("room", { roomId: req.params.room })
})

io.on("connection", socket => {
    socket.on("join-room", () => {
        console.log("Hey we have joined the room.")
    })
})


server.listen(3000);