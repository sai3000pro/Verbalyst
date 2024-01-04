window.addEventListener("load", function() {
var recordButton = document.querySelector("#startRecord");
var stopButton = document.querySelector("#stopRecord")
var refreshButton = document.querySelector("#refresh");
var recordingNumber;
// var startRec = new Audio ("{{url_for('audio', filename='audio/startrecordingsoundeffect.mp3'");
// var stopRec = new Audio("/audio/stoprecordingsoundeffect.mp3");
// // static/audio/startrecordingsoundeffect.mp3
// //        audio/startrecordingsoundeffect.mp3
// recordButton.addEventListener("click", function () {
//     startRec.play();
// });

// stopButton.addEventListener("click", function () {
//     stopRec.play();
// });

const test = ["hi!"];

const tongueTwisters = ["Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?", "Betty Botter bought some butter. But she said the butter's bitter. If I put it in my batter, it will make my batter bitter. But a bit of better butter will make my batter better. So it was better Betty Botter bought a bit of better butter.", "How much wood would a woodchuck chuck if a woodchuck could chuck wood? He would chuck, he would, as much as he could, and chuck as much wood. As a wood chuck would if a woodchuck could chuck wood.", "Sally sells seashells by the seashore.", "How can a clam cram in a clean cream can?", "I scream, you scream, we all scream for ice cream.", "I saw Susie sitting in a shoeshine shop.", "Susie works in a shoeshine shop. Where she shines she sits, and where she sits she shines.", "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn't fuzzy, was he?", "Can you can a can as a canner can can a can?", "I have got a date at a quarter to eight; I'll see you at the gate, so don't be late.", "You know New York, you need New York, you know you need unique New York.", "I saw a kitten eating chicken in the kitchen.", "If a dog chews shoes, whose shoes does he choose?", "I wish to wash my Irish wristwatch.", "Near an ear, a nearer ear, a nearly eerie ear.", "A big black bear sat on a big black rug.", "Tom threw Tim Three thumbtacks.", "Nice nice night nurses nursing nicely", "Wayne went to wales to watch walruses", "We surely shall see the sun shine soon.", "Which wristwatches are Swiss wristwatches?", "Fred fed Ted bread, and Ted fed Fred bread.", "I slit the sheet, the sheet I slit, and on the slitted sheet I sit.", "A skunk sat on a stump and thunk the stump stunk, but the stump thunk the skunk stunk.", "Lesser leather never weathered wetter weather better.", "Of all the videos I've ever viewed, I've never viewed a video as valued as Value Village's Vinter V1"];

// randomly sorts this array so that the order isn't quite the same every time
var a;
var b;
var bucket;
var i = 0;

function sorter() {
    for (var x = 0; x<100; x++) {
        a = Math.floor(Math.random()*tongueTwisters.length);
        b = Math.floor(Math.random()*tongueTwisters.length);
    
        // doesn't let these variables be the same
        while (b === a) {
            b = Math.floor(Math.random()*tongueTwisters.length);
        }
        bucket = tongueTwisters[b];
        tongueTwisters[b] = tongueTwisters[a]; 
        tongueTwisters[a] = bucket;
    }
}



    sorter();
    console.log("SCRAMBLE")
    document.querySelector("#firstFlashcard").textContent = tongueTwisters[i];
    document.querySelector("#secondFlashcard").textContent = tongueTwisters[i + 1];
    document.querySelector("#thirdFlashcard").textContent = tongueTwisters[i + 2];

    refreshButton.addEventListener("click", refresh);

function refresh() {
        i+=3;
        document.querySelector("#firstFlashcard").textContent=tongueTwisters[i];
        document.querySelector("#secondFlashcard").textContent=tongueTwisters[i+1];
        document.querySelector("#thirdFlashcard").textContent=tongueTwisters[i+2];
        if (i >= (tongueTwisters.length - 1)) {
            i = 0;
            alert("No more tongue twisters! Check back later.");
        }
}


});



