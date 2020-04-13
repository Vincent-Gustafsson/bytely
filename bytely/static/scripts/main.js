let full_links = document.getElementsByClassName("full-link-td");

const customLinkCheckbox = document.querySelector('input[name="want-custom-link"]');
const customLinkInput = document.querySelector('input[name="custom-link"]');
customLinkInput.style.display = "none";

for (let i = 0; i < full_links.length; i++) {
    let element = full_links[i];
    if ( element.innerHTML.length > 50) {
        element.innerHTML = element.innerHTML.slice(0, 50) + "...";
    }
}


customLinkCheckbox.addEventListener('change', () => {
    console.log(customLinkCheckbox.checked);
    if(customLinkCheckbox.checked) {
        customLinkInput.style.display = "inline-block";
    } else {
        customLinkInput.style.display = "none";
    }
});