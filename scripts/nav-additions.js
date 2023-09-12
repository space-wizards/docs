// Un-active everything when you click it
Array.prototype.forEach.call(document.getElementsByClassName("pagetoc")[0].children, function(el) {
    el.addEventHandler("click", function() {
        Array.prototype.forEach.call(document.getElementsByClassName("pagetoc")[0].children, function(el) {
            el.classList.remove("active");
        });
        el.classList.add("active");
    });
});

var updateFunction = function() {

    var id;
    var elements = document.getElementsByClassName("header");
    Array.prototype.forEach.call(elements, function(el) {
        if (window.pageYOffset >= el.offsetTop) {
            id = el;
        }
    });

    Array.prototype.forEach.call(document.getElementsByClassName("pagetoc")[0].children, function(el) {
        el.classList.remove("active");
    });

    if (id == undefined)
        return;

    Array.prototype.forEach.call(document.getElementsByClassName("pagetoc")[0].children, function(el) {
        if (id.href.localeCompare(el.href) == 0) {
            el.classList.add("active");
        }
    });
};

window.addEventListener('load', function() {

    /* Scroll the page index on the left to the current active page */
    var active = document.querySelector(".chapter li a.active");
    active.scrollIntoView({ behavior: "instant", block: "center", inline: "nearest" });

    /* Populate subpage footer */

    /* Get next sibling of active list element
       then check if it has a nested ol
       if so, this implies our current active element has nested subpages */
    var nextListEl = active.parentElement.nextElementSibling;
    var footer = document.getElementById("subpage-footer");
    footer.style.display = "none";
    if (nextListEl != null)
    {
        console.log(nextListEl);
        var list = nextListEl.querySelector(".section")
        if (list != null)
        {
            footer.style.display = "block";
            footer.appendChild(list.cloneNode(true));
        }
    }

    /* Populate pagetoc sidebar */

    var pagetoc = document.getElementsByClassName("pagetoc")[0];
    var elements = document.getElementsByClassName("header");
    // don't show pagetoc sidebar with less than 2 headers
    if (elements.length < 2)
        return;

    Array.prototype.forEach.call(elements, function(el) {
        var link = document.createElement("a");

        // Indent shows hierarchy
        var indent = "";
        switch (el.parentElement.tagName) {
            case "H2":
                indent = "20px";
                break;
            case "H3":
                indent = "40px";
                break;
            case "H4":
                indent = "60px";
                break;
            case "H5":
                indent = "80px";
            default:
                break;
        }

        link.appendChild(document.createTextNode(el.text));
        link.style.paddingLeft = indent;
        link.href = el.href;
        pagetoc.appendChild(link);
    });
    updateFunction.call();
});



// Handle active elements on scroll
window.addEventListener("scroll", updateFunction);
