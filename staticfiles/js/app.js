/* main title transition */
const title = document.getElementById("title")
const strText = title.textContent;
const splitText = strText.split("");

title.textContent = "";

for(let i=0; i < splitText.length; i++){
    title.innerHTML += "<span>" + splitText[i] + "</span>";
}

let char = 0;
let timer = setInterval(onTick, 50);

function onTick(){
    const span = title.querySelectorAll('span')[char];
    span.classList.add('fadeout');
    char++;
    if(char === splitText.length){
        complete();
        return;
    }
}

function complete(){
    clearInterval(timer);
    timer = null;
}