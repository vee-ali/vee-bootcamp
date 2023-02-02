console.log("hello")

function message() {
    (alert("Ninja was liked"))

}

function login(click) {
    if(click.innerText == "Login") {
        click.innerText = "Logout";
    } else {
        click.innerText = "Login";
    }
}

function remove(click) {
    click.remove();
}