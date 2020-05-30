function searchFromTables() {
  var  table1,table2,table3,table4,table5,table6, tr;

  table1 = document.getElementById("table1");
  tr = table1.getElementsByTagName("tr");
  search(tr, "warning1");

  table2 = document.getElementById("table2");
  tr = table2.getElementsByTagName("tr");
  search(tr, "warning2");

  table3 = document.getElementById("table3");
  tr = table3.getElementsByTagName("tr");
  search(tr, "warning3");

  table4 = document.getElementById("table4");
  tr = table4.getElementsByTagName("tr");
  search(tr, "warning4");

  table5 = document.getElementById("table5");
  tr = table5.getElementsByTagName("tr");
  search(tr, "warning5");

  table6 = document.getElementById("table6");
  tr = table6.getElementsByTagName("tr");
  search(tr, "warning6");
}

// This function search on Position name, Description, Expectation
function search(trWhole,warningID) {
  var input, filter, tdFirst,tdSecond,tdThird, tdFourth, i,
      message,txtValue2,txtValue3,txtValue4,warning;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  for (i = 0; i < trWhole.length; i++) {
    // Take each column to search
    tdSecond = trWhole[i].getElementsByTagName("td")[1];
    tdThird = trWhole[i].getElementsByTagName("td")[2];
    tdFourth = trWhole[i].getElementsByTagName("td")[3];
    if (tdSecond || tdThird || tdFourth) {

      txtValue2 = tdSecond.textContent || tdSecond.innerText;
      txtValue3 = tdThird.textContent || tdThird.innerText;
      txtValue4 = tdFourth.textContent || tdFourth.innerText;
      if (txtValue2.toUpperCase().indexOf(filter) > -1 ||
          txtValue3.toUpperCase().indexOf(filter) > -1 ||
          txtValue4.toUpperCase().indexOf(filter) > -1) {
        // Show if there is a match
        trWhole[i].style.display = "";
        for (var j = 0; j < trWhole.length; j++)
          if(trWhole[j].style.display === ""){
            warningDisplay("none",warningID);
            break;
        }
      }
      else {
        // Hide if there is no match
        trWhole[i].style.display = "none";
        var flagCount=0;
        for (var j = 0; j < trWhole.length; j++)
          if(trWhole[j].style.display === "none"){
            flagCount++;
        }
        //We should subtract 3 because we have three extra row which is standard(city name, software name,warning message)
        if (flagCount === trWhole.length-3){
          warningDisplay("",warningID)
        }
      }
    }
  }
}

function warningDisplay(value, ID) {
  var warning;
  warning = document.getElementById(ID);
  warning.style.display=value;
}