$(document).ready(function () {
  var oTable = $(".data-table").DataTable({
});

  $("#datepicker_from")
    .datepicker({
      showOn: "button",
      buttonImage: "images/calendar.gif",
      buttonImageOnly: false,
      onSelect: function (date) {
        minDateFilter = new Date(date).getTime();
        oTable.draw();
      },
    })
    .keyup(function () {
      minDateFilter = new Date(this.value).getTime();
      oTable.draw();
    });

  $("#datepicker_to")
    .datepicker({
      showOn: "button",
      buttonImage: "images/calendar.gif",
      buttonImageOnly: false,
      onSelect: function (date) {
        maxDateFilter = new Date(date).getTime();
        oTable.draw();
      },
    })
    .keyup(function () {
      maxDateFilter = new Date(this.value).getTime();
      oTable.draw();
    });
});

// Date range filter
minDateFilter = "";
maxDateFilter = "";

$.fn.dataTableExt.afnFiltering.push(function (oSettings, aData, iDataIndex) {
  if (typeof aData._date == "undefined") {
    aData._date = new Date(aData[3]).getTime();
  }

  if (minDateFilter && !isNaN(minDateFilter)) {
    if (aData._date < minDateFilter) {
      return false;
    }
  }

  if (maxDateFilter && !isNaN(maxDateFilter)) {
    if (aData._date > maxDateFilter) {
      return false;
    }
  }

  return true;
});
