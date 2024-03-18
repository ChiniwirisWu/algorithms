//set answers to each anwer input[type="radio"]
const answer_radio = document.querySelectorAll('.result_radio')
answer_radio.forEach((val, ind)=>{
	console.log('hi')
	val.setAttribute('value', ind)
})



