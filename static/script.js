
       
async function postFormData(url, msgText){
  const data = {user_question: msgText};
  const response = await fetch(url,{
                    method: "POST",
                    body: JSON.stringify(data)
                })
                .then (response => response.json())
                .catch(error => console.log(error));
  console.log(response);
  if (response.status == "ok")
  {
      botResponse(response.message);
      url = "\nEn savoir plus : " + response.url;
      botResponse(response.summary+url);
      
      var lat= response.latitude;
      var lng= response.longitude;
      setTimeout(function(){appendMap(lat, lng);}, 3000);
      //appendMap(lat, lng);
  }
  else
  {
    botResponse(response.message);
  }

}

const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");

// Icons made by Freepik from www.flaticon.com
const BOT_IMG = "https://media.gettyimages.com/vectors/robot-face-icon-smiling-devil-face-emotion-robotic-emoji-vector-id819604502";
const PERSON_IMG = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.w600.comps.canstockphoto.fr%2Fbrun-lignes-visage-rond-dessin-anim%25C3%25A9-illustration_csp64434926.jpg&imgrefurl=https%3A%2F%2Fwww.canstockphoto.fr%2Fbrun-lignes-visage-rond-dessin-anim%25C3%25A9-64434926.html&tbnid=blsdpCF4ms3JSM&vet=12ahUKEwj1qqaM6Mn1AhVPw7sIHeHaDBcQMyg9egQIARBb..i&docid=TduyBMlfpq-RLM&w=500&h=520&q=visage%20dessin%20anim%C3%A9%20icone&hl=fr&ved=2ahUKEwj1qqaM6Mn1AhVPw7sIHeHaDBcQMyg9egQIARBb";
const BOT_NAME = "GRANDPYBOT";
const PERSON_NAME = "USER";

var index = 1;

msgerForm.addEventListener("submit", event => {
  event.preventDefault();

  const msgText = msgerInput.value;
  if (!msgText) return;

  appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);

  const response = postFormData("/question", msgText);  
});

function appendMessage(name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}

function appendMap(lat, lng) {
  //   Simple solution for small apps
  const msgHTML = `
        <div onload="initMap()"></div>
        <div id="map${index}" style="width:100%; height: 100%" </div>
  `;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
  initMap(lat,lng, index);
  index++;
}

function botResponse(response) {
  //const r = random(0, BOT_MSGS.length - 1);
  //const msgText = BOT_MSGS[r];
  const msgText = response

  setTimeout(() => {
    appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
  }, 1000);
}

// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}

function random(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}
var map;
function initMap(lat, lng) {
  var pos = {lat:parseFloat(lat), lng:parseFloat(lng)};
  var map = new google.maps.Map(document.getElementById('map'+index),{
    zoom: 10,
    center:pos
  });
  var marker = new google.maps.Marker({
    position:pos,
    map:map
  });
}


