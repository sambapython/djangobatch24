
// alert("HELLO world");
function erase_others(value){
	alert("clicked on "+value);
	var male_element = document.getElementById("male");
	var female_element = document.getElementById("female");
	var other_element = document.getElementById("other");
	console.log(male_element);
	if(value == "male"){
		female_element.checked=false;
		other_element.checked=false;

	}
	else if(value == "female"){
		male_element.checked=false;
		other_element.checked=false;

	}
	else{
		female_element.checked=false;
		male_element.checked=false;

	}


}	
function changecolor(color){
	document.body.style.color=color;
}