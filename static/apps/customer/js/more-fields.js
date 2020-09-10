function addFields(x, y) {
	var clone = document.getElementById(y).cloneNode(true);
	document.getElementById(x).appendChild(clone);
}
