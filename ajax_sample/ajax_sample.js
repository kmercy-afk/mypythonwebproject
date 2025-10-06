let number = 0;
let data = null; // Store data from ajax.json
const button = document.getElementById('btn');
const titleArea = document.getElementById("title");
const contentArea = document.getElementById("content");
const videoArea = document.getElementById("video");

function getData(callback) {
if (data) {
    // Data already fetched, just call the callback
    callback();
    return;
}

  // Fetch data only once
const request = new XMLHttpRequest();
request.onreadystatechange = function () {
    if (request.readyState === 4 && request.status === 200) {
      data = request.response; // Store the fetched data
    callback();
    }
};
request.open("GET", "ajax.json");
request.responseType = "json";
request.send(null);
}

function shuffleVideo() {
getData(() => {
    if (!data || data.length === 0) return;

    titleArea.innerHTML = data[number].title;
    contentArea.innerHTML = data[number].content;
    videoArea.setAttribute("src", data[number].url);

    number = (number + 1) % data.length; // Cycle through data
});
}

window.onload = function () {
button.addEventListener("click", shuffleVideo);
};