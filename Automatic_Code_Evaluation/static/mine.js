// Function for toggle div
function toggle(){
    var x=document.getElementById("mycode") // Element ID of the element we want to toggle
    if(x.style.display === "none"){
        x.style.display = "block";
    }
    else{
        x.style.display = "none";
    }
}

// Function to change div
function show(x){
    if(x==1){
        document.getElementById("mycode").style.display="block";
    }
    else{
        document.getElementById("mycode").style.display="none";
    }
}

// Add textboxes on click
function add(type) {

    //Create an input type dynamically.
    var element = document.createElement("textarea"); // input for : input element
    var text = document.getElementById("mycode");

    //Append the element in page (in span).
    text.appendChild(element);

}

// Highlight the active button
// Add active class to the current button (highlight it)
function makeActive() {
  var element = document.getElementById("l1");
  element.classList.add("active");
} 
