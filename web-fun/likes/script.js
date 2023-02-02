var like = 3
var likeElement = document.querySelector(".like")

console.log(likeElement)

function add() {
    like++;
    likeElement.innerText = like + "like(s)"
    console.log(like);
}