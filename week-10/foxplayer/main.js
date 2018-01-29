'use strict';

const play = document.getElementById('play');
const audio = document.getElementsByTagName('audio')[0];
const seekbar = document.getElementById('seekbar');

function printEvent(event) {
  console.log(event);
}

function setupSeekbar() {
  seekbar.min = audio.startTime;
  seekbar.max = audio.startTime + audio.duration;
}
audio.ondurationchange = setupSeekbar;

function seekAudio() {
  audio.currentTime = seekbar.value;
}

function updateUI() {
  let lastBuffered = audio.buffered.end(audio.buffered.length-1);
  seekbar.min = audio.startTime;
  seekbar.max = lastBuffered;
  seekbar.value = audio.currentTime;
}
seekbar.onchange = seekAudio;
audio.ontimeupdate = updateUI;

audio.addEventListener('durationchange', setupSeekbar);
audio.addEventListener('timeupdate', updateUI);

play.addEventListener('click', function(e) {
  if(audio.paused) {
    play.setAttribute('src', 'public/images/pause.svg');
    audio.play();
    printEvent(e);
  }
  else {
    play.setAttribute('src', 'public/images/play.svg')
    audio.pause();
    printEvent(e);
  }
}, false);


