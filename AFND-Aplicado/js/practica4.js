var btn1 = $('#btn1');
var btn2 = $('#btn2');
var inpt1 = $('#expression1');
var inpt2 = $('#expression2');
var frm1 = $('#form1');
var frm2 = $('#form2');

btn1.click(function() {
	a = new Automata1(inpt1.val());
	a.start();
	inputFeedback(frm1);
});

btn2.click(function() {
	a = new Automata2(inpt2.val());
	a.start();
	inputFeedback(frm2);
});

function inputFeedback(form) {
	form.removeClass('has-success has-feedback has-error');
	form.children('.glyphicon').remove();
	if(a.getState().message === 'estado final') {
		form.addClass('has-success has-feedback');
		form.append('<span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true"></span>');
	}
	else {
		form.addClass('has-error has-feedback');
		form.append('<span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true"></span>');
	}
}