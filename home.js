var reviewButton = document.getElementById("review_button");

reviewButton.addEventListener("click", () =>
    fetch('http://localhost:5000/tra/reviews').then(r => r.text()).then(result => {
        document.getElementById("review_lst").innerHTML = result
    })
)