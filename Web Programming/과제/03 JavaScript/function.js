function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}
  
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}


function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}

var itemsIndex = [];
var itemsList = [];
var itemsPrice = [39800,49800,59800,69800,89800,99800,59800,29800,10800,24800,49800,12800,15800];

function itemSelect(){

    var itemSelect = document.getElementById("itemList");

    var selectedItem = itemSelect.options[itemSelect.selectedIndex].title;
    var selectedItemIndex = itemSelect.selectedIndex;

    console.log(itemsIndex);

    if(!itemsIndex.includes(selectedItemIndex)){
        if(selectedItemIndex == 0)
            return;

        itemsIndex[selectedItemIndex] = selectedItemIndex;

        var order_area = document.getElementById("order_area");
    
        var li = document.createElement("li");
        var cell = document.createElement("div");
    
        var name = document.createElement("label");
        name.for = "item" + selectedItemIndex;
        name.appendChild(document.createTextNode(selectedItem));
    
        var input = document.createElement("input");
        input.id = "item" + selectedItemIndex;
        input.type = "text";
        input.maxLength = "5";
        input.value = "1";
    
        var plus = document.createElement("button");
        plus.className = "plus";
        plus.appendChild(document.createTextNode("+"))
    
        var minus = document.createElement("button");
        minus.className = "mius";
        minus.appendChild(document.createTextNode("-"))
    
        var del = document.createElement("button");
        del.className = "del";
        del.appendChild(document.createTextNode("x"));
    
        var price_span = document.createElement("span");
        price_span.className = "price_span";
    
        var price = document.createElement("label");
        price.appendChild(document.createTextNode(itemsPrice[selectedItemIndex-1]))
    
        var price_won = document.createElement("span");
        price_won.appendChild(document.createTextNode("원"));
    
        cell.appendChild(name); 
        cell.appendChild(input);
        cell.appendChild(plus);
        cell.appendChild(minus);
        cell.appendChild(del);
        cell.appendChild(price_span);
        cell.appendChild(price);
        cell.appendChild(price_won);
        li.appendChild(cell);

        itemsList.push(li);
    
        order_area.appendChild(li);
        itemSelect.options[0].selected = true;
        
        plus.addEventListener('click', function(){
            input.value = Number(input.value) + 1
        })

        minus.addEventListener('click', function(){
            if(Number(input.value) > 1)
                input.value = Number(input.value) - 1
        })

        del.addEventListener('click', function(){
            li.parentNode.removeChild(li)

            itemsList.remove
        })

        var acc = document.getElementsByClassName("accordion")[2];
        var panel = acc.nextElementSibling;
        panel.style.maxHeight = panel.scrollHeight + "px";
    }
}

function setTotalPrice(){
    var price = document.getElementsByClassName("price")
    price.appendChild()
}

function plus(){
    
}

function minus(){

}