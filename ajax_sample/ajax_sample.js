let number = 0;
let data = []; // Add variable to store data retrieved from ajax.json
const button = document.getElementById('btn');
const titleArea = document.getElementById("title");
const contentArea = document.getElementById("content");
const videoArea = document.getElementById("video");

function getData() {
  const request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4) {
      if (request.status == 200) {
        data = request.response;
        titleArea.innerHTML = data[number].title;
        contentArea.innerHTML = data[number].content;
        videoArea.setAttribute("src", data[number].url);
        number == 2 ? number = 0 : number++;
      }
    }
  }
  request.open("GET", "ajax.json");
  request.responseType = "json";
  request.send(null);
}

function changeVideo() {
  button.addEventListener('click', () => {
    if (data.length === 0) {
      getData();
    } else {
      titleArea.innerHTML = data[number].title;
      contentArea.innerHTML = data[number].content;
      videoArea.setAttribute("src", data[number].url);
      number == 2 ? number = 0 : number++;
    }
  });
}

window.onload = changeVideo;