const socket = io("/");
const videoGrid = document.getElementById("video-grid");
const myVideo = document.createElement("video");
myVideo.muted = true;

var peer = new Peer(undefined, {
    path: "/peerjs",
    host: "/",
    port: "3000"
});

let myVideoStream;
navigator.mediaDevices.getUserMedia({
    video: true,
    audio: true
}).then(stream => {
    myVideoStream = stream;
    addVideoStream(myVideo, stream);

    peer.on("call", call => {
        call.answer(stream); // Answer the call with an A/V stream.
        const video = document.createElement("video");
        call.on("stream", userVideoStream => {
            addVideoStream(video, userVideoStream);
        })
    })

    socket.on("user-connected", (userId) => {
        connectToNewUser(userId, stream);

    })

    let text = $("input");

    $("html").keydown((e) => { // e --> event
        if (e.which == 13 && text.val().length !== 0) { // 13 = enter key, makes sure no empty text
            socket.emit("message", text.val()); // (emit) sends, (on) receives
            text.val(""); // clear input
        }
    })

    socket.on("createMessage", (message) => {
        $("ul").append(`<li class="message"><b>user</b><br/>${message}</li>`)
    })
})

peer.on("open", id => {
    socket.emit("join-room", ROOM_ID, id);
})

const connectToNewUser = (userId, stream) => {
    const call = peer.call(userId, stream);
    const video = document.createElement("video");
    call.on("stream", userVideoStream => {
        addVideoStream(video, userVideoStream)
    })
}


const addVideoStream = (video, stream) => {
    video.srcObject = stream;
    video.addEventListener("loadedmetadata", () => {
        video.play();
    })
    videoGrid.append(video);
}