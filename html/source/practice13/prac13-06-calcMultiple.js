// 웹 페이지로부터 두 수가 오기를 기다린다.
onmessage = function (e) {
	let result;
	let op1 = parseInt(e.data.op1);
	let op2 = parseInt(e.data.op2);
	result = op1 * op2; 
	postMessage(result);
}
