//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;
 
var gumStream; //stream from getUserMedia()
var rec; //Recorder.js object
var input; //MediaStreamAudioSourceNode we'll be recording
 
// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext = new AudioContext; //new audio context to help us record
 
var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");
var pauseButton = document.getElementById("pauseButton"); 
 
//recordButton.addEventListener("click", startRecording);

function startRecording() {
    console.log("recordButton clicked");
    var constraints = { audio: true, video:false }
 
    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
      console.log("getUserMedia() success, stream created, initializing Recorder.js ...");

      /* assign to gumStream for later use */
      gumStream = stream;

      /* use the stream */
      input = audioContext.createMediaStreamSource(stream);

      /* 
      Create the Recorder object and configure to record mono sound (1 channel)
      Recording 2 channels  will double the file size
      */
      rec = new Recorder(input,{numChannels:1})

      //start the recording process
      rec.record()

      console.log("Recording started");

      $('#divRecording').hide();
      setTimeout(function() {
        console.log("2-sec passed");
        setTimeout(function() {
          console.log("2-sec passed");
          setTimeout(function() {
            console.log("2-sec passed");
            setTimeout(function() {
              console.log("2-sec passed");
              setTimeout(function() {
                $('#divRecording').hide();
                $('#divLoading').hide();
                stopRecording();
                $('#divRecord').hide();
                $('#recordButton').attr('src', '/static/rec.jpg');
                $('#upload-complete-container').show();
              }, 2000); // WAIT 2 milliseconds
            }, 2000); // WAIT 2 milliseconds
          }, 2000); // WAIT 2 seconds
        }, 2000); // WAIT 2 seconds
      }, 2000); // WAIT 2 second
    }).catch(function(err) {
      //enable the record button if getUserMedia() fails
      //recordButton.disabled = false;
      //stopButton.disabled = true;
      //pauseButton.disabled = true
    });
}

function pauseRecording(){
    console.log("pauseButton clicked rec.recording=",rec.recording );
    if (rec.recording){
        //pause
        rec.stop();
        pauseButton.innerHTML="Resume";
    }else{
        //resume
        rec.record()
        pauseButton.innerHTML="Pause";
    }
}

function stopRecording() {
    console.log("stopButton clicked");
 
    //tell the recorder to stop the recording
    rec.stop();
 
    //stop microphone access
    gumStream.getAudioTracks()[0].stop();
 
    //create the wav blob and pass it on to createDownloadLink
    rec.exportWAV(uploadFile);
}

var filename;
function uploadFile(blob) {
  filename = new Date().toISOString(); //filename to send to server without extension
  var fd = new FormData();
  fd.append("audio_data",blob, filename);

  var xhr=new XMLHttpRequest();
  xhr.open("POST","https://host.wednus.com/prosper/upload.php", true);
  xhr.send(fd);
  xhr.onload=function(e) {
    if(this.readyState === 4) {
        console.log("Server returned: ",e.target.responseText);
        window.location.replace("./file/"+ filename +".wav");
        $('#divLoading').show();
        var $progressBar = $('.progress-bar');
        setTimeout(function() {
        $progressBar.css('width', '20%');
          setTimeout(function() {
            $progressBar.css('width', '40%');
            setTimeout(function() {
              $progressBar.css('width', '60%');
              setTimeout(function() {
                $progressBar.css('width', '80%');
                setTimeout(function() {
                  $progressBar.css('width', '100%');
                  //$('#divLoading').hide();
                  //$progressBar.css('width', '0%');  // init. back
                }, 8000); // WAIT 2 milliseconds
              }, 8000); // WAIT 2 milliseconds
            }, 8000); // WAIT 2 seconds
          }, 8000); // WAIT 2 seconds
        }, 8000); // WAIT 2 second        
    }
  };
}