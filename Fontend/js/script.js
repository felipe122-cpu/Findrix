
const menuBtn= document.getElementById("menuBtn")
const navlinks= document.getElementById("navlinks")
const links= navlinks.querySelectorAll("a")

menuBtn.addEventListener("click",( ) =>
{
    navlinks.classList.toggle("active");
    if(navlinks.classList.contains("active")){
        menuBtn.innerHTML= "x";
        menuBtn.setAttribute("aria-expanded" , "true")
    }
    else{
        menuBtn.innerHTML="☰";
        menuBtn.setAttribute("aria-expanded" , "false")
    }
}
);

links.forEach(link =>
{
    link.addEventListener(
        "click" , () =>{
            navlinks.classList.remove("active")
            menuBtn.innerHTML="☰";
            menuBtn.setAttribute("aria-expanded" , "false");
        }
    )
}
)