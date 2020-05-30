function searchFromTables() {
  var  table1,table2,table3,table4,table5,table6, tr;

  table1 = document.getElementById("table1");
  tr = table1.getElementsByTagName("tr");
  search(tr);

  table2 = document.getElementById("table2");
  tr = table2.getElementsByTagName("tr");
  search(tr);

  table3 = document.getElementById("table3");
  tr = table3.getElementsByTagName("tr");
  search(tr);

  table4 = document.getElementById("table4");
  tr = table4.getElementsByTagName("tr");
  search(tr);

  table5 = document.getElementById("table5");
  tr = table5.getElementsByTagName("tr");
  search(tr);

  table6 = document.getElementById("table6");
  tr = table6.getElementsByTagName("tr");
  search(tr);
}

function search(tr) {
  var input, filter, tdFirst,tdSecond,tdThird, tdFourth, i, txtValue1,txtValue2,txtValue3,txtValue4;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  for (i = 0; i < tr.length; i++) {
    tdFirst = tr[i].getElementsByTagName("td")[0];
    tdSecond = tr[i].getElementsByTagName("td")[1];
    tdThird = tr[i].getElementsByTagName("td")[2];
    tdFourth = tr[i].getElementsByTagName("td")[3];
    if (tdFirst || tdSecond || tdThird) {
      txtValue1 = tdFirst.textContent || tdFirst.innerText;
      txtValue2 = tdSecond.textContent || tdSecond.innerText;
      txtValue3 = tdThird.textContent || tdThird.innerText;
      txtValue4 = tdFourth.textContent || tdFourth.innerText;
      if (txtValue1.toUpperCase().indexOf(filter) > -1 ||
          txtValue2.toUpperCase().indexOf(filter) > -1 ||
          txtValue3.toUpperCase().indexOf(filter) > -1 ||
          txtValue4.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      }
      else {
        tr[i].style.display = "none";
      }
    }
  }
}