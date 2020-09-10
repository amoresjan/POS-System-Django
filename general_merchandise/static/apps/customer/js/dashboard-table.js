$(document).ready(function () {
  $(".data-table").DataTable({
    dom: "Bfrtip",
    buttons: [
      {
        extend: "excel",
        exportOptions: {
          columns: [0, 1, 2, 3],
        },
      },
    ],
  });
});
``;
