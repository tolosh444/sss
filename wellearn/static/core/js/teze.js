document.getElementById("openModal").addEventListener("click", function() {
    document.getElementById("modal").style.display = "block";
  });
  
  document.getElementsByClassName("close")[0].addEventListener("click", function() {
    document.getElementById("modal").style.display = "none";
  });
  
  document.getElementById("deleteButton").addEventListener("click", function() {
    // Perform delete operation here
    document.getElementById("modal").style.display = "none";
  });
  