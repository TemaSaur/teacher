const form = document.querySelector("form#questions")

form.onsubmit = (e) => {
	e.preventDefault()
	console.log(e)
}
