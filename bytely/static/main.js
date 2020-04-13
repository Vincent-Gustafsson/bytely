let full_links = document.getElementsByClassName("full-link-td");

for (let i = 0; i < full_links.length; i++) {
    let element = full_links[i];
    if ( element.innerHTML.length > 50) {
        element.innerHTML = element.innerHTML.slice(0, 50) + "...";
    }
}