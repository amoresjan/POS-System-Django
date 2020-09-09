$(".mydatatable").dataTable({
	pageLength: 5,
	bLengthChange: false,
	scrollCollapse: false,
	searching: false,
	columnDefs: [{ orderable: false, targets: -1 }],
});
